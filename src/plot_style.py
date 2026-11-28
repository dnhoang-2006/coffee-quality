"""Style chung cho hình xuất slide và notebook 04.

Chỉ dùng cho hình trên slide và trong ``notebooks/04_summary.ipynb``; không áp
dụng lại cho các biểu đồ trong các notebook 02 đã merge.

Cách dùng::

    from src.plot_style import apply_style
    apply_style()
    fig, ax = plt.subplots()
    ...
    fig.savefig("q3_forest.png", dpi=200)
"""

import matplotlib.pyplot as plt


def apply_style():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.figsize": (10, 5.6), "font.size": 13, "axes.titlesize": 15,
                         "axes.labelsize": 13, "savefig.dpi": 200, "savefig.bbox": "tight"})
