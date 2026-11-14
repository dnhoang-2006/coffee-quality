# Coffee Quality Analysis — CSC17104 Final Project

## Team
| MSSV | Họ tên | Vai trò |
|---|---|---|
| 24120053 | Đặng Ngọc Hoàng | Nhóm trưởng |
| 23120361 | Đào Đức Thịnh | Thành viên|
| 24120311 | Nguyễn Mai Tùng Hiếu | Thành viên|

## Task breakdown
| Thành viên | Câu hỏi phụ trách | Công việc chính |
|---|---|---|
| Ngọc Hoàng (24120053) | Q1, Q2 (ML) | Dựng repo & môi trường, Data collection (3.1), README, mô hình ML, slide mở đầu |
| Đức Thịnh (23120361) | Q3, Q4 | Exploration: cột số, outlier, missing (3.2); Summary & reflection (3.5) |
| Tùng Hiếu (24120311) | Q5, Q6 | Exploration: cột phân loại, quan hệ (3.2); dữ liệu ngoài (FAOSTAT); slides.pdf, kiểm tra tái lập |

## Dataset
- **Tên:** Coffee Quality with Locations of Origin
- **Nguồn:** https://www.kaggle.com/datasets/adampq/coffee-quality-with-locations-of-origin (tác giả RealDealAdamP, `adampq`).
- **Phiên bản:** Version 1 (*Initial release*), công bố 31/03/2024, chưa cập nhật lần nào. Nhóm tải về ngày 01/11/2026.
- **License:** CC BY-SA 4.0 (phải ghi nguồn; sản phẩm phái sinh chia sẻ theo cùng giấy phép).
- **Mô tả:** 3 file CSV. File chính `Coffee_Qlty.csv` gồm 1.339 dòng × 22 cột (`REC_ID` chạy từ 0 đến 1338); mỗi dòng là một lô cà phê được CQI chấm điểm (xuất xứ, giống, phương pháp sơ chế, 9 thuộc tính cảm quan, độ ẩm, số lỗi hạt). Năm thu hoạch 2009–2018. Hai file `By_Country` / `By_Continent` là bảng tổng hợp tính từ file chính.
- **Dữ liệu bổ sung:** sản lượng cà phê nhân xanh theo quốc gia–năm từ FAOSTAT (xem `data/external/README.md`).
- **Notebook công khai liên quan:** xem bảng *Related public notebooks* bên dưới.

