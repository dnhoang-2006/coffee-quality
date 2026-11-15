from src.config import SCORE_COLS


def add_total_score(df):
    """Trả về bản sao có cột total_9 = tổng 9 thuộc tính cảm quan (NA nếu thiếu thuộc tính nào)."""
    out = df.copy()
    out["total_9"] = out[SCORE_COLS].sum(axis=1, min_count=len(SCORE_COLS))
    return out


def add_grading_date(df):
    """Trả về bản sao có cột grading_date = Expiration − 365 ngày.

    Giả định: chứng nhận CQI có hiệu lực 1 năm kể từ ngày chấm (cupping), nên ngày
    chấm ≈ ngày hết hạn trừ 365 ngày. Cột ``Expiration`` phải đã là datetime (gọi hàm
    này sau ``convert_types``); nếu không sẽ ``raise TypeError``.
    """
    import pandas as pd

    if "Expiration" not in df.columns:
        raise KeyError("Thiếu cột 'Expiration' để tính grading_date")
    if not pd.api.types.is_datetime64_any_dtype(df["Expiration"]):
        raise TypeError(
            f"Cột 'Expiration' phải là datetime (đang là {df['Expiration'].dtype}); "
            "hãy gọi convert_types trước add_grading_date"
        )
    out = df.copy()
    out["grading_date"] = out["Expiration"] - pd.Timedelta(days=365)
    return out
