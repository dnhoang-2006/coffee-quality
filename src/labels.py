"""Conservative label normalization and rare-category grouping for CQI data.

Missing values stay missing. Literal labels such as ``None`` and ``Other``
remain labels; deciding their meaning is a separate cleaning decision.
"""

from numbers import Integral

import pandas as pd


CAT_COLS = (
    "Species", "Continent.of.Origin", "Country.of.Origin",
    "Variety", "Color", "Processing.Method",
)

# Keys and values use the same whitespace/case convention as normalize_labels.
# Geographic subdivisions (e.g. Hawaii) are deliberately not collapsed here.
COUNTRY_ALIASES = {
    "united states of america": "united states",
    "tanzania, united republic of": "tanzania",
    "united republic of tanzania": "tanzania",
    "viet nam": "vietnam",
    "lao people's democratic republic": "laos",
    "cote divoire": "cote d'ivoire",
    "côte d'ivoire": "cote d'ivoire",
    "côte d’ivoire": "cote d'ivoire",
}


def normalize_labels(df):
    """Return a copy with the six available categorical columns normalized.

    Trim and collapse whitespace, use Unicode casefold, then apply explicit
    country aliases. Do not infer synonyms for varieties, colors or processing
    methods. Absent categorical columns are skipped; other columns are intact.
    Empty/whitespace-only strings become missing, but literal ``None`` becomes
    ``none``. Normalize before grouping or joining; keep the raw frame separately.
    """
    result = df.copy(deep=True)
    for column in CAT_COLS:
        if column not in result.columns:
            continue
        nonmissing = result[column].dropna()
        if not all(isinstance(value, str) for value in nonmissing):
            raise TypeError(f"{column} must contain text labels or missing values")
        labels = (
            result[column].astype("string")
            .str.strip().str.replace(r"\s+", " ", regex=True).str.casefold()
        )
        labels = labels.mask(labels.eq(""), pd.NA)
        if column == "Country.of.Origin":
            labels = labels.replace(COUNTRY_ALIASES)
        result[column] = labels
    return result


def group_rare(s, min_n=20, other="Other (rare)"):
    """Return a Series grouping nonmissing labels with count < min_n.

    Counts refer to the supplied analysis sample. A label with exactly min_n
    rows is retained. Missing values and the input Series are preserved.
    A pre-existing output label is rejected when grouping is needed, to avoid
    silently merging an original label with newly grouped categories.
    """
    if isinstance(min_n, bool) or not isinstance(min_n, Integral) or min_n < 1:
        raise ValueError("min_n must be a positive integer")
    if not isinstance(other, str) or not other.strip():
        raise ValueError("other must be a nonempty text label")
    counts = s.value_counts(dropna=True)
    rare_labels = counts[counts.lt(min_n)].index
    rare_mask = s.notna() & s.isin(rare_labels)
    result = s.copy(deep=True)
    if not rare_mask.any():
        return result
    if s.eq(other).fillna(False).any():
        raise ValueError(f"Output label {other!r} already exists; choose another label")
    if isinstance(result.dtype, pd.CategoricalDtype):
        result = result.cat.add_categories([other])
    return result.where(~rare_mask, other)