**Provenance:** dữ liệu được scrape bằng script Python từ cơ sở dữ liệu công khai của Coffee Quality Institute (https://database.coffeeinstitute.org) và qua nhiều nguồn trung gian trước khi tới bản nhóm dùng:

| Thời gian | Nguồn | Nội dung | Giấy phép |
|:---|:---|:---|:---|
| 01/2018 | GitHub `jldbc/coffee-quality-database` (J. LeDoux) | Script scrape website CQI, khoảng 1.340 lô (Arabica + Robusta) | MIT (cho mã nguồn) |
| 12/2019 | Kaggle `volpatto/coffee-quality-database-from-cqi` | Đưa bộ dữ liệu trên lên Kaggle | ODbL |
| 05/2023 | Kaggle `fatihb/coffee-quality-data-cqi` | Sửa script cho website mới, scrape lại, chỉ lấy Arabica | "Other" (không nêu cụ thể) |
| 31/03/2024 | Kaggle `adampq/coffee-quality-with-locations-of-origin` | Tổng hợp, chỉnh sửa từ các bộ trên: **bản nhóm dùng** | CC BY-SA 4.0 |

Dữ liệu gốc của CQI không có điều khoản tái sử dụng công khai, nên nhóm chỉ dùng cho mục đích học tập và không phát hành lại dữ liệu gốc.

### Related public notebooks
Trang Kaggle của dataset có 7 notebook công khai. Phân tích chi tiết từng notebook nằm trong `docs/related_work.md`.

| # | Notebook (tác giả) | Nội dung chính |
|:---:|:---|:---|
| 1 | [Final](https://www.kaggle.com/code/joshuatyrell/final/notebook) (Joshua Tyrell) | So sánh `Flavor` theo sơ chế, xuất xứ, lỗi hạt; Linear Regression dự đoán `Flavor`, chia train/test ngẫu nhiên 70/30 |
| 2 | [Coffee quality report](https://www.kaggle.com/code/beshoyashraf/coffee-quality-report) (Beshoy Qulta) | Mean `Sweetness`, `Aroma` và khoảng cách thu hoạch–hết hạn theo quốc gia, tách riêng Arabica / Robusta |
| 3 | [Coffee Quality - Explorations](https://www.kaggle.com/code/docxian/coffee-quality-explorations) (Chris X.) | EDA tổng quát: giá trị thiếu, phân phối, tương quan Pearson và Phi_K |
| 4 | [Clustering of coffee quality](https://www.kaggle.com/code/arkabarua173/clustering-of-coffee-quality-k-means-pca) (Arka Barua) | PCA (3 thành phần) + K-means (6 cụm) trên các biến số |
| 5 | [project](https://www.kaggle.com/code/vivek193/project) (Vivek Yadav) | Dự đoán `Balance`, `Sweetness` từ các điểm cảm quan khác; phân loại loài, màu, xuất xứ |
| 6 | [Py \| EDA - Data dispersion](https://www.kaggle.com/code/mlippo/py-eda-data-dispersion) (mlippo) | Phân phối và mean các thuộc tính cảm quan theo giống và phương pháp sơ chế |
| 7 | [Processing Methods by Country and Continent](https://www.kaggle.com/code/adampq/processing-methods-by-country-and-continent) (RealDealAdamP) | Scatter plot cho biết phương pháp sơ chế nào xuất hiện ở quốc gia / châu lục nào |

**Câu hỏi của nhóm khác ở đâu:**
- **Biến chất lượng:** các notebook trên phân tích từng điểm cảm quan riêng lẻ (`Flavor`, `Aroma`, `Sweetness`…); nhóm dùng biến tổng hợp `total_9`.
- **Dữ liệu ngoài (Q5):** không notebook nào nối thêm nguồn ngoài; nhóm nối sản lượng FAOSTAT theo quốc gia–năm.
- **So sánh có kiểm soát và độ bền (Q1, Q3, Q4, Q6):** các notebook dừng ở mean / median mô tả theo nhóm; nhóm so sánh trong cùng châu lục, kiểm soát cơ cấu quốc gia theo năm, báo CI 95% bằng bootstrap và kiểm tra kết luận khi đổi cách làm sạch.
- **ML (Q2):** *Final* chia ngẫu nhiên và dự đoán một thuộc tính; *project* dùng các điểm cảm quan khác làm đầu vào và fit tiền xử lý trên toàn bộ dữ liệu. Nhóm chỉ dùng thông tin có **trước khi cupping**, chia train/test **theo thời gian**, và đặt mọi bước tiền xử lý trong `Pipeline`.

**Kiểm tra dữ liệu (MD5):** sau khi tải dữ liệu, chạy mục 3.1.2 trong `notebooks/01_collection_exploration.ipynb` và so sánh với bảng dưới. Cả 3 mã trùng khớp nghĩa là dữ liệu giống hệt bản nhóm đã dùng.

| File | Kích thước (KB) | MD5 |
|:---|---:|:---|
| `Coffee_Qlty.csv` | 166.6 | `183955d1a03c9d7447cf658e9cff0f45` |
| `Coffee_Qlty_By_Continent.csv` | 1.3 | `b5befb87b0d98c8b75d3263afa86fc91` |
| `Coffee_Qlty_By_Country.csv` | 5.5 | `625485a31a724517d132cfc4741e3f4f` |

## Questions

| # | Phụ trách | Câu hỏi | Tiêu chí |
|:---|:---|:---|:---|
| Q1 | Ngọc Hoàng | Trong cùng châu lục, sơ chế khô vs ướt chênh bao nhiêu điểm (CI 95%)? | D3, D4, D5 |
| Q2 | Ngọc Hoàng | **ML (hồi quy):** dự đoán `total_9` từ thông tin có trước khi cupping, sai trung bình bao nhiêu điểm? | ML |
| Q3 | Đức Thịnh | Độ ẩm 10–12% và không lỗi loại 1 cao hơn bao nhiêu điểm; có bền khi đổi cách làm sạch? | D3, D5, D6 |
| Q4 | Đức Thịnh | Xu hướng điểm 2012–2017 (CI cho độ dốc) có còn sau khi kiểm soát cơ cấu quốc gia? | D2, D4, D5 |
| Q5 | Tùng Hiếu | Ở mức quốc gia, nước sản xuất nhỏ vs lớn có điểm khác nhau không (nối FAOSTAT)? | D1, D3, D5 |
| Q6 | Tùng Hiếu | Hồ sơ hương vị 4 châu lục; xếp hạng có bền khi bỏ 3 cột trần điểm? | D2, D3, D6 |

## Key findings
*(Cập nhật sau)*

## How to run
### 1. Yêu cầu
- Miniconda hoặc Anaconda, Git.
- Khuyến nghị chạy trên Linux/WSL Ubuntu (như tài liệu giảng viên thực hành cung cấp). 

### 2. Clone repo
```bash
git clone https://github.com/dnhoang-2006/coffee-quality.git
cd coffee-quality
```

### 3. Tạo môi trường conda (giống nhau cho cả nhóm)
```bash
conda env create -f environment.yml
conda activate coffee
python -m ipykernel install --user --name coffee --display-name "Python (coffee)"
```
Kiểm tra phiên bản. Kết quả phải là numpy 1.26, pandas 2.1, scipy 1.17, scikit-learn 1.9:
```bash
python -c "import numpy, pandas, scipy, sklearn; print(numpy.__version__, pandas.__version__, scipy.__version__, sklearn.__version__)"
```

### 4. Tải dữ liệu
Theo yêu cầu của đề, file dữ liệu không đưa vào repo; mỗi người tự tải theo các bước dưới đây.
1. Tải zip tại https://www.kaggle.com/datasets/adampq/coffee-quality-with-locations-of-origin (cần đăng nhập Kaggle).
2. Giải nén vào `data/raw/`:
   ```bash
   unzip <đường-dẫn-tới-file-zip> -d data/raw/
   ls data/raw/
   ```
3. `data/raw/` phải có đúng 3 file: `Coffee_Qlty.csv`, `Coffee_Qlty_By_Continent.csv`, `Coffee_Qlty_By_Country.csv`.
4. Tải dữ liệu FAOSTAT tại https://www.fao.org/faostat/en/#data/QCL theo bộ lọc trong `data/external/README.md`. Cần số liệu quốc gia/vùng lãnh thổ cho 2008–2018 và tám dòng `World` cho 2010–2017. Ghép các dòng dữ liệu vào một CSV cùng cấu trúc, chỉ giữ một dòng tiêu đề và đặt tên `data/external/FAOSTAT_coffee.csv`. Bản nhóm dùng có 920 dòng dữ liệu.

### 5. Chạy notebook
```bash
jupyter lab
```
Chọn kernel **Python (coffee)** và chạy theo thứ tự:
1. `notebooks/01_collection_exploration.ipynb`
2. `notebooks/02_analysis_q1.ipynb` → `02_analysis_q6.ipynb`
3. `notebooks/03_ml_question.ipynb`

### 6. Khi environment.yml thay đổi
Nếu có người thêm thư viện mới vào `environment.yml`, sau khi `git pull` cả nhóm chạy:
```bash
conda env update -f environment.yml --prune
```

## Quy ước làm việc
- Mỗi người làm trên branch riêng `feat/<tên-việc>`, merge vào `main` qua Pull Request; nhóm trưởng review.
- Không push thẳng lên `main`.
- `git config user.email` phải trùng email tài khoản GitHub (để commit được tính cho đúng người).
- Không tự `conda install` thêm thư viện: báo nhóm trưởng để cập nhật `environment.yml`.
- Đường dẫn trong code luôn lấy từ `src/config.py`, không viết đường dẫn tuyệt đối.

Quy trình mỗi lần làm việc:
```bash
git checkout main && git pull
git checkout -b feat/<tên-việc>
# ... làm việc, Restart & Run All notebook ...
git add <file> && git commit -m "<mô tả ngắn>"
git push -u origin feat/<tên-việc>
# lên GitHub bấm "Compare & pull request"
```
