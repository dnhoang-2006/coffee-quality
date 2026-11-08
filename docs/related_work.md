# Related work
## 1. Final
### a. Thông tin notebook
- **Tác giả đăng:** Joshua Tyrell.
- **Link:** [Final trên Kaggle](https://www.kaggle.com/code/joshuatyrell/final/notebook).
  
### b. Câu hỏi nghiên cứu
Trong **Step 1**, Joshua Tyrell đặt câu hỏi về mối liên hệ giữa điểm `Flavor` và các đặc điểm của lô cà phê, gồm xuất xứ, phương pháp sơ chế, độ ẩm, lỗi hạt, năm thu hoạch và loài. Mục đích là giúp người mua cà phê hoặc người phụ trách chất lượng chọn những lô cần ưu tiên nếm thử hoặc kiểm tra thêm.

Các bảng, biểu đồ và mô hình ở **Step 3–5** triển khai câu hỏi chính theo ba hướng:
- **Sơ chế và xuất xứ:** Các lô sử dụng phương pháp sơ chế khác nhau có median `Flavor` chênh lệch ra sao? Khi nhóm theo châu lục hoặc quốc gia, mean `Flavor` cao hơn ở những nhóm nào trong mẫu?
- **Độ ẩm và lỗi hạt:** Mean `Flavor` thay đổi thế nào giữa các nhóm có ít và nhiều lỗi `Category.Two.Defects`? Các lô có `Moisture` cao hơn có xu hướng nhận điểm `Flavor` thấp hơn không?
- **Dự đoán trên các lô chưa thấy:** Khi đưa các đặc điểm của lô vào cùng một mô hình Linear Regression, sai số dự đoán `Flavor` giảm bao nhiêu so với cách dự đoán cùng một điểm trung bình cho mọi lô?

### c. Phương pháp phân tích
1. **Chuẩn bị dữ liệu:** Tác giả đọc `Coffee_Qlty.csv` và loại một lô có `Flavor = 0` vì cả chín điểm cảm quan của lô đều bằng 0. Các giá trị thiếu ở cột phân loại được chuyển thành `Unknown` để giữ lại lô trong dữ liệu, còn `Harvest.Year` thiếu được điền bằng median. Sau bước này, mẫu giảm từ 1.339 xuống 1.338 lô.
2. **So sánh `Flavor` giữa các nhóm:** Tác giả tính median `Flavor` theo `Processing.Method` và dùng các nhóm có ít nhất 10 lô. Với xuất xứ, tác giả tính mean `Flavor` theo châu lục và vẽ biểu đồ cho 10 quốc gia có mean cao nhất trong số những quốc gia có ít nhất 10 lô. Để xem mean `Flavor` thay đổi theo mức lỗi hạt ra sao, tác giả chia `Category.Two.Defects` thành bốn nhóm gồm 0, 1–3, 4–7 và từ 8 lỗi trở lên. Scatter plot `Moisture`–`Flavor` bổ sung góc nhìn ở cấp từng lô, cho thấy độ phân tán của điểm tại các mức độ ẩm.
3. **Kiểm tra khả năng dự đoán:** Tác giả mã hoá các biến phân loại bằng `pd.get_dummies`, sau đó chia ngẫu nhiên dữ liệu thành 70% train và 30% test. Mô hình Linear Regression dùng loài, châu lục, phương pháp sơ chế, năm thu hoạch, độ ẩm và lỗi hạt để dự đoán `Flavor`. Baseline lấy mean `Flavor` của tập train làm dự đoán cho mọi lô trong tập test. Tác giả báo RMSE trên tập test khoảng 0,292 cho mô hình và 0,312 cho baseline, tương ứng mức giảm khoảng 0,020 điểm `Flavor`.

### d. Đối chiếu với câu hỏi của nhóm
*Final* hỏi liệu các đặc điểm của từng lô, như phương pháp sơ chế, độ ẩm và lỗi hạt, có giúp dự đoán điểm `Flavor` của một lô mới hay không. Trong mô hình của tác giả, châu lục xuất xứ là một biến đầu vào cùng với các đặc điểm đó. Phân tích của nhóm dùng quốc gia và năm thu hoạch làm khóa để ghép sản lượng cà phê từ FAOSTAT, rồi xem mức sản lượng của quốc gia trong năm đó có liên hệ thế nào với `total_9` của các lô CQI. Vì vậy, hai câu hỏi khác nhau cả về mục tiêu lẫn biến được phân tích. *Final* đánh giá khả năng dự đoán một điểm cảm quan ở cấp lô, còn phân tích của nhóm tìm hiểu mối liên hệ giữa sản lượng ở cấp quốc gia–năm và tổng điểm của chín thuộc tính cảm quan.

## 2. Coffee quality report
### a. Thông tin notebook
- **Tác giả đăng:** Beshoy Qulta.
- **Link:** [Coffee quality report trên Kaggle](https://www.kaggle.com/code/beshoyashraf/coffee-quality-report).

### b. Câu hỏi nghiên cứu
Notebook không viết câu hỏi nghiên cứu thành một mục riêng. Dựa trên sáu biểu đồ, có thể diễn đạt mục tiêu phân tích theo hai hướng dưới đây. Mỗi phép so sánh được thực hiện riêng cho Arabica và Robusta.
- **Điểm cảm quan theo xuất xứ:** Trong từng loài, mean `Sweetness` và mean `Aroma` khác nhau thế nào giữa các quốc gia có lô trong mẫu sau làm sạch?
- **Khoảng cách giữa năm thu hoạch và năm hết hạn:** Trong từng loài, số năm chênh lệch trung bình giữa năm thu hoạch và năm hết hạn khác nhau thế nào giữa các quốc gia?

### c. Phương pháp phân tích

1. **Chuẩn bị dữ liệu:** Tác giả đọc `Coffee_Qlty.csv`, đổi tên cột sang `snake_case`, rồi loại các dòng thiếu ở bất kỳ cột nào bằng `dropna()` và loại dòng trùng hoàn toàn bằng `drop_duplicates()`. Các bảng và biểu đồ sau đó chỉ sử dụng những lô còn lại sau hai bước lọc này.
2. **Tạo biến thời gian và chia theo loài:** Tác giả lấy năm từ `expiration`, rồi tính `expiry_duration` bằng `expiry_year` trừ `harvest_year`. Đại lượng này đo chênh lệch giữa hai mốc ở độ phân giải năm. Sau đó, tác giả tách dữ liệu thành hai nhóm `Arabica` và `Robusta` để so sánh các quốc gia trong từng loài.
3. **So sánh theo quốc gia:** Với mỗi loài, tác giả dùng `groupby()` để tính mean `sweetness`, `aroma` và `expiry_duration` theo quốc gia, rồi vẽ một scatter plot cho mỗi biến. Khi đọc biểu đồ, cần kiểm tra thứ tự nhãn quốc gia. Code lấy nhãn trục ngang từ `unique()` nhưng lấy giá trị mean từ `groupby()`, nên nhãn và điểm có thể lệch nhau nếu hai danh sách khác thứ tự. Notebook cũng chưa ghi số lô bên cạnh từng giá trị mean.

### d. Đối chiếu với câu hỏi của nhóm
*Coffee quality report* dùng quốc gia để chia nhóm trong từng loài Arabica và Robusta. Các biểu đồ cho biết mean `Sweetness`, `Aroma` và chênh lệch giữa năm thu hoạch với năm hết hạn khác nhau ra sao giữa các quốc gia trong mẫu. Đối với phân tích của nhóm thì nhóm dùng quốc gia cùng năm thu hoạch để nối thêm sản lượng FAOSTAT, qua đó phân biệt được những năm có mức sản lượng khác nhau ngay trong cùng một nước. Thông tin này phục vụ câu hỏi về mối liên hệ giữa quy mô sản xuất theo quốc gia–năm và `total_9` của các lô CQI, trong khi các bảng của *Coffee quality report* mô tả từng chỉ số riêng theo quốc gia và loài.

## 3. ☕Coffee Quality - Explorations
### a. Thông tin notebook

- **Tác giả đăng:** Chris X.
- **Link:** [Coffee Quality - Explorations trên Kaggle](https://www.kaggle.com/code/docxian/coffee-quality-explorations).

### b. Câu hỏi nghiên cứu
Notebook trình bày một lượt EDA tổng quát. Dựa trên các mục **Import and First Glance**, **Basic EDA** và **Feature Correlation**, có thể diễn đạt các câu hỏi mà tác giả khám phá như sau:
- **Chất lượng và phân bố dữ liệu:** Những cột nào có giá trị thiếu? Các điểm cảm quan, độ ẩm và số lỗi hạt phân bố ra sao, và có lô nào mang giá trị bất thường? Mỗi loài, xuất xứ, năm thu hoạch và phương pháp sơ chế xuất hiện bao nhiêu lần trong mẫu?
- **Mối liên hệ giữa các biến:** Những cặp biến số nào thay đổi cùng nhau rõ nhất, chẳng hạn giữa hai thuộc tính cảm quan hoặc giữa số lỗi hạt và một điểm cảm quan? Khi xét thêm các biến phân loại như `Species` và `Processing.Method`, ma trận phi_K cho thấy những cặp nào có mức liên hệ nổi bật?

### c. Phương pháp phân tích
1. **Kiểm tra dữ liệu đầu vào:** Tác giả đọc `Coffee_Qlty.csv`, xem các dòng đầu, kiểu dữ liệu và thống kê mô tả. Ma trận `missingno` hiển thị vị trí các ô thiếu để quan sát những cột nào bị thiếu và các giá trị thiếu có xuất hiện trên cùng lô hay không.
2. **Khám phá từng biến:** Sau khi kiểm tra bản ghi có nhiều điểm bằng 0, tác giả giữ các dòng có `Aroma > 0`. Tác giả dùng histogram và boxplot cho các biến số để xem phân bố và giá trị ngoại lệ. Với biến phân loại, biểu đồ cột đếm cả giá trị thiếu. `Harvest.Year` được vẽ thêm theo thứ tự năm để xem số lô thay đổi theo thời gian.
3. **Khám phá quan hệ giữa các biến:** Tác giả dùng Pearson heatmap để xem chiều và độ mạnh của liên hệ tuyến tính giữa các biến số, rồi dùng pairplot để quan sát hình dạng của từng cặp. Sau đó, tác giả tính ma trận Phi_K trên cả biến số và biến phân loại để khảo sát các liên hệ có `Species`, xuất xứ hoặc `Processing.Method` tham gia.

### d. Đối chiếu với câu hỏi của nhóm
*Coffee Quality - Explorations* dùng xuất xứ như một biến trong ma trận liên hệ để xem quốc gia và châu lục đi cùng những đặc điểm nào của các lô CQI. Còn nhóm dùng quốc gia và năm thu hoạch làm khóa để ghép sản lượng từ FAOSTAT, qua đó bổ sung mức sản lượng ứng với từng quốc gia trong từng năm. Với thông tin đó, nhóm xem các lô ở những mức sản lượng khác nhau có chênh lệch về `total_9` hay không, trong khi notebook của Chris X khảo sát nhiều cặp biến và giữ các điểm cảm quan như `Aroma` và `Flavor` ở dạng từng cột riêng.

## 4. Clustering of coffee quality 🍵 | K-means | PCA
### a. Thông tin notebook

- **Tác giả đăng:** Arka Barua.
- **Link:** [Clustering of coffee quality trên Kaggle](https://www.kaggle.com/code/arkabarua173/clustering-of-coffee-quality-k-means-pca).

### b. Câu hỏi nghiên cứu
Tác giả đặt mục tiêu phân cụm các lô cà phê bằng PCA và K-means. Từ quy trình trong notebook, mục tiêu này có thể diễn đạt thành hai câu hỏi cụ thể:

- **Giảm số chiều:** Có thể dùng bao nhiêu thành phần PCA để biểu diễn các đặc điểm dạng số của lô cà phê mà vẫn giữ phần lớn phương sai trong dữ liệu đầu vào?
- **Phân cụm:** Khi biểu diễn mỗi lô bằng các thành phần PCA đã chọn, K-means chia các lô thành những cụm nào? Số cụm được chọn dựa trên mức giảm của WCSS khi tăng số cụm từ 1 đến 20.

### c. Phương pháp phân tích
1. **Chuẩn bị và khám phá dữ liệu:** Tác giả đọc `Coffee_Qlty.csv`, bỏ lô `REC_ID = 1197` vì thiếu nhiều thông tin, rồi bỏ cột ID trước khi loại dòng trùng. Tác giả trích `Expiration_year` từ `Expiration` và vẽ các biểu đồ mean theo quốc gia cho điểm cảm quan, độ ẩm và lỗi hạt.
2. **Biểu diễn dữ liệu bằng PCA:** Tác giả lấy các cột số, gồm điểm cảm quan, độ ẩm, lỗi hạt, `Harvest.Year` và `Expiration_year`, rồi điền giá trị thiếu bằng mean của từng cột. Code đưa các giá trị này vào PCA trực tiếp, nên mức độ đóng góp của từng biến phụ thuộc vào thang đo và phương sai của nó. Theo notebook, ba thành phần đầu giữ gần 93% phương sai của tập biến số được đưa vào PCA.
3. **Chọn và trực quan hoá các cụm:** Tác giả chạy K-means trên ba thành phần PCA, thử từ 1 đến 20 cụm và chọn 6 cụm dựa trên điểm gấp của đường WCSS. Cuối cùng, tác giả gắn nhãn cụm cho từng lô và dùng scatter plot 2D và 3D để xem các cụm phân bố thế nào trong không gian PCA.

### d. Đối chiếu với câu hỏi của nhóm
Notebook của Arka Barua dùng các biến số của từng lô để tìm những lô có đặc điểm giống nhau. Quốc gia được dùng để nhóm các biểu đồ EDA, còn phần K-means dựa trên các thành phần PCA tạo từ các cột số. Phân tích của nhóm dùng quốc gia cùng năm thu hoạch làm khóa để ghép sản lượng FAOSTAT. Sau khi ghép, nhóm xem sản lượng ở cấp quốc gia–năm liên hệ thế nào với `total_9` ở cấp lô. Vì vậy, đầu ra của notebook là nhãn cụm cho từng lô, còn phân tích của nhóm tập trung vào mối liên hệ giữa một biến sản lượng bổ sung và tổng điểm cảm quan.

## 5. project
### a. Thông tin notebook

- **Tác giả đăng:** Vivek Yadav.
- **Link:** [project trên Kaggle](https://www.kaggle.com/code/vivek193/project).

### b. Câu hỏi nghiên cứu
Notebook thử nhiều mô hình trên bốn dataset. Riêng phần `Coffee_Qlty.csv`, các câu hỏi dưới đây được suy ra từ biến đầu vào và biến đích mà tác giả chọn cho từng mô hình.
- **Dự đoán điểm cảm quan:** Có thể dùng các điểm cảm quan còn lại, độ ẩm và lỗi hạt để dự đoán `Balance` không? Một nhóm biến số gồm `Aroma`, `Flavor`, `Aftertaste`, `Acidity`, `Body`, `Uniformity` và `Moisture` dự đoán `Sweetness` tốt đến đâu qua cross-validation?
- **Dự đoán nhãn của lô:** Các biến số của lô có giúp nhận diện `Arabica`, xuất xứ `India` hoặc giống `Arusha` không? Riêng với màu hạt, tác giả kiểm tra liệu chỉ dùng `Aroma` và `Flavor` có thể phân biệt nhãn `Green` với các nhãn còn lại hay không.

### c. Phương pháp phân tích
1. **Tiền xử lý:** Tác giả dùng `ColumnTransformer` để áp dụng hai quy trình. Biến số được điền thiếu bằng median và chuẩn hoá bằng `StandardScaler`. Biến phân loại được điền bằng nhãn phổ biến nhất rồi chuyển thành các cột one-hot để dùng làm biến đích trong các bài toán nhận diện nhãn.
2. **Hồi quy điểm cảm quan:** Tác giả dùng Linear Regression để dự đoán `Balance` đã chuẩn hoá từ các biến số còn lại, dành 20% dữ liệu làm tập test và tính MAE, MSE, RMSE và R². Với `Sweetness`, tác giả dùng SVR, đánh giá bằng KFold 10 phần và thử tham số bằng GridSearchCV.
3. **Dự đoán nhãn:** Tác giả dùng Logistic Regression để nhận diện Arabica, SVC để nhận diện nhãn `Green` và Decision Tree Classifier để nhận diện xuất xứ India. Với SVC, tác giả vẽ ranh giới quyết định trên mặt phẳng `Aroma`–`Flavor` và thử tham số bằng GridSearchCV và RandomizedSearchCV. Tác giả còn dùng Decision Tree Regressor cho biến chỉ báo `Variety_Arusha`.
4. **Giới hạn khi đọc kết quả:** Code gọi `fit_transform()` trên toàn bộ bảng cà phê trước khi chia train và test. Do đó, các thống kê dùng để điền thiếu và chuẩn hoá đã lấy thông tin từ cả các lô sau này được dùng để đánh giá. Các điểm đánh giá cần được đọc với giới hạn đó.

### d. Đối chiếu với câu hỏi của nhóm
Phần cà phê trong *project* dùng các đặc điểm đã ghi của từng lô để dự đoán một điểm cảm quan hoặc một nhãn của chính lô đó. Chẳng hạn, xuất xứ India được mã hoá thành biến đích cho cây quyết định. Trong phân tích của nhóm, xuất xứ có vai trò khác: quốc gia kết hợp với năm thu hoạch tạo thành khóa để nối sản lượng FAOSTAT vào các lô CQI. Phép nối cho phép nhóm xem mức sản lượng theo quốc gia–năm liên hệ thế nào với `total_9`, còn các thí nghiệm của Vivek Yadav đánh giá khả năng dự đoán từ những biến sẵn có ở cấp lô.

## 6. Py | EDA - Data dispersion
### a. Thông tin notebook
- **Tác giả đăng:** mlippo.
- **Link:** [Py | EDA - Data dispersion trên Kaggle](https://www.kaggle.com/code/mlippo/py-eda-data-dispersion).

### b. Câu hỏi nghiên cứu
Tác giả muốn tìm hiểu các lô cà phê có điểm cảm quan cao nên qua các bảng và biểu đồ, mục tiêu này được triển khai theo hai hướng. Điểm `Aroma` và `Sweetness` phân bố thế nào giữa các giống và phương pháp sơ chế? Khi lấy mean của từng thuộc tính cảm quan, mức chênh lệch giữa các giống hoặc giữa các phương pháp sơ chế lớn đến đâu?

### c. Phương pháp phân tích
1. **Chọn mẫu:** Tác giả đọc `Coffee_Qlty.csv`, kiểm tra số ô thiếu rồi loại các lô thiếu `Variety` hoặc `Processing.Method`. Đây là hai nhãn dùng để chia nhóm trong các so sánh sau.
2. **Xem phân bố ở cấp lô:** Scatter plot đặt `Aroma` trên trục ngang và `Sweetness` trên trục dọc, dùng màu cho `Variety` và ký hiệu cho `Processing.Method`. Tác giả kiểm tra thêm phân bố `Sweetness` riêng ở giống Catuai sau khi thấy một điểm thấp.
3. **So sánh giữa các nhóm:** Tác giả tính mean từng thuộc tính cảm quan và `Moisture` theo giống và theo phương pháp sơ chế. Code tạo boxplot để xem độ phân tán của điểm từng lô và của mean theo giống, rồi vẽ biểu đồ đường để so sánh mean của chín thuộc tính giữa các giống. Nhận xét về phương pháp sơ chế dựa trên các mean mô tả, nên mức chênh lệch giữa các nhóm chưa cho biết tác động của sơ chế lên điểm.

### d. Đối chiếu với câu hỏi của nhóm
*Py | EDA - Data dispersion* dùng giống và phương pháp sơ chế để chia nhóm, rồi xem từng điểm cảm quan phân bố và chênh lệch ra sao giữa các nhóm. Phân tích của nhóm dùng quốc gia và năm thu hoạch để gắn cho mỗi lô mức sản lượng cà phê nhân xanh tương ứng từ FAOSTAT. Từ đó, phân tích của nhóm xem quy mô sản xuất ở cấp quốc gia–năm có liên hệ thế nào với `total_9` của các lô CQI. Hai bài khác nhau ở biến dùng để giải thích sự khác biệt về điểm và ở cách biểu diễn chất lượng cảm quan.

## 7. Processing Methods by Country and Continent
### a. Thông tin notebook
- **Tác giả đăng:** RealDealAdamP.
- **Link:** [Processing Methods by Country and Continent trên Kaggle](https://www.kaggle.com/code/adampq/processing-methods-by-country-and-continent).

### b. Câu hỏi nghiên cứu
Từ hai biểu đồ trong notebook, các câu hỏi được đưa ra là những phương pháp sơ chế nào xuất hiện ở từng quốc gia và từng châu lục trong mẫu CQI? Tách hai cấp địa lý giúp xem một phương pháp xuất hiện ở đâu khi nhìn theo từng nước và khi nhìn theo châu lục.

### c. Phương pháp phân tích
1. **Chọn dữ liệu:** Tác giả đọc `Coffee_Qlty.csv` và dùng ba cột `Processing.Method`, `Country.of.Origin` và `Continent.of.Origin` cho phần trực quan hoá.
2. **Vẽ hai scatter plots:** Cả hai biểu đồ đặt `Processing.Method` trên trục ngang và dùng màu để phân biệt phương pháp. Trục dọc lần lượt là quốc gia và châu lục. Mỗi điểm lấy từ một dòng trong CSV, vì vậy nhiều lô có cùng phương pháp và xuất xứ có thể chồng lên nhau. Biểu đồ cho thấy một tổ hợp xuất hiện ở đâu. Muốn so tần suất giữa các nhóm cần thêm bảng số lô hoặc tỷ lệ theo từng nhóm.

### d. Đối chiếu với câu hỏi của nhóm
Notebook của RealDealAdamP dùng xuất xứ để xác định những phương pháp sơ chế nào xuất hiện tại mỗi nơi. Phân tích của nhóm dùng quốc gia cùng năm thu hoạch để nối sản lượng FAOSTAT, giúp phân biệt những năm có mức sản lượng khác nhau ngay trong cùng một nước. Câu hỏi của nhóm vì vậy xoay quanh mối liên hệ giữa sản lượng và `total_9` của lô, còn hai biểu đồ trong notebook mô tả sự hiện diện của phương pháp sơ chế theo địa lý.
