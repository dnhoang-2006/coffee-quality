# LLM_USAGE — Hỗ trợ kỹ thuật và xử lý dữ liệu

Phần ghi nhận này tập trung vào các yêu cầu về kỹ thuật, code, thống kê và kiểm tra dữ liệu. Nội dung prompt được tóm tắt theo mục đích sử dụng.

| Ngày | Người dùng | Công cụ | Nội dung prompt | Cách sử dụng và kiểm tra |
| --- | --- | --- | --- | --- |
| 05/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Triển khai Relationships theo quy tắc dữ liệu đã thống nhất, kiểm tra các bảng và biểu đồ trên CSV. | Xây dựng các cell thống kê mối quan hệ, kiểm tra số lô và chạy tuần tự các cell để đối chiếu kết quả. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Hoàn thiện COUNTRY_MAP và load_fao(), giữ đúng cột yêu cầu, kiểm tra phép nối CQI–FAOSTAT. | Xây dựng hàm nạp dữ liệu và merge_production(), kiểm tra khóa duy nhất, phép nối many-to-one, số dòng trước và sau nối cùng các khóa không khớp. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Xác nhận phạm vi nhãn China và kiểm tra dữ liệu tổng sản lượng thế giới vừa tải. | Đối chiếu 16 lô với bản CQI nguồn. Kiểm tra tám dòng World, ghép với 912 dòng ban đầu và dùng tổng thế giới cùng năm để tính tỷ trọng. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Tổng hợp mỗi quốc gia một dòng, tính median total_9 và trung bình tỷ trọng trong 2010–2017. | Tính tỷ trọng ở cấp quốc gia–năm để mỗi năm có cùng trọng số. Lọc theo ngưỡng 10 lô và kiểm tra mẫu cuối có 18 quốc gia/vùng. |
| 09/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Chia nhóm quy mô và tính CI 95% cho chênh lệch median cùng Spearman. | Tái sử dụng bootstrap_diff và bootstrap_ci trong src/stats.py, lấy mẫu lại ở cấp quốc gia với 5.000 lượt và seed cố định. Đối chiếu CI bằng phép tính riêng. |
| 09–10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Kiểm tra độ nhạy của thống kê khi bỏ một lô trong cặp 721 và 742. | Tính lại số lô và các thống kê sau khi bỏ 742, đối chiếu với mẫu chính để kiểm tra mức thay đổi. |
| 10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Tạo mẫu Q6, thực hiện melt chín thuộc tính và pivot_table theo châu lục. | Chốt mẫu dùng tất cả năm, bảng dài bốn cột và pivot median. Kiểm tra 1.308 lô tạo 11.772 dòng sau melt, đối chiếu median bằng groupby. |
| 10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Tính z-score và xếp hạng thuộc tính theo độ chênh giữa bốn châu lục. | Chuẩn hóa từng thuộc tính trên mẫu chung với ddof=1. Tính mean z-score theo châu lục và spread, đối chiếu z-score với SciPy. |
| 10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Kiểm tra độ bền khi bỏ ba thuộc tính sát trần và khi bỏ lô trùng 742. | So sánh spread và hạng với chín hoặc sáu thuộc tính. Tính lại tham số chuẩn hóa sau khi bỏ 742 và lập bảng thay đổi. |
| 10/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Dựng scatter plot, biểu đồ CI, heatmap và line profile từ các bảng thống kê. | Dùng Matplotlib và Seaborn, kiểm tra dữ liệu trục, đơn vị, màu và chú giải. Lưu output sau khi chạy notebook. |
| 15/11/2026 | Nguyễn Mai Tùng Hiếu | Codex | Đồng bộ với main mới nhất và kiểm tra lại hai notebook bằng kernel coffee. | Cập nhật import add_total_score từ src.features, kiểm tra metadata kernel và chạy lại từ đầu để phát hiện lỗi tương thích. |
