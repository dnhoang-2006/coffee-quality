## 05/11/2026 — Relationships

- Công cụ Codex hỗ trợ triển khai các cell Relationships theo câu trả lời của Thịnh, kiểm tra số đếm trên CSV và ghi báo cáo kiểm chứng.
- Các kết quả được kiểm tra bằng lượt chạy tuần tự 41 cell. Thành viên cần tự chạy lại trên kernel `coffee` và tự viết nhận xét dựa trên output.

## 06/11/2026 — Nhận xét EDA

- Codex hỗ trợ đọc output notebook đã lưu và viết nháp nhận xét cho Categorical columns và Relationships. Đã đối chiếu số đếm, mẫu số và hệ số với bảng, biểu đồ và dữ liệu nguồn. Thành viên rà lại và giải thích các nhận xét trước khi nộp.

## 08/11/2026 — Summary EDA

- Codex hỗ trợ soạn bản nháp Summary từ bảng và biểu đồ đã lưu. Nội dung tách số liệu quan sát, cách xử lý dự kiến và hướng phân tích. Thành viên rà lại mẫu số, cách diễn giải và các quyết định tiền xử lý trước khi nộp.

## 14–15/11/2026 — Tuần 2: Cleaning/Features & Phân tích Q3, Q4

- **Người dùng:** Thịnh · **Công cụ:** Antigravity (AI Coding Assistant)
- **Hỏi gì:** Hỗ trợ tách `src/cleaning.py` và `src/features.py` (Bước 0), triển khai biến dẫn xuất D3 (`add_defect_total`, `bin_moisture`), định lượng bất định D5 (`bootstrap_diff`, `kruskal`), kiểm tra độ bền D6 (`Moisture = 0`, `1,5×IQR` vs `3×IQR`) cho Q3 (`notebooks/02_analysis_q3.ipynb`), và phân tích xu hướng 2012–2017 kèm kiểm soát cơ cấu quốc gia D4 và bootstrap CI độ dốc D5 cho Q4 (`notebooks/02_analysis_q4.ipynb`).
- **Đã dùng / sửa thế nào:** Dùng cấu trúc code và bảng tổng hợp do AI đề xuất, bổ sung `%matplotlib inline` theo review để hiển thị đầy đủ biểu đồ trong notebook, tách riêng p-value Kruskal–Wallis khỏi bảng so sánh từng cặp ở Q3, tự đối chiếu lại toàn bộ số liệu đầu ra bằng cách chạy `Restart & Run All` trên kernel `coffee`, và tự rà soát phần diễn giải kết quả (bao gồm lý giải nhóm `<10%` và độ nhạy với `Moisture = 0`).
