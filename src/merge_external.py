"""Load FAOSTAT production and audit its country–harvest year join with CQI."""

import pandas as pd

from .labels import normalize_labels
from .config import EXTERNAL

FAOSTAT_FILE = EXTERNAL / "FAOSTAT_coffee.csv"


# Keys follow normalize_labels(), values preserve FAOSTAT QCL data-row names.
# Japan is a recognized area name but has no rows in this coffee extract.
# All 16 CQI lots labeled China were matched to source records from Yunnan.
# Source: github.com/jldbc/coffee-quality-database/blob/master/data/arabica_data_cleaned.csv
# Keep the separate CQI Taiwan label mapped to its own FAOSTAT series.
COUNTRY_MAP = {
    "ethiopia": "Ethiopia", "guatemala": "Guatemala", "brazil": "Brazil",
    "peru": "Peru", "united states": "United States of America",
    "indonesia": "Indonesia", "china": "China, mainland",
    "costa rica": "Costa Rica", "mexico": "Mexico", "uganda": "Uganda",
    "honduras": "Honduras", "taiwan": "China, Taiwan Province of",
    "nicaragua": "Nicaragua", "tanzania": "United Republic of Tanzania",
    "kenya": "Kenya", "thailand": "Thailand", "colombia": "Colombia",
    "panama": "Panama", "papua new guinea": "Papua New Guinea",
    "el salvador": "El Salvador", "japan": "Japan", "ecuador": "Ecuador",
    "haiti": "Haiti", "burundi": "Burundi", "vietnam": "Viet Nam",
    "philippines": "Philippines", "rwanda": "Rwanda", "malawi": "Malawi",
    "laos": "Lao People's Democratic Republic", "zambia": "Zambia",
    "myanmar": "Myanmar", "mauritius": "Mauritius",
    "cote d'ivoire": "Côte d'Ivoire", "india": "India",
}


def load_fao(path=FAOSTAT_FILE):
    """Load country–year production in tonnes from the filtered FAOSTAT CSV."""
    fao = pd.read_csv(
        path,
        usecols=["Area", "Year", "Value"],
        dtype={"Area": "string", "Year": "Int64", "Value": "Float64"},
    ).rename(columns={"Area": "country_fao", "Year": "year", "Value": "production_t"})
    keys = ["country_fao", "year"]
    if fao[keys].isna().any().any():
        raise ValueError("FAOSTAT contains a missing country or year key")
    duplicates = fao.loc[fao.duplicated(keys, keep=False), keys].drop_duplicates()
    if not duplicates.empty:
        raise ValueError(f"Duplicate FAOSTAT country–year keys:\n{duplicates.to_string(index=False)}")
    return fao[[*keys, "production_t"]]


def audit_country_mapping(cqi, fao):
    """Return one row per observed CQI country, including unmapped/missing ones.

    This checks names only, not harvest-year compatibility or value availability.
    Japan is deliberately left without a substitute if absent in coffee data.
    """
    labels = normalize_labels(cqi)["Country.of.Origin"]
    counts = labels.value_counts(dropna=False)
    area_column = "country_fao" if "country_fao" in fao else "Area"
    areas = set(fao[area_column].dropna())
    rows = []
    for country, count in counts.items():
        missing = pd.isna(country)
        area = COUNTRY_MAP.get(country) if not missing else None
        available = area in areas if area is not None else False
        status = (
            "missing_cqi_country" if missing else
            "unmapped" if area is None else
            "absent_in_coffee_extract" if not available else
            "name_matched"
        )
        rows.append({"cqi_country": country, "fao_area": area,
                     "n_cqi_lots": int(count), "area_available": available,
                     "status": status})
    return pd.DataFrame(rows)


def merge_production(cqi, fao):
    """Left join CQI lots to loaded FAOSTAT data and annotate each row's status.

    Preserve original CQI columns. Match normalized country names and integer
    harvest years, keeping missing keys and missing production visible.
    """
    country = normalize_labels(cqi[["Country.of.Origin"]])["Country.of.Origin"]
    year = pd.to_numeric(cqi["Harvest.Year"], errors="coerce")
    if (year.dropna() % 1 != 0).any():
        raise ValueError("Harvest years must be integers")
    left = cqi.assign(
        cqi_country=country,
        country_fao=country.map(COUNTRY_MAP),
        year=year.astype("Int64"),
    )
    result = left.merge(fao, on=["country_fao", "year"], how="left",
                        validate="many_to_one", indicator=True)
    if len(result) != len(cqi):
        raise ValueError("Candidate join changed CQI row count")
    result["status"] = "candidate_matched"
    result.loc[result["production_t"].isna(), "status"] = "matched_key_missing_value"
    result.loc[result["_merge"].eq("left_only"), "status"] = "no_fao_country_year"
    result.loc[result["country_fao"].isna(), "status"] = "unmapped_country"
    result.loc[result["year"].isna(), "status"] = "missing_harvest_year"
    result.loc[result["cqi_country"].isna(), "status"] = "missing_cqi_country"
    return result


def audit_country_year(cqi, fao):
    """Return the Week 1 audit columns, including flags from a raw FAOSTAT CSV."""
    right = fao[["Area", "Year", "Value", "Flag", "Area Code (M49)"]].rename(
        columns={"Area": "country_fao", "Year": "year", "Value": "production_t"}
    )
    result = merge_production(cqi[["REC_ID", "Country.of.Origin", "Harvest.Year"]], right)
    columns = ["REC_ID", "cqi_country", "country_fao", "year", "production_t",
               "Flag", "Area Code (M49)", "_merge", "status"]
    return result[columns].rename(columns={"country_fao": "fao_area"})


def main():
    import json
    from .config import RAW

    cqi = pd.read_csv(RAW / "Coffee_Qlty.csv", keep_default_na=False, na_values=[""])
    fao = pd.read_csv(FAOSTAT_FILE, dtype={"Area Code (M49)": "string", "Item Code (CPC)": "string"})
    countries = audit_country_mapping(cqi, fao)
    candidate = audit_country_year(cqi, fao)
    summary = {
        "purpose": "audit CQI coverage by FAOSTAT country and harvest year",
        "cqi_rows_before": len(cqi), "candidate_rows_after": len(candidate),
        "country_name_statuses": {str(k): int(v) for k, v in countries["status"].value_counts().items()},
        "lot_statuses": {str(k): int(v) for k, v in candidate["status"].value_counts().items()},
        "left_rows_without_country_year_match": int(candidate["_merge"].eq("left_only").sum()),
        "left_distinct_complete_unmatched_keys": int(candidate.loc[
            candidate["_merge"].eq("left_only") & candidate["fao_area"].notna() & candidate["year"].notna(),
            ["fao_area", "year"]].drop_duplicates().shape[0]),
        "note": "Status categories are exclusive; missing country has priority over missing year.",
    }
    # Print diagnostics only; keep external/ limited to source CSV + README.
    print(countries.to_string(index=False))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
