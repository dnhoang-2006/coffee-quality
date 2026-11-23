# LLM_USAGE — Hỗ trợ kỹ thuật và xử lý dữ liệu

Phần ghi nhận này tập trung vào các yêu cầu về kỹ thuật, code, thống kê và kiểm tra dữ liệu. Mục Hỏi gì tóm tắt yêu cầu cùng các chi tiết kỹ thuật đã trao đổi trong quá trình thực hiện.

## 05/11/2026 — Relationships

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Triển khai Pearson, Spearman, crosstab châu lục–phương pháp sơ chế và median điểm theo quốc gia như thế nào? Kiểm tra phạm vi mẫu, giá trị thiếu, lô trùng và mẫu số của từng bảng ra sao?
- **Đã dùng / sửa thế nào:** Xây dựng các cell thống kê mối quan hệ, kiểm tra số lô và chạy tuần tự các cell để đối chiếu kết quả.

## 09/11/2026 — Q5 — Ánh xạ quốc gia và kiểm tra phép nối

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hoàn thiện `COUNTRY_MAP` và `load_fao()` với ba cột country_fao, year, production_t như thế nào? Kiểm tra khóa quốc gia–năm, left join many-to-one và audit để giữ nguyên số lô, phân biệt khóa không khớp với sản lượng thiếu ra sao?
- **Đã dùng / sửa thế nào:** Xây dựng hàm nạp dữ liệu và `merge_production()`, kiểm tra khóa duy nhất, phép nối many-to-one, số dòng trước và sau nối cùng các khóa không khớp.

## 09/11/2026 — Q5 — Phạm vi China và tổng sản lượng thế giới

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Đối chiếu 16 lô China với nguồn CQI để xác nhận China, mainland và giữ Taiwan riêng như thế nào? Kiểm tra bộ lọc, đơn vị, dữ liệu World 2010–2017 và ghép CSV ra sao để tránh tính trùng các vùng thành phần?
- **Đã dùng / sửa thế nào:** Đối chiếu 16 lô với bản CQI nguồn. Kiểm tra tám dòng World, ghép với 912 dòng ban đầu và dùng tổng thế giới cùng năm để tính tỷ trọng.

## 09/11/2026 — Q5 — Tổng hợp dữ liệu theo quốc gia

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Tổng hợp số lô, median `total_9` và tỷ trọng sản lượng trung bình theo quốc gia như thế nào? Tính tỷ trọng từng năm với trọng số năm bằng nhau, đồng thời kiểm tra điều kiện dữ liệu hợp lệ và ngưỡng tối thiểu 10 lô ra sao?
- **Đã dùng / sửa thế nào:** Tính tỷ trọng ở cấp quốc gia–năm để mỗi năm có cùng trọng số. Lọc theo ngưỡng 10 lô và kiểm tra mẫu cuối có 18 quốc gia/vùng.

## 09/11/2026 — Q5 — Phân nhóm quy mô và bootstrap CI 95%

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Chia nhóm theo median tỷ trọng và tính bootstrap CI 95% cho chênh lệch median nhỏ − lớn cùng Spearman như thế nào? Lấy mẫu lại ở cấp quốc gia, độc lập theo nhóm hoặc giữ cặp tỷ trọng–điểm, với 5.000 lượt, seed cố định và kiểm tra lượt Spearman không xác định ra sao?
- **Đã dùng / sửa thế nào:** Tái sử dụng `bootstrap_diff` và `bootstrap_ci` trong `src/stats.py`, lấy mẫu lại ở cấp quốc gia với 5.000 lượt và seed cố định. Đối chiếu CI bằng phép tính riêng.

## 09–10/11/2026 — Kiểm tra cặp lô trùng

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Xác nhận cặp 721–742 trùng nhau ngoài REC_ID và tính lại số lô, median, ngưỡng 10 lô cùng hai CI sau khi bỏ 742 như thế nào? Giữ nguyên tỷ trọng FAOSTAT và ngưỡng chia nhóm để so sánh với mẫu chính ra sao?
- **Đã dùng / sửa thế nào:** Tính lại số lô và các thống kê sau khi bỏ 742, đối chiếu với mẫu chính để kiểm tra mức thay đổi.

## 10/11/2026 — Q6 — Chọn mẫu, melt và pivot_table

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Chọn Arabica ở bốn châu lục, giữ tất cả năm và loại các bản ghi ngoài phạm vi như thế nào? Melt chín thuộc tính với REC_ID, Continent.of.Origin, kiểm tra shape và tạo pivot_table median Châu lục × Thuộc tính ra sao?
- **Đã dùng / sửa thế nào:** Chốt mẫu dùng tất cả năm, bảng dài bốn cột và pivot median. Kiểm tra 1.308 lô tạo 11.772 dòng sau melt, đối chiếu median bằng groupby.

## 10/11/2026 — Q6 — Z-score và xếp hạng thuộc tính

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Chuẩn hóa từng thuộc tính bằng broadcasting với mean và độ lệch chuẩn chung, ddof=1 như thế nào? Từ mean z-score theo châu lục, tính spread max − min và xếp hạng ra sao để xử lý đồng hạng, tránh sai lệch do làm tròn?
- **Đã dùng / sửa thế nào:** Chuẩn hóa từng thuộc tính trên mẫu chung với ddof=1. Tính mean z-score theo châu lục và spread, đối chiếu z-score với SciPy.

## 10/11/2026 — Q6 — Kiểm tra độ bền

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Kiểm tra tỷ lệ sát trần và thay đổi spread, thứ hạng khi bỏ Uniformity, Clean.Cup, Sweetness như thế nào? Khi bỏ lô 742, tính lại tham số z-score và so sánh với mẫu chính ra sao?
- **Đã dùng / sửa thế nào:** So sánh spread và hạng với chín hoặc sáu thuộc tính. Tính lại tham số chuẩn hóa sau khi bỏ 742 và lập bảng thay đổi.

## 10/11/2026 — Trực quan hóa dữ liệu

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Vẽ scatter plot sản lượng trên thang log10 với median điểm, số lô và nhóm quy mô như thế nào? Biểu diễn CI 95% của chênh lệch điểm, heatmap và line profile mean z-score ra sao để có trục, thang màu và chú giải phù hợp?
- **Đã dùng / sửa thế nào:** Dùng Matplotlib và Seaborn, kiểm tra dữ liệu trục, đơn vị, màu và chú giải. Lưu output sau khi chạy notebook.

## 15/11/2026 — Đồng bộ code và kiểm tra môi trường

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Cập nhật import `add_total_score` từ `src.features` sau khi đồng bộ main như thế nào? Kiểm tra kernel coffee và chạy lại hai notebook từ đầu ra sao để xác nhận đủ output, biểu đồ và phát hiện lỗi phụ thuộc phiên chạy?
- **Đã dùng / sửa thế nào:** Cập nhật import add_total_score từ `src.features`, kiểm tra metadata kernel và chạy lại từ đầu để phát hiện lỗi tương thích.

