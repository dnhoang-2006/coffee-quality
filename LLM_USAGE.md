# LLM_USAGE — Hỗ trợ kỹ thuật và xử lý dữ liệu

## Tuần 1 — Khảo sát categorical columns và chuẩn hóa nhãn

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy thống kê số nhãn, số lô và tỷ lệ của các cột phân loại, phân biệt tỷ lệ trên toàn mẫu với tỷ lệ trên các lô có nhãn. Chuẩn hóa chữ hoa/thường, khoảng trắng và alias; gộp nhóm dưới 20 lô và so sánh ngưỡng 10–30 lô cho tôi. Giữ riêng giá trị thiếu, nhãn `None` và tên quốc gia chưa gộp để nối FAOSTAT.
- **Đã dùng / sửa thế nào:** Triển khai các bảng tần suất và tỷ lệ, dùng `normalize_labels` và `group_rare` để chuẩn hóa, gộp nhóm hiếm và so sánh theo ngưỡng. Giữ dữ liệu gốc, phân biệt giá trị thiếu với nhãn có sẵn và dùng tên quốc gia chưa gộp khi nối dữ liệu ngoài.

## 01–08/11/2026 — Notebook 01, mục 3.1 Data collection

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude
- **Hỏi gì:** Dựng khung notebook 3.1 theo cấu trúc homework/lab; code đọc dữ liệu, MD5, bảng nhóm cột, bảng quần thể/giai đoạn/độ phủ; góp ý nội dung Subject, License, Collection method; kiểm tra tài liệu tham khảo.
- **Đã dùng / sửa thế nào:** Dùng khung và code gợi ý, tự chạy lại và đối chiếu số liệu với dữ liệu; tự chọn và viết lại các kết luận; sửa số lô 1.338 → 1.339 sau khi kiểm tra REC_ID.

## 05/11/2026 — Relationships

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy tính Pearson và Spearman giữa các biến cảm quan, biến vật lý và `total_9`, rồi trực quan hóa bằng heatmap cho tôi. Lập thêm crosstab châu lục–phương pháp sơ chế và bảng median điểm theo quốc gia. Ghi rõ số lô hợp lệ, cách xử lý giá trị thiếu và mẫu số khi tính tỷ lệ.
- **Đã dùng / sửa thế nào:** Xây dựng các cell thống kê mối quan hệ, kiểm tra số lô và chạy tuần tự các cell để đối chiếu kết quả.

## 09/11/2026 — Q5 — Ánh xạ quốc gia và kiểm tra phép nối

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy hoàn thiện `COUNTRY_MAP` từ danh sách quốc gia CQI và cho `load_fao()` trả về ba cột `country_fao`, `year`, `production_t`, với sản lượng tính bằng tấn. Kiểm tra khóa quốc gia–năm duy nhất trước khi left join many-to-one. Lập bảng audit số dòng trước–sau nối, tách khóa không khớp với khóa khớp nhưng thiếu sản lượng cho tôi.
- **Đã dùng / sửa thế nào:** Xây dựng hàm nạp dữ liệu và `merge_production()`, kiểm tra khóa duy nhất, phép nối many-to-one, số dòng trước và sau nối cùng các khóa không khớp.

## 09/11/2026 — Q5 — Phạm vi China và tổng sản lượng thế giới

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy đối chiếu địa danh của 16 lô `China` trong bản CQI nguồn để xác nhận ánh xạ `China, mainland`, giữ `Taiwan` thành một chuỗi riêng. Kiểm tra dữ liệu `World` 2010–2017 có đúng một tổng sản lượng dương cho mỗi năm và cùng đơn vị tấn. Dùng tổng thế giới trực tiếp, tránh cộng trùng vùng tổng hợp với quốc gia thành phần.
- **Đã dùng / sửa thế nào:** Đối chiếu 16 lô với bản CQI nguồn. Kiểm tra tám dòng World, ghép với 912 dòng ban đầu và dùng tổng thế giới cùng năm để tính tỷ trọng.

## 09/11/2026 — Q5 — Tổng hợp dữ liệu theo quốc gia

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy chọn các lô Arabica hợp lệ trong 2010–2017, tổng hợp số lô và median `total_9` theo quốc gia cho tôi. Tính tỷ trọng bằng sản lượng quốc gia chia tổng `World` cùng năm, rồi lấy trung bình với trọng số năm bằng nhau để không phụ thuộc số lô CQI. Chỉ giữ quốc gia có ít nhất 10 lô hợp lệ và hiển thị bảng mẫu cuối.
- **Đã dùng / sửa thế nào:** Tính tỷ trọng ở cấp quốc gia–năm để mỗi năm có cùng trọng số. Lọc theo ngưỡng 10 lô và kiểm tra mẫu cuối có 18 quốc gia/vùng.

