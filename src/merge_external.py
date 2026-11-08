"""Draft CQI -> FAOSTAT names; no production/quality analysis is performed here."""

from .labels import normalize_labels
from .config import EXTERNAL

FAOSTAT_FILE = EXTERNAL / "FAOSTAT_coffee.csv"


# Keys follow normalize_labels(), values preserve FAOSTAT QCL data-row names.
# These names must be checked again if the source release changes.
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

# CQI's broad "China" label needs provenance confirmation before a final join.
PROVISIONAL_COUNTRIES = {"china"}


def audit_country_mapping(cqi, fao):
    """Return one row per observed CQI country, including unmapped/missing ones.

    This checks names only, not harvest-year compatibility or value availability.
    Japan is deliberately left without a substitute if absent in coffee data.
    """
    import pandas as pd

    labels = normalize_labels(cqi)["Country.of.Origin"]
    counts = labels.value_counts(dropna=False)
    areas = set(fao["Area"].dropna())
    rows = []
    for country, count in counts.items():
        missing = pd.isna(country)
        area = COUNTRY_MAP.get(country) if not missing else None
        available = area in areas if area is not None else False
        status = (
            "missing_cqi_country" if missing else
            "unmapped" if area is None else
            "absent_in_coffee_extract" if not available else
            "provisional_geographic_scope" if country in PROVISIONAL_COUNTRIES else
            "name_matched"
        )
        rows.append({"cqi_country": country, "fao_area": area,
                     "n_cqi_lots": int(count), "area_available": available,
                     "status": status})
    return pd.DataFrame(rows)


def audit_country_year(cqi, fao):
    """Preflight a many-to-one candidate join, without approving scope choices.

    Only harvest year is used. Missing years are not inferred from expiration.
    The result is an audit artifact, not the dataset for research conclusions.
    """
    import pandas as pd

    normalized = normalize_labels(cqi)
    year = pd.to_numeric(cqi["Harvest.Year"], errors="coerce")
    if (year.dropna() % 1 != 0).any():
        raise ValueError("Harvest years must be integers")
    left = pd.DataFrame({
        "REC_ID": cqi["REC_ID"],
        "cqi_country": normalized["Country.of.Origin"],
        "fao_area": normalized["Country.of.Origin"].map(COUNTRY_MAP),
        "year": year.astype("Int64"),
    })
    right = fao[["Area", "Year", "Value", "Flag", "Area Code (M49)"]].rename(
        columns={"Area": "fao_area", "Year": "year", "Value": "production_t"}
    )
    result = left.merge(right, on=["fao_area", "year"], how="left",
                        validate="many_to_one", indicator=True)
    if len(result) != len(cqi):
        raise ValueError("Candidate join changed CQI row count")
    result["status"] = "candidate_matched"
    result.loc[result["cqi_country"].isin(PROVISIONAL_COUNTRIES), "status"] = "provisional_geographic_scope"
    result.loc[result["production_t"].isna(), "status"] = "matched_key_missing_value"
    result.loc[result["_merge"].eq("left_only"), "status"] = "no_fao_country_year"
    result.loc[result["fao_area"].isna(), "status"] = "unmapped_country"
    result.loc[result["year"].isna(), "status"] = "missing_harvest_year"
    result.loc[result["cqi_country"].isna(), "status"] = "missing_cqi_country"
    return result


def main():
    import json
    import pandas as pd
    from .config import RAW

    cqi = pd.read_csv(RAW / "Coffee_Qlty.csv", keep_default_na=False, na_values=[""])
    fao = pd.read_csv(FAOSTAT_FILE, dtype={"Area Code (M49)": "string", "Item Code (CPC)": "string"})
    countries = audit_country_mapping(cqi, fao)
    candidate = audit_country_year(cqi, fao)
    summary = {
        "purpose": "preflight only; no final research join approved",
        "cqi_rows_before": len(cqi), "candidate_rows_after": len(candidate),
        "country_name_statuses": {str(k): int(v) for k, v in countries["status"].value_counts().items()},
        "lot_statuses": {str(k): int(v) for k, v in candidate["status"].value_counts().items()},
        "left_rows_without_country_year_match": int(candidate["_merge"].eq("left_only").sum()),
        "left_distinct_complete_unmatched_keys": int(candidate.loc[
            candidate["_merge"].eq("left_only") & candidate["fao_area"].notna() & candidate["year"].notna(),
            ["fao_area", "year"]].drop_duplicates().shape[0]),
        "provisional_country_choices": {c: COUNTRY_MAP[c] for c in PROVISIONAL_COUNTRIES},
        "note": "Status categories are exclusive; missing country has priority over missing year.",
    }
    # Print diagnostics only; keep external/ limited to source CSV + README.
    print(countries.to_string(index=False))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
