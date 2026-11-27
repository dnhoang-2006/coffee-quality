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

## 25/11/2026 — Thiết kế lại phần đầu notebook

- **Người dùng:** Ngọc Hoàng
- **Công cụ:** Claude Code
- **Hỏi gì:** Thiết kế lại phần đầu của `01_collection_exploration.ipynb`, `02_analysis_q1.ipynb` và `03_ml_question.ipynb` theo một khuôn chung: thông tin trường/môn và bảng phân công (notebook 01); người phụ trách, loại câu hỏi, tiêu chí, cột dữ liệu sử dụng và câu hỏi nghiên cứu (Q1, Q2).
- **Đã dùng / sửa thế nào:** Dùng khung HTML/CSS do Claude Code đề xuất; tự điền và kiểm tra nội dung câu hỏi, tiêu chí, cột dữ liệu theo `docs/questions.md`; chạy lại Restart & Run All để kiểm tra notebook hiển thị đúng trước khi push.

## 27/11/2026 — Notebook 04, style hình và hình cho slide Q3, Q4

- **Người dùng:** Đức Thịnh
- **Công cụ:** Claude Code
- **Hỏi gì:** Tạo `src/plot_style.py` theo cấu hình nhóm đã chốt; dựng `04_summary.ipynb` (Key findings, Limitations, Future work, khung Individual reflection); xuất hình forest plot D6 (Q3) và biểu đồ trước–sau kiểm soát (Q4) cho slide.
- **Đã dùng / sửa thế nào:** Claude Code viết nháp toàn bộ chữ của Key findings, Limitations, Future work và chọn insight bất ngờ nhất (Q1); mọi con số được chép từ output đã lưu của các notebook 02, 03 trên `main` (Q2 lấy từ bảng test 24/11), và ô `# TEST` kiểm tra mỗi ước lượng nằm trong CI. Phần reflection chỉ có khung trống, không viết hộ ai. Hình slide được tính lại bằng cùng code và seed như notebook, có `assert` đối chiếu với bảng D6 và bảng độ dốc. Chạy Restart & Run All trên kernel `coffee`.
