# Thiết lập kết nối cho các thiết bị 

Tiếp theo mình sẽ tiến hành thiết lập các kết nối cho thiết bị ( Kết nối nguồn, kết nối interface và đặt IP, add các Iventory)

## Kết nối nguồn 

Để kết nối nguồn, trước tiên mình sẽ tạo 1 PDU cho rack. 

Kích vào tạo thiết bị như phần trước nhưng ta sẽ không đặt nó vào `U` (Có thể gọi là thiết bị không ăn U)

![Imgur](https://i.imgur.com/5dMS64D.png)

Tương tự vậy ta sẽ tạo ra 2 PDU cho tủ rack này. 

Sau khi tạo, kích vào rack để xem. Những thiết bị không ăn U sẽ được liệt kê tại đây. 

![Imgur](https://i.imgur.com/fiZCEqq.png)

Sau đó ta kích vào PDU 1 và kích và kết nối sau đó chọn `Power Feed` để kết nối PDU với `Power Feed`. 

![Imgur](https://i.imgur.com/XT8zAAA.png)

ta sẽ điền các thông số như sau: 

![Imgur](https://i.imgur.com/2u79HO6.png)

- `1` : Chọn `Site` 

- `2` : Chọn rack group là `FPT Data Center` 

- `3` : Chọn `Power Panel` (Chọn đúng Power Panel có kết nối với Power Feed của rack này thì mới có thể hiển thị đúng ở phần sau)

- `4` : Chọn `Power Feed` để kết nối với PDU (`Power Feed 1` kết nối với `PDU 1`)

- `5` : Chọn kiểu dây (mình sẽ chọn là power)

Sau đó chọn màu để nhận diện và có thể nhập vào length là độ dài dây (nếu không nhập thì độ dài dây sẽ mặc định là 1 met). Chọn `Connect` để kết nối. 

Tương tự vậy ta sẽ kết nối `PDU 2` với `Power Feed 2` . 

Sau khi đã có PDU kết nối với `Power Feed` ta sẽ tạo các kết nối cho các thiết bị (server và Switch).

Chọn vào thiết bị ta sẽ thấy rằng đã có 1 `power port` được tạo mặc đinh ở phần trước. Kích vào nút có dạng connect và chọn `Power Outlet` 

Vì nguồn của các thiết bị trên `Data Center` sẽ được cắm vào các ổ cắm trên PDU nên mình sẽ tạo kết nối cho `Power Port` trên thiết bị kết nối đến các `power outlet` của PDU. 

![Imgur](https://i.imgur.com/bPIRvi8.png)

Và ta sẽ nhập vào như sau : 

![Imgur](https://i.imgur.com/E6rNKQZ.png)

- `1` : Chọn Site 

- `2` : Vị trí của thiết bị (tủ rack)

- `3` : Chọn `PDU 1 ` hoặc `PDU 2` 

- `4` : Chọn vị trí chân cắm trên PDU để connect tới. (Các chân đã được cắm cho thiết bị khác sẽ không thể chọn được)

- `5` : Chọn kiểu dây là `Power` 

Tiếp theo chọn màu và độ dài của dây. Kích và `Connect` để tạo kết nối. 

Nếu máy có 2 nguồn thì ta sẽ có 2 `Power Port`, mỗi cổng kết nối đến 1 PDU khác nhau. 

## Kết nối các thiết bị (server) với Switch 

Chọn vào `+ Add Components` chọn `Interface` . 

![Imgur](https://i.imgur.com/Pjl3rwq.png) 

![Imgur](https://i.imgur.com/8MZyrS5.png)

- `Name` : Nhập vào tên của interface 

- `Type` : chọn loại card mạng 

- `MAC Address` : Nhập địa chỉ MAC cho interface này 

- `Mode` : Mình đặt mode là Access 

- `Untagged vlan` : Chọn Vlan cho card mạng này. 

sau đó chọn `Create` để tạo. 

Chọn `+` để thêm IP cho card mạng này. 

![Imgur](https://i.imgur.com/HTPQLB9.png)

Nhập vào địa chỉ IP 

![Imgur](https://i.imgur.com/q0NIsuN.png)

Chọn `Make this the primary IP for the device/VM` để đặt làm IP chính cho thiết bị. Nếu không phải IP chính có thể bỏ qua. 

![Imgur](https://i.imgur.com/RFFXSKx.png) 

Chọn `Create` để thêm. 

Tiếp theo để thiết lập kết nối cho card mạng này, kích vào như dưới sau đó chọn `Interface` để tạo kết nối đến `Switch`. 

![Imgur](https://i.imgur.com/taEL72L.png)

Nhập vào như sau : 

![Imgur](https://i.imgur.com/lI8GhPd.png)

- `Device` : Chọn thiết bị là Switch 

- `Name` : Chọn số Port của Switch ( Thiết bị sẽ cắm đến Port của Switch) 

Tiếp theo `Cable` chọn loại Cap kết nối : 

- `Type` là loại  `CAT 5`

- `Color` : Chọn màu cho Cap này. Sau đó chọn độ dài của cap. Nếu không chọn thì độ dài mặc định sẽ là 1 sau đó chọn `Connect` để kết nối





