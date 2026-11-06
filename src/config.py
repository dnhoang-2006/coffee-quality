from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
EXTERNAL = ROOT / "data" / "external"
RANDOM_STATE = 42
SCORE_COLS = ["Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance",
              "Uniformity", "Clean.Cup", "Sweetness"]


def add_total_score(df):
    """Return a copy with the sum of all nine sensory scores, or NA if incomplete."""
    out = df.copy()
    out["total_9"] = out[SCORE_COLS].sum(axis=1, min_count=len(SCORE_COLS))
    return out