## 09/11/2026 — Q5 — Phân nhóm quy mô và bootstrap CI 95%

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy chia nhóm Nhỏ và Lớn theo median tỷ trọng sản lượng, rồi tính chênh lệch median điểm cấp quốc gia Nhỏ − Lớn và Spearman giữa tỷ trọng với median điểm. Dùng 5.000 lượt bootstrap có hoàn lại ở cấp quốc gia, seed 42; lấy mẫu riêng từng nhóm và giữ cặp tỷ trọng–điểm khi tính Spearman. Xuất ước lượng cùng CI 95% theo phân vị 2,5% và 97,5%.
- **Đã dùng / sửa thế nào:** Tái sử dụng `bootstrap_diff` và `bootstrap_ci` trong `src/stats.py`, lấy mẫu lại ở cấp quốc gia với 5.000 lượt và seed cố định. Đối chiếu CI bằng phép tính riêng.

## 09–10/11/2026 — Kiểm tra cặp lô trùng

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy đối chiếu toàn bộ cột ngoài `REC_ID` để xác nhận cặp 721–742 trùng nhau. Bỏ lô 742, tính lại số lô, median theo quốc gia và kiểm tra điều kiện tối thiểu 10 lô. Giữ nguyên tỷ trọng FAOSTAT và ngưỡng chia nhóm, rồi so sánh hai ước lượng cùng CI của Q5 với mẫu chính cho tôi.
- **Đã dùng / sửa thế nào:** Tính lại số lô và các thống kê sau khi bỏ 742, đối chiếu với mẫu chính để kiểm tra mức thay đổi.

## 10/11/2026 — Q6 — Chọn mẫu, melt và pivot_table

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy chọn Arabica ở North America, South America, Asia và Africa, bỏ lô 1310 nhưng giữ tất cả năm, kể cả lô thiếu năm. Melt chín thuộc tính thành bốn cột `REC_ID`, `Continent.of.Origin`, `attribute`, `score` cho tôi. Hiển thị shape trước–sau, kiểm tra mỗi lô tạo chín dòng và lập pivot_table median cùng bảng số lô có điểm hợp lệ.
- **Đã dùng / sửa thế nào:** Chốt mẫu dùng tất cả năm, bảng dài bốn cột và pivot median. Kiểm tra 1.308 lô tạo 11.772 dòng sau melt, đối chiếu median bằng groupby.

## 10/11/2026 — Q6 — Z-score và xếp hạng thuộc tính

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy tính z-score từng thuộc tính bằng mean và độ lệch chuẩn mẫu chung của bốn châu lục, dùng `ddof=1`, không chuẩn hóa riêng trong từng châu lục. Tạo bảng mean z-score Châu lục × Thuộc tính, tính spread bằng max − min của bốn mean và xếp hạng giảm dần. Giữ độ chính xác khi tính, chỉ làm tròn lúc hiển thị và xử lý đồng hạng cho tôi.
- **Đã dùng / sửa thế nào:** Chuẩn hóa từng thuộc tính trên mẫu chung với ddof=1. Tính mean z-score theo châu lục và spread, đối chiếu z-score với SciPy.

## 10/11/2026 — Q6 — Kiểm tra độ bền

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy thống kê tỷ lệ đạt 10 điểm ở `Uniformity`, `Clean.Cup`, `Sweetness`, rồi so sánh spread và thứ hạng khi bỏ ba thuộc tính này. Kiểm tra riêng trường hợp bỏ lô trùng 742 bằng cách tính lại mean, độ lệch chuẩn và hồ sơ z-score. Xuất bảng thay đổi spread, thứ hạng so với mẫu chính cho tôi.
- **Đã dùng / sửa thế nào:** So sánh spread và hạng với chín hoặc sáu thuộc tính. Tính lại tham số chuẩn hóa sau khi bỏ 742 và lập bảng thay đổi.

## 10/11/2026 — Trực quan hóa dữ liệu

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy vẽ scatter plot với trục x là log10 sản lượng trung bình, trục y là median `total_9`, màu phân biệt nhóm quy mô và kích thước điểm thể hiện số lô CQI. Vẽ thêm ước lượng chênh lệch median cùng CI 95% và đường tham chiếu 0. Với Q6, tạo heatmap và line profile từ cùng bảng mean z-score, thống nhất thứ tự thuộc tính và màu châu lục.
- **Đã dùng / sửa thế nào:** Dùng Matplotlib và Seaborn, kiểm tra dữ liệu trục, đơn vị, màu và chú giải. Lưu output sau khi chạy notebook.

