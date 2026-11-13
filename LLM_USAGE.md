## 05/11/2026 — Relationships

- Công cụ Codex hỗ trợ triển khai các cell Relationships theo câu trả lời của Thịnh, kiểm tra số đếm trên CSV và ghi báo cáo kiểm chứng.
- Các kết quả được kiểm tra bằng lượt chạy tuần tự 41 cell. Thành viên cần tự chạy lại trên kernel `coffee` và tự viết nhận xét dựa trên output.

## 06/11/2026 — Nhận xét EDA

- Codex hỗ trợ đọc output notebook đã lưu và viết nháp nhận xét cho Categorical columns và Relationships. Đã đối chiếu số đếm, mẫu số và hệ số với bảng, biểu đồ và dữ liệu nguồn. Thành viên rà lại và giải thích các nhận xét trước khi nộp.

## 08/11/2026 — Summary EDA

- Codex hỗ trợ soạn bản nháp Summary từ bảng và biểu đồ đã lưu. Nội dung tách số liệu quan sát, cách xử lý dự kiến và hướng phân tích. Thành viên rà lại mẫu số, cách diễn giải và các quyết định tiền xử lý trước khi nộp.

## 09/11/2026 — Audit phép nối CQI và FAOSTAT

- Codex hỗ trợ đối chiếu nhãn quốc gia, viết hàm nạp và nối dữ liệu, tạo các bảng kiểm tra khóa trong notebook. Các kiểm tra dùng CSV gốc và dữ liệu thử có khóa trùng hoặc thiếu. Thành viên rà lại ánh xạ `China` trước khi đưa các lô liên quan vào phân tích theo quốc gia.
- Codex hỗ trợ đối chiếu 16 lô `China` với cột `Region` trong bản CQI nguồn, kiểm tra hai bản xuất FAOSTAT và thêm bảng tỷ trọng theo quốc gia–năm. Bảng bằng chứng ghi lại mã lô và dòng nguồn để nhóm kiểm tra.
- Codex hỗ trợ lập bảng chất lượng và tỷ trọng trung bình theo quốc gia, kiểm tra số lô ở từng bước lọc và đối chiếu số quốc gia đạt ngưỡng 10 lô với thống kê sơ bộ.
- Codex hỗ trợ triển khai phân nhóm theo median tỷ trọng, chạy bootstrap theo quốc gia cho chênh lệch median và Spearman, rồi đối chiếu khoảng tin cậy với một phép tính riêng. Notebook có thêm lượt kiểm tra khi bỏ lô trùng `REC_ID = 742`.
- Codex hỗ trợ dựng scatter plot và biểu đồ CI, kiểm tra đầu ra và chuẩn bị câu hỏi tự kiểm để thành viên viết phần diễn giải kết quả.

## 10/11/2026 — Chọn mẫu và reshape cho Q6

- Codex hỗ trợ đối chiếu bản phân công với quyết định chung và đưa đề xuất về phạm vi năm, cột giữ khi melt và cách tổng hợp pivot. Thành viên chốt dùng tất cả năm, bảng dài bốn cột, median kèm số lô hợp lệ.
- Codex hỗ trợ tạo notebook, lập bảng số dòng và kiểm tra median với cách tổng hợp độc lập.
- Codex hỗ trợ triển khai z-score theo từng thuộc tính trên mẫu chung, lập bảng xếp hạng theo khoảng cách giữa các mean theo châu lục và dựng heatmap. Đã đối chiếu z-score với SciPy và kiểm tra hình hiển thị.
- Codex hỗ trợ kiểm tra khi bỏ ba thuộc tính sát trần và khi bỏ lô trùng 742. Notebook nêu giới hạn của phép so sánh bỏ cột do z-score được tính độc lập theo từng thuộc tính, đồng thời tính lại tham số chuẩn hóa trong lượt bỏ lô trùng.
- Codex hỗ trợ dựng line profile và bảng tra cứu các thuộc tính dẫn đầu, thêm gợi ý để thành viên tự đọc bằng chứng và viết phần Results.

## 13/11/2026 — Rà câu trả lời Q6

- Sau khi thành viên viết hai câu trả lời, Codex hỗ trợ đối chiếu số liệu, sửa tên thuộc tính và biên tập diễn đạt. Đã làm rõ đơn vị của z-score và giới hạn khi đánh giá độ bền bằng cách bỏ cột.
- Codex hỗ trợ rà đoạn kết quả bỏ lô trùng do thành viên viết và bổ sung nội dung về ứng dụng cupping cùng giới hạn của mẫu. Thành viên cần rà, điều chỉnh và giải thích nội dung trước khi nộp.
- Theo yêu cầu thành viên, Codex hỗ trợ dọn notebook Q6, bỏ nội dung giới hạn, ứng dụng, hướng dẫn và các bảng trung gian, rồi chạy lại phần thống kê và biểu đồ.
- Codex hỗ trợ gộp tám báo cáo tuần 2, giữ bằng chứng ánh xạ quốc gia và kết quả kiểm tra trong một file, cập nhật hướng dẫn FAOSTAT và chạy lại Q5, Q6 trong hai tiến trình độc lập của môi trường `coffee`.
- Codex hỗ trợ bổ sung lời giải thích trước từng code cell của Q5 và Q6 về đầu vào, mục đích, thao tác, đầu ra và cách đọc bảng, biểu đồ để người đọc theo được quy trình.
- Sau khi thành viên tự viết hai câu trả lời, Codex hỗ trợ rà số liệu, sửa cách đọc trục log₁₀ và biên tập cách trình bày dựa trên bảng kết quả đã lưu.
