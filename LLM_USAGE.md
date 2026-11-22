## 05/11/2026 — Relationships

- Công cụ Codex hỗ trợ triển khai các cell Relationships theo câu trả lời của Thịnh, kiểm tra số đếm trên CSV và ghi báo cáo kiểm chứng.
- Các kết quả được kiểm tra bằng lượt chạy tuần tự 41 cell. Thành viên cần tự chạy lại trên kernel `coffee` và tự viết nhận xét dựa trên output.

## 06/11/2026 — Nhận xét EDA

- Codex hỗ trợ đọc output notebook đã lưu và viết nháp nhận xét cho Categorical columns và Relationships. Đã đối chiếu số đếm, mẫu số và hệ số với bảng, biểu đồ và dữ liệu nguồn. Thành viên rà lại và giải thích các nhận xét trước khi nộp.

## 08/11/2026 — Summary EDA

- Codex hỗ trợ soạn bản nháp Summary từ bảng và biểu đồ đã lưu. Nội dung tách số liệu quan sát, cách xử lý dự kiến và hướng phân tích. Thành viên rà lại mẫu số, cách diễn giải và các quyết định tiền xử lý trước khi nộp.

## 09/11/2026 — Q5 — Ánh xạ quốc gia và kiểm tra phép nối

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Hoàn thiện `COUNTRY_MAP` và `load_fao()`, giữ đúng cột yêu cầu, kiểm tra phép nối CQI–FAOSTAT.
- **Đã dùng / sửa thế nào:** Xây dựng hàm nạp dữ liệu và `merge_production()`, kiểm tra khóa duy nhất, phép nối many-to-one, số dòng trước và sau nối cùng các khóa không khớp.

## 09/11/2026 — Q5 — Phạm vi China và tổng sản lượng thế giới

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Xác nhận phạm vi nhãn China và kiểm tra dữ liệu tổng sản lượng thế giới vừa tải.
- **Đã dùng / sửa thế nào:** Đối chiếu 16 lô với bản CQI nguồn. Kiểm tra tám dòng World, ghép với 912 dòng ban đầu và dùng tổng thế giới cùng năm để tính tỷ trọng.

## 09/11/2026 — Q5 — Tổng hợp dữ liệu theo quốc gia

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Tổng hợp mỗi quốc gia một dòng, tính median `total_9` và trung bình tỷ trọng trong 2010–2017.
- **Đã dùng / sửa thế nào:** Tính tỷ trọng ở cấp quốc gia–năm để mỗi năm có cùng trọng số. Lọc theo ngưỡng 10 lô và kiểm tra mẫu cuối có 18 quốc gia/vùng.

## 09/11/2026 — Q5 — Phân nhóm quy mô và bootstrap CI 95%

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Chia nhóm quy mô và tính CI 95% cho chênh lệch median cùng Spearman.
- **Đã dùng / sửa thế nào:** Tái sử dụng `bootstrap_diff` và `bootstrap_ci` trong `src/stats.py`, lấy mẫu lại ở cấp quốc gia với 5.000 lượt và seed cố định. Đối chiếu CI bằng phép tính riêng.

## 09–10/11/2026 — Kiểm tra cặp lô trùng

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Kiểm tra độ nhạy của thống kê khi bỏ một lô trong cặp 721 và 742.
- **Đã dùng / sửa thế nào:** Tính lại số lô và các thống kê sau khi bỏ 742, đối chiếu với mẫu chính để kiểm tra mức thay đổi.

## 10/11/2026 — Q6 — Chọn mẫu, melt và pivot_table

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Tạo mẫu Q6, thực hiện melt chín thuộc tính và pivot_table theo châu lục.
- **Đã dùng / sửa thế nào:** Chốt mẫu dùng tất cả năm, bảng dài bốn cột và pivot median. Kiểm tra 1.308 lô tạo 11.772 dòng sau melt, đối chiếu median bằng groupby.

## 10/11/2026 — Q6 — Z-score và xếp hạng thuộc tính

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Tính z-score và xếp hạng thuộc tính theo độ chênh giữa bốn châu lục.
- **Đã dùng / sửa thế nào:** Chuẩn hóa từng thuộc tính trên mẫu chung với ddof=1. Tính mean z-score theo châu lục và spread, đối chiếu z-score với SciPy.

