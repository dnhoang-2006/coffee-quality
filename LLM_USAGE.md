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
