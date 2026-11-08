"""Hàm thống kê dùng chung cho cả nhóm (tiêu chí D5: định lượng bất định).

- ``bootstrap_diff(a, b, stat)``: chênh lệch ``stat(a) - stat(b)`` giữa hai nhóm
  kèm CI 95%, vector hoá hoàn toàn bằng fancy indexing (Q1, Q3).
- ``bootstrap_ci(data, stat_fn)``: CI 95% cho một thống kê **bất kỳ** tính trên
  các dòng của ``data``, có tuỳ chọn lấy mẫu lại theo tầng (Q4: độ dốc xu hướng,
  lấy mẫu lại trong từng năm; Q5: hệ số tương quan Spearman giữa các quốc gia).
- ``cohens_d(a, b)``: độ lớn hiệu ứng (effect size) chuẩn hoá theo độ lệch chuẩn gộp.

Quy ước chung:
- Giá trị thiếu (NaN) trong ``a``/``b`` bị bỏ trước khi tính.
- Hàm trả về ``(giá_trị_quan_sát, np.array([ci_thấp, ci_cao]))``.
- ``seed`` mặc định lấy từ ``config.RANDOM_STATE`` để kết quả tái lập được.
"""

import numpy as np
import pandas as pd

from src.config import RANDOM_STATE


def _clean_1d(x, name):
    """Chuyển về mảng float 1 chiều, bỏ NaN; báo lỗi nếu rỗng."""
    arr = np.asarray(x, dtype=float).ravel()
    arr = arr[~np.isnan(arr)]
    if arr.size == 0:
        raise ValueError(f"{name} không có giá trị hợp lệ (rỗng hoặc toàn NaN)")
    return arr


def _check_ci(ci):
    if not 0 < ci < 100:
        raise ValueError("ci phải nằm trong khoảng (0, 100), ví dụ 95")
    return [(100 - ci) / 2, 100 - (100 - ci) / 2]


def bootstrap_diff(a, b, stat=np.median, n_boot=5000, seed=RANDOM_STATE, ci=95):
    """Chênh lệch stat(a) - stat(b) và khoảng tin cậy bằng bootstrap percentile.

    Lấy mẫu lại có hoàn lại **độc lập trong từng nhóm** (giữ nguyên cỡ mẫu mỗi
    nhóm). Toàn bộ ``n_boot`` lần lấy mẫu được sinh một lần dưới dạng ma trận chỉ
    số ``(n_boot, n)`` rồi dùng fancy indexing, không có vòng for Python.

    Parameters
    ----------
    a, b : array-like
        Hai mẫu cần so sánh (ví dụ ``total_9`` của nhóm Natural và Washed). NaN bị bỏ.
    stat : callable, mặc định ``np.median``
        Hàm thống kê nhận tham số ``axis`` (``np.median``, ``np.mean``...).
    n_boot : int
        Số lần lấy mẫu lại.
    seed : int
        Hạt giống cho ``np.random.default_rng``.
    ci : float
        Mức tin cậy (%), mặc định 95.

    Returns
    -------
    observed : float
        ``stat(a) - stat(b)`` trên dữ liệu gốc.
    interval : np.ndarray, shape (2,)
        ``[cận dưới, cận trên]`` của CI.

    Examples
    --------
    >>> diff, (lo, hi) = bootstrap_diff(natural, washed)
    >>> print(f"{diff:+.2f} điểm, CI 95% [{lo:.2f}, {hi:.2f}]")
    """
    q = _check_ci(ci)
    a, b = _clean_1d(a, "a"), _clean_1d(b, "b")
    rng = np.random.default_rng(seed)
    ia = rng.integers(0, len(a), (n_boot, len(a)))
    ib = rng.integers(0, len(b), (n_boot, len(b)))
    diffs = stat(a[ia], axis=1) - stat(b[ib], axis=1)
    return float(stat(a) - stat(b)), np.percentile(diffs, q)


