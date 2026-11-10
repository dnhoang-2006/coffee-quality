"""Các hàm đọc dữ liệu gốc, ép kiểu và đánh dấu giá trị giữ chỗ cho dữ liệu CQI.

Mọi hàm đều trả về một DataFrame mới và không chỉnh sửa trực tiếp DataFrame đầu vào.
"""

import pandas as pd

from src.config import RAW, SCORE_COLS


def load_raw(path=None):
    """Đọc file Coffee_Qlty.csv từ thư mục data/raw/ và trả về DataFrame mới.

    Dùng ``keep_default_na=False, na_values=[""]`` giống notebook 01 để chỉ coi ô
    trống là giá trị thiếu (NaN) và bảo toàn chuỗi literal ``"None"`` ở cột ``Color``.
    """
    csv_path = (RAW / "Coffee_Qlty.csv") if path is None else path
    return pd.read_csv(csv_path, keep_default_na=False, na_values=[""])


def convert_types(df):
    """Trả về bản sao của DataFrame với cột thời gian được ép sang kiểu chuẩn.

    - ``Expiration``: chuyển sang ``datetime64[ns]`` theo định dạng ``%m/%d/%y``
      (với ``errors="coerce"``).
    - ``Harvest.Year``: chuyển sang số nguyên có hỗ trợ NA (``Int64``).
    """
    out = df.copy()
    if "Expiration" in out.columns:
        out["Expiration"] = pd.to_datetime(
            out["Expiration"], format="%m/%d/%y", errors="coerce"
        )
    if "Harvest.Year" in out.columns:
        out["Harvest.Year"] = pd.to_numeric(
            out["Harvest.Year"], errors="coerce"
        ).astype("Int64")
    return out


def flag_placeholders(df):
    """Trả về DataFrame boolean mask đánh dấu các dòng mang giá trị giữ chỗ ở mục 3.2.2.

    Quy tắc phát hiện dựa trên kết quả khám phá ở mục 3.2.2:
    - ``zero_all_scores``: cả 9 cột trong ``SCORE_COLS`` đều bằng 0 (hoặc ``REC_ID == 1310``),
      là bản ghi lỗi chưa có kết quả cupping được điền số 0 giữ chỗ.
      Lưu ý: lô ``REC_ID = 1306`` chỉ có riêng ``Clean.Cup = 0`` còn 8 cột khác hợp lệ
      nên là giá trị thật, không bị đánh dấu ở cột này.
    - ``zero_moisture``: ``Moisture == 0`` (264 lô có độ ẩm bằng 0,00 — giá trị quy ước
      khi không đo độ ẩm hạt nhân xanh).
    - ``any_placeholder``: dòng có ít nhất một trong các dấu hiệu giữ chỗ trên.
    """
    masks = pd.DataFrame(index=df.index)
    if set(SCORE_COLS).issubset(df.columns):
        zero_all_scores = df[SCORE_COLS].eq(0).all(axis=1)
    elif "REC_ID" in df.columns:
        zero_all_scores = df["REC_ID"].eq(1310)
    else:
        zero_all_scores = pd.Series(False, index=df.index)

    if "REC_ID" in df.columns:
        zero_all_scores = zero_all_scores | df["REC_ID"].eq(1310)

    if "Moisture" in df.columns:
        zero_moisture = pd.to_numeric(df["Moisture"], errors="coerce").eq(0).fillna(False)
    else:
        zero_moisture = pd.Series(False, index=df.index)

    masks["zero_all_scores"] = zero_all_scores.astype(bool)
    masks["zero_moisture"] = zero_moisture.astype(bool)
    masks["any_placeholder"] = masks["zero_all_scores"] | masks["zero_moisture"]
    return masks
