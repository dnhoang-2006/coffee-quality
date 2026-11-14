import pandas as pd

from src.config import SCORE_COLS


def add_total_score(df):
    """Trả về bản sao có cột total_9 = tổng 9 thuộc tính cảm quan (NA nếu thiếu thuộc tính nào)."""
    out = df.copy()
    out["total_9"] = out[SCORE_COLS].sum(axis=1, min_count=len(SCORE_COLS))
    return out


def add_defect_total(df):
    """Trả về bản sao có cột defects_total = Category.One.Defects + Category.Two.Defects + Quakers."""
    out = df.copy()
    out["defects_total"] = (
        out["Category.One.Defects"] + out["Category.Two.Defects"] + out["Quakers"]
    )
    return out


def bin_moisture(
    df,
    bins=(0, 0.10, 0.12, 1),
    labels=("<10%", "10–12%", ">12%"),
    right=False,
):
    """Trả về bản sao có cột moisture_band phân nhóm độ ẩm theo ngưỡng khuyến nghị SCA/ISO (10–12%)."""
    out = df.copy()
    out["moisture_band"] = pd.cut(
        out["Moisture"], bins=bins, labels=labels, right=right
    )
    return out
