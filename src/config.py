from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
EXTERNAL = ROOT / "data" / "external"
RANDOM_STATE = 42
SCORE_COLS = ["Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance",
              "Uniformity", "Clean.Cup", "Sweetness"]
