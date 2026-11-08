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
| Tùng Hiếu (24120311) | Q5, Q6 | Exploration: cột phân loại, quan hệ (3.2); dữ liệu ngoài (FAOSTAT); slides.pdf, LLM_USAGE, kiểm tra tái lập |

## Dataset
- **Tên:** Coffee Quality with Locations of Origin
- **Nguồn:** https://www.kaggle.com/datasets/adampq/coffee-quality-with-locations-of-origin (tác giả RealDealAdamP, `adampq`).
- **Phiên bản:** Version 1 (*Initial release*), công bố 31/03/2024, chưa cập nhật lần nào. Nhóm tải về ngày 01/11/2026.
- **License:** CC BY-SA 4.0 (phải ghi nguồn; sản phẩm phái sinh chia sẻ theo cùng giấy phép).
- **Mô tả:** 3 file CSV. File chính `Coffee_Qlty.csv` gồm 1.339 dòng × 22 cột (`REC_ID` chạy từ 0 đến 1338); mỗi dòng là một lô cà phê được CQI chấm điểm (xuất xứ, giống, phương pháp sơ chế, 9 thuộc tính cảm quan, độ ẩm, số lỗi hạt). Năm thu hoạch 2009–2018. Hai file `By_Country` / `By_Continent` là bảng tổng hợp tính từ file chính.
- **Dữ liệu bổ sung:** sản lượng cà phê nhân xanh theo quốc gia–năm từ FAOSTAT (xem `data/external/README.md`).
- **Notebook công khai liên quan:** *(đang cập nhật, xem `docs/related_work.md`)*

**Provenance:** dữ liệu được scrape bằng script Python từ cơ sở dữ liệu công khai của Coffee Quality Institute (https://database.coffeeinstitute.org) và qua nhiều nguồn trung gian trước khi tới bản nhóm dùng:

| Thời gian | Nguồn | Nội dung | Giấy phép |
|:---|:---|:---|:---|
| 01/2018 | GitHub `jldbc/coffee-quality-database` (J. LeDoux) | Script scrape website CQI, khoảng 1.340 lô (Arabica + Robusta) | MIT (cho mã nguồn) |
| 12/2019 | Kaggle `volpatto/coffee-quality-database-from-cqi` | Đưa bộ dữ liệu trên lên Kaggle | ODbL |
| 05/2023 | Kaggle `fatihb/coffee-quality-data-cqi` | Sửa script cho website mới, scrape lại, chỉ lấy Arabica | "Other" (không nêu cụ thể) |
| 31/03/2024 | Kaggle `adampq/coffee-quality-with-locations-of-origin` | Tổng hợp, chỉnh sửa từ các bộ trên: **bản nhóm dùng** | CC BY-SA 4.0 |

Dữ liệu gốc của CQI không có điều khoản tái sử dụng công khai, nên nhóm chỉ dùng cho mục đích học tập và không phát hành lại dữ liệu gốc.

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
Dữ liệu không được commit lên repo (file lớn, license CC BY-SA 4.0).
1. Tải zip tại https://www.kaggle.com/datasets/adampq/coffee-quality-with-locations-of-origin (cần đăng nhập Kaggle).
2. Giải nén vào `data/raw/`:
   ```bash
   unzip <đường-dẫn-tới-file-zip> -d data/raw/
   ls data/raw/
   ```
3. `data/raw/` phải có đúng 3 file: `Coffee_Qlty.csv`, `Coffee_Qlty_By_Continent.csv`, `Coffee_Qlty_By_Country.csv`.
4. Tải dữ liệu FAOSTAT tại https://www.fao.org/faostat/en/#data/QCL, chọn bộ lọc theo `data/external/README.md` (Item: Coffee, green · Element: Production · Years: 2008–2018), rồi lưu file CSV thành `data/external/FAOSTAT_coffee.csv`.

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
