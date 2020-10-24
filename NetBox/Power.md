# Power 

Ví dụ về cấu trúc liên kết nguồn. 

![Imgur](https://i.imgur.com/q6yNYuA.png)

## Power Panel

Là 1 bảng điều khiển đại diện cho bảng phân phối mạch điện và bộ ngắt mạch. Nếu bạn có nhiều bảng điện trong trung tâm giữ liệu của mình, bạn nên lập mô hình quản lý trong netbox để hỗ trợ xác định mức dự phòng của phân bổ điện. 

Ta sẽ tạo `powwer panel` sử dụng làm 1 bảng điều khiển chung cho các `power feed` : 

Kích vào `+` để tạo 1 `power panel` mới : 

![Imgur](https://i.imgur.com/Xe0H7UC.png)

![Imgur](https://i.imgur.com/WFkaV4W.png)

- `Site` : Chọn Site 

- `Rack group`: Chọn rack group. Vì panel này là 1 bảng điều khiển, phân phối mạch điện cho cả tòa nhà nên mình đặt trong `Rack group` đại diện cho tất cả các rack trong tòa nhà là `FPT Data Center`

- `Name`: Nhập vào tên cho `Power panel` định tạo. 

Và sau đó bấm `Create` để tạo. 

## Power Feed 

Xác định outlet/drop đi đến các rack. Power feeds có loại cung cấp (AC/DC), điện áp, cường độ dòng điện và phase ( 3 pha hoặc đơn pha)

Trong ngữ cảnh của PDU, power feed tương tự với `power outlet` mà `power port` của PDU kết nối với. 

Việc sử dụng năng lượng của rack được tính khi `power feed` được gán cho rack đó và được kết nối với `power port`. 

Để tạo `power feed` ta làm như sau : 

![Imgur](https://i.imgur.com/GwRNjJM.png)

![Imgur](https://i.imgur.com/8usHPSI.png)

- `Site` : Chọn Site là `cloud365-FPT`

- `Power Panel` : Power Panel FPT

- `Rack` : Chọn tủ rack cần add 

- `Name` : Đặt tên cho power feed này. 

- `Status` : Chọn trạng thái cho feed này. 

Phần `Characteristics` : 

Chọn `Type` là `Primary` hoặc `Redundant`. Dòng điện xoay chiều (AC), có điện áp là 230v, 16 ampe, sử dụng dòng điện 3 pha và mức sử dụng tối đa cho phép là 80%. 

![Imgur](https://i.imgur.com/2DaOvfl.png)

Tiếp theo có thể đánh tags hoặc không sau đó chọn `Create` để tạo . 

Theo mô hình cấu trúc liên kết nguồn ở trên, ta sẽ tạo 2 power feed. Tương tự như trên, tạo thêm 1 power feed nữa. 