## 10/11/2026 — Q6 — Kiểm tra độ bền

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Kiểm tra độ bền khi bỏ ba thuộc tính sát trần và khi bỏ lô trùng 742.
- **Đã dùng / sửa thế nào:** So sánh spread và hạng với chín hoặc sáu thuộc tính. Tính lại tham số chuẩn hóa sau khi bỏ 742 và lập bảng thay đổi.

## 10/11/2026 — Trực quan hóa dữ liệu

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Dựng scatter plot, biểu đồ CI, heatmap và line profile từ các bảng thống kê.
- **Đã dùng / sửa thế nào:** Dùng Matplotlib và Seaborn, kiểm tra dữ liệu trục, đơn vị, màu và chú giải. Lưu output sau khi chạy notebook.

## 15/11/2026 — Đồng bộ code và kiểm tra môi trường

- **Người dùng:** Tùng Hiếu
- **Công cụ:** Codex
- **Hỏi gì:** Đồng bộ với main mới nhất và kiểm tra lại hai notebook bằng kernel coffee.
- **Đã dùng / sửa thế nào:** Cập nhật import add_total_score từ `src.features`, kiểm tra metadata kernel và chạy lại từ đầu để phát hiện lỗi tương thích.

## 14–15/11/2026 — Tuần 2: Cleaning/Features & Phân tích Q3, Q4

- **Người dùng:** Đức Thịnh
- **Công cụ:** Antigravity
- **Hỏi gì:** Hỗ trợ tách `src/cleaning.py` và `src/features.py`, triển khai biến dẫn xuất D3 (`add_defect_total`, `bin_moisture`), định lượng bất định D5 (`bootstrap_diff`, `kruskal`), kiểm tra độ bền D6 (`Moisture = 0`, `1,5×IQR` vs `3×IQR`) cho Q3 (`notebooks/02_analysis_q3.ipynb`), và phân tích xu hướng 2012–2017 kèm kiểm soát cơ cấu quốc gia D4 và bootstrap CI độ dốc D5 cho Q4 (`notebooks/02_analysis_q4.ipynb`).
- **Đã dùng / sửa thế nào:** Dùng cấu trúc code và bảng tổng hợp do AI đề xuất, bổ sung `%matplotlib inline` theo review để hiển thị đầy đủ biểu đồ trong notebook, tách riêng p-value Kruskal–Wallis khỏi bảng so sánh từng cặp ở Q3, tự đối chiếu lại toàn bộ số liệu đầu ra bằng cách chạy `Restart & Run All` trên kernel `coffee`, và tự rà soát phần diễn giải kết quả (bao gồm lý giải nhóm `<10%` và độ nhạy với `Moisture = 0`).

## 01–08/11/2026 — Notebook 01, mục 3.1 Data collection

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude
- **Hỏi gì:** Dựng khung notebook 3.1 theo cấu trúc homework/lab; code đọc dữ liệu, MD5, bảng nhóm cột, bảng quần thể/giai đoạn/độ phủ; góp ý nội dung Subject, License, Collection method; kiểm tra tài liệu tham khảo.
- **Đã dùng / sửa thế nào:** Dùng khung và code gợi ý, tự chạy lại và đối chiếu số liệu với dữ liệu; tự chọn và viết lại các kết luận; sửa số lô 1.338 → 1.339 sau khi kiểm tra REC_ID.

## 22/11/2026 — Sửa notebook 01 theo review

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude (review đối chiếu đề, Notion, lab), Claude Code (thực hiện)
- **Hỏi gì:** Rà notebook 01 theo đề và checklist Notion; sửa lỗi số liệu, bỏ nội dung lặp, bổ sung đường xu hướng scatter, thống nhất hình thức.
- **Đã dùng / sửa thế nào:** Claude Code sửa lỗi sự thật, bỏ nội dung lặp, thêm đường xu hướng scatter và sửa các con số trong nhận xét cho khớp output; câu chữ nhận xét của thành viên giữ nguyên. Đổi imputer cột phân loại ở 03_ml_question.ipynb sang "unknown" cho khớp kế hoạch EDA. Ngọc Hoàng duyệt bảng thay đổi trước khi push.
