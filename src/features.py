from src.config import SCORE_COLS


def add_total_score(df):
    """Trả về bản sao có cột total_9 = tổng 9 thuộc tính cảm quan (NA nếu thiếu thuộc tính nào)."""
    out = df.copy()
    out["total_9"] = out[SCORE_COLS].sum(axis=1, min_count=len(SCORE_COLS))
    return out
