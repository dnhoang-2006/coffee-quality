## 05/11/2026 — Relationships

- Công cụ Codex hỗ trợ triển khai các cell Relationships theo câu trả lời của Thịnh, kiểm tra số đếm trên CSV và ghi báo cáo kiểm chứng.
- Các kết quả được kiểm tra bằng lượt chạy tuần tự 41 cell. Thành viên cần tự chạy lại trên kernel `coffee` và tự viết nhận xét dựa trên output.

## 06/11/2026 — Nhận xét EDA

- Codex hỗ trợ đọc output notebook đã lưu và viết nháp nhận xét cho Categorical columns và Relationships. Đã đối chiếu số đếm, mẫu số và hệ số với bảng, biểu đồ và dữ liệu nguồn. Thành viên rà lại và giải thích các nhận xét trước khi nộp.

## 08/11/2026 — Summary EDA

- Codex hỗ trợ soạn bản nháp Summary từ bảng và biểu đồ đã lưu. Nội dung tách số liệu quan sát, cách xử lý dự kiến và hướng phân tích. Thành viên rà lại mẫu số, cách diễn giải và các quyết định tiền xử lý trước khi nộp.

## Tuần 2 — Q5 và Q6

| Ngày | Người dùng | Công cụ | Nội dung yêu cầu | Cách dùng và chỉnh sửa |
| --- | --- | --- | --- | --- |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Đọc bản phân công, hoàn thiện ánh xạ CQI–FAOSTAT và kiểm tra phép nối. | Dùng hỗ trợ viết `load_fao()`, `merge_production()`, bảng số dòng và khóa chưa khớp. Đối chiếu CSV gốc và kiểm tra khóa many-to-one. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Xác nhận phạm vi nhãn China và dùng tổng sản lượng thế giới. | Đối chiếu 16 lô với bản CQI nguồn, dùng dòng World từ CSV thành viên tải. Ghép thành một CSV FAOSTAT cục bộ và ghi nguồn, bộ lọc. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Tổng hợp theo quốc gia, chia nhóm quy mô và tính hai CI 95%. | Dùng hỗ trợ triển khai bảng mỗi vùng một dòng, trung bình tỷ trọng theo năm và bootstrap ở cấp quốc gia. Tái sử dụng hàm của nhóm và kiểm tra mẫu cuối 18 vùng. |
| 10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Tạo Q6, đề xuất chọn mẫu, melt, pivot và tính z-score. | Thành viên chọn tất cả năm, bảng dài bốn cột và pivot median. Dùng hỗ trợ code, bảng kiểm tra và heatmap theo các lựa chọn đã chốt. |
| 10–13/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Kiểm tra độ bền, dựng profile và giải thích cách đọc thống kê. | Dùng hỗ trợ phép bỏ ba cột và lô trùng, dựng biểu đồ, giải thích z-score, spread và CI. Các bảng và output được chạy để đối chiếu. |
| 13/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Rà câu trả lời đã viết, thống nhất form và giải thích quy trình trước code. | Thành viên viết và chỉnh câu trả lời, Codex hỗ trợ mẫu diễn giải, biên tập số liệu, bổ sung một số đoạn và lời dẫn. Một số đoạn ứng dụng và giới hạn được thêm rồi bỏ theo yêu cầu của thành viên. |
| 15/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Sửa theo review, khôi phục log và bổ sung phép D6 có thể đổi kết quả. | Khôi phục file và phân công trong README, so mean với median z-score, sửa import theo main mới, chọn kernel coffee và chạy lại hai notebook. Thứ hạng dẫn đầu đổi khi đổi cách tổng hợp. |

Codex đã hỗ trợ viết và biên tập cả code lẫn một số nội dung diễn giải. Thành viên cần tự kiểm tra, chỉnh lại câu chữ theo cách hiểu của mình và giải thích được các bước trong buổi Q&A. File log từng bị xóa theo yêu cầu dọn repo ngày 13/11 và được khôi phục khi xử lý review ngày 15/11.
