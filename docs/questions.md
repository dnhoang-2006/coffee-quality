# Câu hỏi nghiên cứu

**Phạm vi chung cho cả 6 câu:** chỉ phân tích Arabica; bỏ bản ghi giữ chỗ `REC_ID = 1310`; coi `Moisture = 0` là giá trị thiếu; `total_9` = tổng 9 thuộc tính cảm quan; ngày chấm ≈ `Expiration − 1 năm`.

---

## Q1 — Phương pháp sơ chế và chất lượng · Ngọc Hoàng · D3, D4, D5

**Câu hỏi:** Trong cùng một châu lục, các lô sơ chế khô (*Natural / Dry*) có `total_9` cao hơn các lô sơ chế ướt (*Washed / Wet*) không, chênh lệch bao nhiêu điểm (CI 95%), và chênh lệch thô trên toàn mẫu có đổi chiều sau khi kiểm soát châu lục không?

- **Motivation:** nông hộ và hợp tác xã cân nhắc chuyển quy trình sơ chế (sơ chế khô tốn ít nước hơn) cần biết việc chuyển đổi có làm giảm điểm chất lượng không.
- **Phạm vi:** các lô có đủ châu lục và phương pháp sơ chế; chỉ giữ 2 phương pháp trên; chỉ giữ châu lục có ≥ 20 lô mỗi nhóm.
- **Bằng chứng:** D3 `total_9` (có biện luận) · D4 bảng chênh lệch thô vs chênh lệch trong từng châu lục · D5 bootstrap CI 95% + Cohen's d.

## Q2 — Dự đoán điểm chất lượng trước khi cupping (ML) · Ngọc Hoàng

**Câu hỏi:** Khi nhận mẫu cà phê nhân xanh, chỉ dựa trên thông tin có sẵn **trước khi cupping** (xuất xứ, giống, phương pháp sơ chế, màu hạt, độ ẩm, số lỗi hạt, năm thu hoạch), mô hình dự đoán `total_9` sai lệch trung bình bao nhiêu điểm, có tốt hơn đáng kể so với việc chỉ đoán điểm trung bình không, và thông tin nào giúp dự đoán nhiều nhất?

- **Motivation:** nhà nhập khẩu nhận nhiều mẫu nhưng cupping tốn thời gian và chi phí; điểm dự đoán giúp **ưu tiên lô nào gửi đi chấm trước** và ước lượng sơ bộ chất lượng khi đàm phán.
- **Bài toán:** hồi quy, biến mục tiêu `total_9`.
- **Cột bị loại (rò rỉ dữ liệu):** 9 thuộc tính cảm quan (cộng lại chính là `total_9`), `total_9`, `Expiration` (chỉ dùng để chia dữ liệu), `REC_ID`.
- **Chia dữ liệu theo thời gian:** train = các lô chấm trước 2016 (≈ 1.063 lô), test = các lô chấm từ 2016 (≈ 275 lô); cross-validation bằng `TimeSeriesSplit` chỉ trên train.
- **Mô hình:** baseline `DummyRegressor(strategy="mean")` · `Ridge` (tuyến tính, dễ diễn giải) · `RandomForestRegressor` (bắt quan hệ phi tuyến). Mọi bước tiền xử lý nằm trong `Pipeline`.
- **Metric:** **MAE** (đơn vị: điểm) làm metric chính vì dễ hiểu với người dùng ("sai trung bình X điểm"); báo kèm RMSE để xem các lô bị đoán sai nhiều.
- **Phân tích lỗi & diễn giải:** sai số theo châu lục/quốc gia và theo khoảng điểm (lô điểm rất cao/thấp); `permutation_importance` trên tập test.

## Q3 — Độ ẩm, lỗi hạt và chất lượng · Đức Thịnh · D3, D5, D6

**Câu hỏi:** Các lô có độ ẩm trong khoảng khuyến nghị **10–12%** và **không có lỗi hạt loại 1** có `total_9` cao hơn các lô còn lại bao nhiêu điểm (CI 95%), và kết luận có giữ nguyên khi (a) giữ hay bỏ các lô `Moisture = 0`, (b) đổi ngưỡng outlier từ 1,5×IQR sang 3×IQR không?

- **Motivation:** khâu phơi/sấy và bảo quản cần biết việc đưa độ ẩm về đúng khoảng và loại bỏ hạt lỗi có đáng đầu tư không.
- **Phạm vi:** các lô có độ ẩm dương (≈ 1.074 lô) cho phân tích chính; toàn mẫu chỉ dùng cho kiểm tra độ bền.
- **Bằng chứng:** D3 `moisture_band` (ngưỡng có trích nguồn) và `defects_total` · D5 bootstrap CI + Kruskal–Wallis · D6 bảng cùng một chỉ số kết luận dưới 3 lựa chọn làm sạch.

