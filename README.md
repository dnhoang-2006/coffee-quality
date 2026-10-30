# Coffee Quality Analysis — CSC17104 Final Project

## Team
| MSSV | Họ tên | Vai trò |
|---|---|---|
| 24120053 | Ngọc Hoàng | Nhóm trưởng |
| 23120361 | Đức Thịnh | Thành viên|
| 23120311 | Tùng Hiếu | Thành viên|

## Task breakdown
| Thành viên | Câu hỏi phụ trách | Công việc chính |
|---|---|---|
| Ngọc Hoàng (24120053) | Q1, Q2 (ML) | Dựng repo & môi trường, Data collection (3.1), README, mô hình ML, slide mở đầu |
| Đức Thịnh (23120361) | Q3, Q4 | Exploration: cột số, outlier, missing (3.2); Summary & reflection (3.5) |
| Tùng Hiếu (23120311) | Q5, Q6 | Exploration: cột phân loại, quan hệ (3.2); dữ liệu ngoài (FAOSTAT); slides.pdf, LLM_USAGE, kiểm tra tái lập |

## Dataset
- **Tên:** Coffee Quality with Locations of Origin
- **Nguồn:** https://www.kaggle.com/datasets/adampq/coffee-quality-with-locations-of-origin (tác giả RealDealAdamP), dữ liệu gốc scrape từ cơ sở dữ liệu của Coffee Quality Institute (CQI).
- **License:** CC BY-SA 4.0 (phải ghi nguồn; sản phẩm phái sinh chia sẻ theo cùng giấy phép).
- **Mô tả:** 3 file CSV. File chính `Coffee_Qlty.csv` gồm 1.338 dòng × 22 cột; mỗi dòng là một lô cà phê được CQI chấm điểm (xuất xứ, giống, phương pháp sơ chế, 9 thuộc tính cảm quan, độ ẩm, số lỗi hạt). Năm thu hoạch 2009–2018.
- **Dữ liệu bổ sung:** sản lượng cà phê nhân xanh theo quốc gia–năm từ FAOSTAT (xem `data/external/README.md`).
- **Notebook công khai liên quan:** *(đang cập nhật, xem `docs/related_work.md`)*

## Questions
*(Cập nhật sau)*

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