def cohens_d(a, b):
    """Cohen's d = (mean(a) - mean(b)) / độ lệch chuẩn gộp (ddof=1).

    Quy ước đọc thô (Cohen, 1988): |d| ≈ 0.2 nhỏ, 0.5 vừa, 0.8 lớn.
    Trả về NaN nếu độ lệch chuẩn gộp bằng 0. NaN trong dữ liệu bị bỏ.
    """
    a, b = _clean_1d(a, "a"), _clean_1d(b, "b")
    na, nb = len(a), len(b)
    if na + nb < 3:
        raise ValueError("Cần tổng cộng ít nhất 3 quan sát để tính độ lệch chuẩn gộp")
    pooled_var = ((na - 1) * a.var(ddof=1 if na > 1 else 0)
                  + (nb - 1) * b.var(ddof=1 if nb > 1 else 0)) / (na + nb - 2)
    if pooled_var == 0:
        return np.nan
    return float((a.mean() - b.mean()) / np.sqrt(pooled_var))


def _resample_index(n, strata, n_boot, rng):
    """Ma trận vị trí (n_boot, n): lấy mẫu lại có hoàn lại, giữ cỡ mẫu từng tầng."""
    if strata is None:
        return rng.integers(0, n, (n_boot, n))
    codes, _ = pd.factorize(np.asarray(strata), use_na_sentinel=False)
    blocks = []
    for g in np.unique(codes):
        pos = np.flatnonzero(codes == g)
        blocks.append(pos[rng.integers(0, len(pos), (n_boot, len(pos)))])
    return np.hstack(blocks)


def bootstrap_ci(data, stat_fn, n_boot=2000, seed=RANDOM_STATE, ci=95, strata=None):
    """CI bootstrap percentile cho một thống kê bất kỳ, lấy mẫu lại theo **dòng**.

    Dùng khi thống kê phụ thuộc nhiều cột cùng lúc (độ dốc, hệ số tương quan...),
    nên phải lấy mẫu lại cả dòng để giữ cặp giá trị đi cùng nhau.

    Parameters
    ----------
    data : pd.DataFrame, pd.Series hoặc np.ndarray
        Mỗi dòng là một đơn vị quan sát (một lô, một quốc gia...).
    stat_fn : callable
        ``stat_fn(sample) -> float``, nhận vào cùng kiểu với ``data``.
    n_boot : int
        Số lần lấy mẫu lại (mặc định 2000 vì ``stat_fn`` được gọi trong vòng lặp).
    seed : int
        Hạt giống cho ``np.random.default_rng``.
    ci : float
        Mức tin cậy (%), mặc định 95.
    strata : str, array-like hoặc None
        Nếu có, lấy mẫu lại **trong từng tầng** để giữ nguyên số dòng mỗi tầng.
        Với DataFrame có thể truyền tên cột (ví dụ ``"Harvest.Year"``).

    Returns
    -------
    observed : float
        ``stat_fn(data)`` trên dữ liệu gốc.
    interval : np.ndarray, shape (2,)
        ``[cận dưới, cận trên]``. Các lần bootstrap cho NaN bị bỏ qua.

    Examples
    --------
    Q4: độ dốc median theo năm, lấy mẫu lại trong từng năm

    >>> def slope_of(s):
    ...     med = s.groupby("Harvest.Year")["total_9"].median()
    ...     return np.polyfit(med.index.astype(float), med.values, 1)[0]
    >>> slope, (lo, hi) = bootstrap_ci(d, slope_of, strata="Harvest.Year")

    Q5: tương quan Spearman giữa các quốc gia

    >>> from scipy.stats import spearmanr
    >>> rho, (lo, hi) = bootstrap_ci(
    ...     by_country, lambda s: spearmanr(s["production_share"], s["median_total_9"]).statistic)
    """
    q = _check_ci(ci)
    n = len(data)
    if n == 0:
        raise ValueError("data rỗng")
    if isinstance(strata, str):
        strata = data[strata]
    if strata is not None and len(strata) != n:
        raise ValueError("strata phải có cùng số dòng với data")

    is_pandas = isinstance(data, (pd.DataFrame, pd.Series))
    arr = data if is_pandas else np.asarray(data)
    take = (lambda rows: arr.iloc[rows]) if is_pandas else (lambda rows: arr[rows])

    idx = _resample_index(n, strata, n_boot, np.random.default_rng(seed))
    boot = np.array([stat_fn(take(rows)) for rows in idx], dtype=float)
    if np.isnan(boot).all():
        raise ValueError("stat_fn trả về NaN ở mọi lần bootstrap")
    return float(stat_fn(data)), np.nanpercentile(boot, q)