## Q4 — Xu hướng chất lượng theo năm thu hoạch · Đức Thịnh · D2, D4, D5

**Câu hỏi:** Trong giai đoạn thu hoạch **2012–2017**, điểm trung vị `total_9` tăng hay giảm bao nhiêu điểm mỗi năm (CI 95%), và xu hướng đó còn giữ không khi loại bỏ ảnh hưởng của việc cơ cấu quốc gia gửi mẫu thay đổi qua các năm?

- **Motivation:** nhà rang xay và người mua theo dõi chất lượng nguồn cung cần phân biệt "chất lượng thật sự thay đổi" với "chỉ là nước khác gửi mẫu nhiều hơn".
- **Phạm vi:** năm thu hoạch 2012–2017 (89–354 lô/năm); bỏ 2009–2011 và 2018 vì quá ít lô, bỏ lô thiếu năm — nêu rõ lý do và số dòng.
- **Bằng chứng:** D2 pivot Năm × Châu lục, `rolling(3)`, `pct_change()` · D4 xu hướng gộp vs xu hướng sau khi trừ median của từng quốc gia + bảng tỷ trọng quốc gia theo năm · **D5 bootstrap CI 95% cho độ dốc** (lấy mẫu lại các lô trong từng năm), cho cả phiên bản chưa và đã kiểm soát.
- **Lưu ý:** chỉ có 6 điểm thời gian, nên nếu CI của độ dốc chứa 0 thì kết luận "không đủ bằng chứng có xu hướng".

## Q5 — Quy mô sản xuất quốc gia và chất lượng · Tùng Hiếu · D1, D3, D5

**Câu hỏi:** Ở **mức quốc gia**, các nước sản xuất cà phê quy mô nhỏ có điểm chất lượng trung vị cao hơn hay thấp hơn các nước quy mô lớn, và mức liên hệ giữa tỷ trọng sản lượng thế giới với điểm chất lượng là bao nhiêu (CI 95%)?

- **Motivation:** nhà rang xay tìm nguồn cà phê đặc sản muốn biết có nên tìm tới các nước sản xuất nhỏ thay vì chỉ mua từ các nước lớn không.
- **Đơn vị phân tích:** mỗi quốc gia là một quan sát: median `total_9` của các lô thuộc nước đó, số lô, và tỷ trọng sản lượng trung bình giai đoạn 2010–2017. Chỉ giữ quốc gia có đủ số lô tối thiểu (ngưỡng thống nhất, ví dụ ≥ 5 lô) và báo rõ số quốc gia bị loại.
- **Bằng chứng:** D1 nối CQI với FAOSTAT theo (quốc gia, năm) rồi tổng hợp theo quốc gia — báo số dòng trước/sau, các quốc gia không khớp tên và lý do chọn `how='left'` · D3 `production_share` và nhóm quy mô theo ngưỡng có biện luận · D5 bootstrap trên các quốc gia: CI 95% cho chênh lệch median giữa nhóm nhỏ và lớn, và cho hệ số tương quan Spearman.
- **Lưu ý:** chỉ còn khoảng 20–30 quốc gia sau khi lọc, nên CI sẽ rộng; trình bày kèm số lô của từng nước.

## Q6 — Hồ sơ hương vị theo châu lục · Tùng Hiếu · D2, D3, D6

**Câu hỏi:** Bốn châu lục (Bắc Mỹ, Nam Mỹ, châu Á, châu Phi) có hồ sơ hương vị khác nhau không — thuộc tính nào tạo khác biệt lớn nhất giữa các châu lục, và xếp hạng đó có giữ nguyên khi bỏ 3 thuộc tính "trần điểm" (Uniformity, Clean.Cup, Sweetness) không?

- **Motivation:** barista và nhà rang xay phối trộn (blend) cần biết nên lấy nguồn từ châu lục nào để có độ chua, độ đậm hay hương vị mong muốn.
- **Phạm vi:** 4 châu lục trên; bỏ Oceania (1 lô) và lô thiếu châu lục.
- **Bằng chứng:** D2 `melt` 9 thuộc tính rồi `pivot_table` Châu lục × Thuộc tính · D3 z-score (có biện luận vì sao chuẩn hoá) · D6 so xếp hạng khi dùng 9 thuộc tính vs 6 thuộc tính.

---
