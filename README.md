# DecisionTreeClassifier_Stock
Thuật toán được tham khảo ý tưởng bởi bài viết [Link Bài Viết](https://www.datacamp.com/community/tutorials/decision-tree-classification-python)(Nên đọc qua trước, trước khi sử dụng model để thực hiện)

## Chuẩn Bị Data
Chuẩn bị data, Data gồm có giá giao dịch của các công ty trên sàn chứng khoán khác nhau trên đất nước Việt Nam(Khoảng 1.8k công ty). Chi tiết data như sau:
  - Date: Ngày giao dịch 
  - Close: Giá đóng cửa ngày hôm đấy
  - Open: Giá mở cửa ngày hôm đấy
  - High: Giá cao nhất ngày hôm đấy.
  - Low: Giá thấp nhất ngày hôm đấy.
  - Ngoài ra có các chỉ số Volume,Value Match nhưng hiện tôi chưa sử dụng các cái đấy.
Để xử lí đầu vào từ dạng data raw sang dạng data có thể xử dụng được thì tôi tạo ra một folder để transform và format data. Bạn có thể đọc thêm trong folder đó.
Tóm lại sau khi xử lí xong data thì chúng ta sẽ có một Object và 1 thuộc tính chính là bộ data sau khi được xử lí. "Data Real"

## Hàm tính toán tạo trường phụ.
```
def RSI(data, period=20,column='close'):
  # tính toán độ chênh lệch giá hôm trước và hôm sau
  delta = data[column].diff(1) 
  delta = delta.dropna()
  up = delta.copy()
  down = delta.copy()
  up[up<0] = 0
  down[down>0] = 0
  data["up"] = up
  data["down"] = down
  # tính toán trung bình tăng giảm và tỷ lệ tăng giảm
  AVG_Gain = SMA(data,period,column='up')
  AVG_Loss = abs(SMA(data,period,column='down'))
  RS = AVG_Gain/AVG_Loss
  RSI = 100-(100/(1+RS))
  data["RSI"] = RSI
  return data 
 ```
 SMA: Tính trung bình cột nào đấy tùy theo số lượng period(ngày cũ)
 
 ## Chương trình chính
 Setup lấy 29 ngày trước đấy
 ```
    <!--   Tính toán   -->
    Com = t.Company(symbol)
    Com.SetupDataSet()
    data = Com.Data_Real
    MACD(data)
    RSI(data)
    data["SMA"] = SMA(data)
    data["EMA"] = EMA(data)
    data = data[29:]
    keep_column = ["close","open","low","MACD","RSI","SMA","EMA","signal_Line"]
    X = data[keep_column].values
    Y = data["result"].values
    <!--   Gọi module thực hiện   -->
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
    tree = DecisionTreeClassifier().fit(X_train,Y_train)
    arr = tree.predict(X_test)
 ```
 EMA: Đường trung bình động dự báo su hướng. setup mặc định dài thì là 26 hoặc ngắn thì là 12 ngày. 
 ## Kết quả
 - Model áp dựng cho từng công ty một.
 - Tổng hợp lại dự kết quả dự đoán thấp nhất trong 10 ngày gần nhất là đúng 54%.