## 14–15/11/2026 — Tuần 2: Cleaning/Features & Phân tích Q3, Q4

- **Người dùng:** Đức Thịnh
- **Công cụ:** Antigravity
- **Hỏi gì:** Hỗ trợ tách `src/cleaning.py` và `src/features.py`, triển khai biến dẫn xuất D3 (`add_defect_total`, `bin_moisture`), định lượng bất định D5 (`bootstrap_diff`, `kruskal`), kiểm tra độ bền D6 (`Moisture = 0`, `1,5×IQR` vs `3×IQR`) cho Q3 (`notebooks/02_analysis_q3.ipynb`), và phân tích xu hướng 2012–2017 kèm kiểm soát cơ cấu quốc gia D4 và bootstrap CI độ dốc D5 cho Q4 (`notebooks/02_analysis_q4.ipynb`).
- **Đã dùng / sửa thế nào:** Dùng cấu trúc code và bảng tổng hợp do AI đề xuất, bổ sung `%matplotlib inline` theo review để hiển thị đầy đủ biểu đồ trong notebook, tách riêng p-value Kruskal–Wallis khỏi bảng so sánh từng cặp ở Q3, tự đối chiếu lại toàn bộ số liệu đầu ra bằng cách chạy `Restart & Run All` trên kernel `coffee`, và tự rà soát phần diễn giải kết quả (bao gồm lý giải nhóm `<10%` và độ nhạy với `Moisture = 0`).

## 15/11/2026 — Đồng bộ code và kiểm tra môi trường

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy kiểm tra đường dẫn import sau khi đồng bộ main và chuyển `add_total_score` sang `src.features` đúng cấu trúc hiện tại. Xác nhận metadata kernel `coffee`, restart rồi chạy Q5–Q6 từ đầu để phát hiện biến chưa khởi tạo hoặc lỗi phụ thuộc thứ tự cell. Kiểm tra các bảng, biểu đồ và output lỗi sau lượt chạy cho tôi.
- **Đã dùng / sửa thế nào:** Cập nhật import add_total_score từ `src.features`, kiểm tra metadata kernel và chạy lại từ đầu để phát hiện lỗi tương thích.

## 22/11/2026 — Sửa notebook 01 theo review

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude (review đối chiếu đề, Notion, lab), Claude Code (thực hiện)
- **Hỏi gì:** Rà notebook 01 theo đề và checklist Notion; sửa lỗi số liệu, bỏ nội dung lặp, bổ sung đường xu hướng scatter, thống nhất hình thức.
- **Đã dùng / sửa thế nào:** Claude Code sửa lỗi sự thật, bỏ nội dung lặp, thêm đường xu hướng scatter và sửa các con số trong nhận xét cho khớp output; câu chữ nhận xét của thành viên giữ nguyên. Đổi imputer cột phân loại ở 03_ml_question.ipynb sang "unknown" cho khớp kế hoạch EDA. Ngọc Hoàng duyệt bảng thay đổi trước khi push.

## Tuần 2–3 — Q6 — Đối chiếu mean và median z-score

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy giữ nguyên mẫu và tham số z-score, thay mean bằng median khi tổng hợp theo châu lục, rồi tính lại spread và thứ hạng. Lập bảng so sánh hai cách, chỉ rõ thuộc tính đổi hạng và các trường hợp đồng hạng cho tôi. Kiểm tra median điểm gốc của ba thuộc tính sát trần để xác định vì sao spread median bằng 0, khác với phép chỉ bỏ ba cột.
- **Đã dùng / sửa thế nào:** Bổ sung bảng đối chiếu spread, hạng và thay đổi hạng giữa mean và median z-score. Dùng cùng mẫu và cùng tham số chuẩn hóa để so sánh; kiểm tra median điểm gốc của ba thuộc tính sát trần và xác định phép bỏ cột không làm thay đổi spread của sáu thuộc tính còn lại.

## 24/11/2026 — Q1 — Viết nhận xét kết quả

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude
- **Hỏi gì:** Góp ý bản nháp các ô nhận xét của `02_analysis_q1.ipynb`: so sánh thô và có kiểm soát châu lục, CI bootstrap và Cohen's d, trả lời Q1, ý nghĩa thực tế, điều bất ngờ, hạn chế.
- **Đã dùng / sửa thế nào:** Tự viết nhận xét từ bảng và biểu đồ đã lưu; dùng góp ý về cách diễn đạt (tách "không đủ bằng chứng" khỏi "không khác", không đọc ước lượng sau kiểm soát là "natural vẫn cao hơn"). Mọi con số được đối chiếu lại với output notebook.

## 24/11/2026 — Q2 — Viết nhận xét mô hình ML

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude
- **Hỏi gì:** Góp ý bản nháp các ô nhận xét của `03_ml_question.ipynb`: bảng rò rỉ theo mốc T, lý do chọn metric, kết quả tinh chỉnh trên CV, kết quả test so với baseline, phân tích lỗi và permutation importance.
- **Đã dùng / sửa thế nào:** Tự viết nhận xét từ output; dùng góp ý để tách kết luận với giả thuyết chưa kiểm chứng và nêu rõ khi CI chứa 0. Lựa chọn mô hình vẫn chỉ dựa trên CV, không đổi theo kết quả test.

## 24/11/2026 — Rà soát nhận xét Q1, Q2

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude
- **Hỏi gì:** Rà toàn bộ nhận xét Q1, Q2: kiểm tra các con số so với output và tìm chỗ lập luận chưa nhất quán.
- **Đã dùng / sửa thế nào:** Nhận được danh sách lỗi nội dung (REC_ID cần xếp vào rò rỉ target, lý giải sai vì sao CI sau kiểm soát rộng hơn ở Q1) và các chỉnh câu chữ nhỏ. Tự xem lại từng điểm trước khi sửa; ý "sơ chế khô tiết kiệm nước" bị bỏ vì chưa có nguồn trích dẫn.

## 25/11/2026 — Q5 — Trực quan hóa Spearman và CI 95%

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy lấy hệ số Spearman và hai cận bootstrap CI 95% trực tiếp từ bảng `effects`, không nhập tay số liệu. Vẽ điểm ước lượng cùng khoảng ngang, đặt trục từ −1 đến 1 và đường tham chiếu 0, hiển thị giá trị ở điểm và hai đầu khoảng. Giữ biểu đồ này riêng với chênh lệch median vì hai đại lượng khác đơn vị.
- **Đã dùng / sửa thế nào:** Thêm biểu đồ lấy trực tiếp từ `effects`, dùng trục hệ số từ −1 đến 1 và đường tham chiếu 0. Chạy lại toàn bộ notebook trên kernel coffee và dùng output mới cho slide.

## 25/11/2026 — Thiết kế lại phần đầu notebook

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude Code
- **Hỏi gì:** Thiết kế lại phần đầu của `01_collection_exploration.ipynb`, `02_analysis_q1.ipynb` và `03_ml_question.ipynb` theo một khuôn chung: thông tin trường/môn và bảng phân công (notebook 01); người phụ trách, loại câu hỏi, tiêu chí, cột dữ liệu sử dụng và câu hỏi nghiên cứu (Q1, Q2).
- **Đã dùng / sửa thế nào:** Dùng khung HTML/CSS do Claude Code đề xuất; tự điền và kiểm tra nội dung câu hỏi, tiêu chí, cột dữ liệu theo `docs/questions.md`; chạy lại Restart & Run All để kiểm tra notebook hiển thị đúng trước khi push.

## 26/11/2026 — Q5–Q6 — Kiểm tra nguồn dữ liệu và căn cứ phương pháp

- **Người dùng:** Tùng Hiếu.
- **Công cụ:** Codex
- **Hỏi gì:** Hãy kiểm tra nguồn dataset CQI, bộ lọc và đơn vị FAOSTAT, cùng file gốc dùng đối chiếu địa danh `China` trong Q5–Q6. Đối chiếu Spearman, bootstrap percentile và `ddof=1` với tài liệu chính thức có nội dung hỗ trợ trực tiếp. Phân biệt nguồn dữ liệu, tài liệu phương pháp và các hàm nhóm tự triển khai; giữ nguyên code và số liệu phân tích cho tôi.
- **Đã dùng / sửa thế nào:** Bổ sung liên kết dataset Kaggle, README FAOSTAT và file `arabica_data_cleaned.csv` dùng đối chiếu địa danh. Thêm tài liệu SciPy về Spearman, bootstrap percentile và pandas về độ lệch chuẩn mẫu. Ghi rõ CI dùng các hàm trong `src/stats.py`; chỉ cập nhật Markdown của Q5–Q6, kiểm tra cấu trúc notebook hợp lệ và giữ nguyên code cùng output đã lưu.
