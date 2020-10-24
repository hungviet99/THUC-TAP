# Devices

Các phần sau có thể được tạo trực tiếp. Những phần không có dấu `+` sẽ được tạo khi thiết lập các kết nối. 

![Imgur](https://i.imgur.com/9pqt6BM.png)

Để tạo `Devices` ta cần biết các khái niệm và tạo lần lượt như sau: 

## Device Types

### Manufacturers 

Phần này đề cập đến 1 hãng sản xuất ra thiết bị đó, ví dụ như dell, cisco, ... 

Để tạo `Manufacturers` làm như sau : 

![Imgur](https://i.imgur.com/I2Vu9x4.png)

Ở đây mình sẽ có 2 lựa chọn là chỉ thêm các nhà sản xuất các thiết bị đang được đặt trên tủ rack hoặc thêm tất cả các nhà sản xuất phổ biến để sau này khi có thiết bị thuộc nhà sản xuất đó thì không cần quay lại thêm nữa. 

Mình sẽ tạo 1 số hãng của thiết bị chủ yếu có trong hệ thống của mình mà không add hết các hãng trên thị trường. Mình sẽ add một số các hãng như Supermicro, HP, Dell, Cisco, ...

![Imgur](https://i.imgur.com/Afisrxp.png)

- `Name`: Đặt tên đúng với tên của hãng hoặc tên viết tắt của hãng

- `slug`: Có thể để tự sinh ra hoặc tạo 1 url trông gọn gàng hơn nếu quá dài. 

- `Description` : Mô tả cho manufacturer

Tương tự như phần tạo hãng `Supermicro` ở trên, ta lần lượt tạo thêm các hãng như `Dell`, `HP`, `Cisco`, `IBM`, `Intel`, .. 

Ta sẽ được các manufacturers như sau : 

![Imgur](https://i.imgur.com/RM4eXPa.png)

### Device Types 

Device type đại diện cho 1 kiểu dáng, kiểu phần cứng cụ thể trong thực tế. Các device type xác định thuộc tính của thiết bị (Chiếm bao nhiêu chiều cao và chiều sâu của rack) và các thành phần riêng lẻ của nó (Giao diện điều khiển, nguồn và giao diện mạng)

Để tạo 1 device type, kích vào nút khởi tạo device : 

![Imgur](https://i.imgur.com/XR2ieOh.png)

Sau đó lần lượt điền vào tương tự như sau : 

![Imgur](https://i.imgur.com/N1t6Dxu.png)

- `Manufacturer` : Ở phần trước mình đã tạo các manufacturer cho các thiết bị của mình. Bây giờ mình muốn thêm các kiểu thiết bị và khi tạo kiểu thiết bị mình phải thêm kiểu thiết bị đó thuộc hãng nào. Kiểu thiết bị của mình định tạo là của lenovo nên mình sẽ chọn kiểu `Lenovo`. 

- `Model` : Ở đây sẽ đặt tên cho kiểu thiết bị này. Đặt tên giống với tên thiết bị nhất có thể để dễ phân biệt. 

- `Slug` : Có thể để tự sinh ra khi nhập model. 

- `part number` : Phần này là tùy chọn (có hoặc không nên ta có thể bỏ qua)

- `height (U)` : Mỗi thiết bị được xác định sẽ chiếm bao nhiêu chiều cao của rack, thường là từ 1 -> 2 U. Thiết bị của mình chiếm 2 U nên mình đặt là 2. Sau đó tích vào `Is full depth` nếu thiết bị có chiều sâu bằng với chiều sâu của rack, còn nếu chiều sâu của thiết bị không chiếm hết chiều sâu của rack thì ta không tích vào phần này. 

- `Parent/child status` : phần này ta tạm thời bỏ qua vì k có kiểu thiết bị cha hay con nào.

Chuyển đến các tab tiếp theo 

![Imgur](https://i.imgur.com/SrVTrxo.png)

Chuyển đến phần tiếp theo là hình ảnh của thiết bị. Nếu bạn thêm hình ảnh thì có thể tải lên ảnh mặt trước và mặt sau của thiết bị. 

Phần `Tags` và `Comments` ta mình không đặt. Sau đó bấm `Create` để tạo kiểu thiết bị. 

Tương tự như vậy, hãy tạo các kiểu thiết bị mà bạn đang sử dụng trên hệ thống của mình. Mình tiến hành tạo các kiểu thiết bị mà mình sử dụng hoặc sẽ sử dụng .  
Dưới đây là các kiểu thiết bị mà mình đang sử dụng và sẽ sử dụng cũng đều được mình tiến hành add vào đây. 

![Imgur](https://i.imgur.com/hkULpZu.png)

Sau khi tạo xong ta chuyển sang và tạo các mục trong phần devices

## Devices 

### Platforms 

Một platforms xác định loại phần mềm chạy trên thiết bị hoặc máy ảo.

2 thiết bị cùng loại có thể chạy các nền tảng khác nhau. Ví dụ 1 máy chạy CentOS 7 và 1 máy chạy Ubuntu 18. 

Chỉ định platforms là một tính năng tùy chọn và có thể bỏ qua nếu không muốn

### Device Roles

Các vai trò của thiaats bị là hoàn toàn tùy biến, bạn có thể tạo vai trò cho core switches, distribution switches and access switches.

Ở đây mình có các thiết bị để làm Switch, Server, vv.. . Nên mình sẽ tạo ra các device role như Server, Access Switch, ...

Để tạo device role ta kích vào nút `+` để tạo mới 1 role

![Imgur](https://i.imgur.com/LPE8O9G.png)

![Imgur](https://i.imgur.com/1mR9wPg.png)

- `Name` : Đặt tên cho role này

- `Slug` : Phần này mình để nó tự sinh ra

- `Color` : Chọn màu cho device role này. 

- `Description` : Bạn có thể thêm mô tả thêm cho device role này. Phần này mình không có mô tả gì thêm. 

Sau đó bấm `Create` để tạo 1 device role. 

Mình có tạo 1 số device role như dưới đây. 

![Imgur](https://i.imgur.com/Gb4Ypur.png)

Sau khi đã tạo device role, ta sẽ tiến hành tạo các device cho tủ rack. 

Nhưng trước khi tạo device, ta sẽ xem xét quay lại các `Device Types`, để tạo các cổng mặc định cho các thiết bị để các thiết bị cùng loại có thể thống nhất với nhau ( cùng số interface, cùng số nguồn, cùng số power outlet). Ví dụ đối với Sw cisco 2690 có 24 port mình sẽ add luôn tại đây, đến khi thêm vào các rack thì ở đâu xuất hiện sw cisco 2690 sẽ mặc định là có 24 interface. 

Đối với mỗi thiết bị sẽ có 2 điểm cần chú ý đó là power port và power outlet 

Đối với các thiết bị trên DC, `power port` thường có kiểu là `IEC 60320 C14` và `power outlet` thường có kiểu là `IEC 60320 C13` 

Trông chúng như sau : 

![Imgur](https://i.imgur.com/nkNtSaB.png)

Để xem sơ đồ cấp nguồn và ý nghĩa, khái niệm của nguồn có thể xem [tại đây](https://github.com/hungviet99/thuc_tap/blob/master/NetBox/Power.md)

#### Đối với Switch 

![Imgur](https://i.imgur.com/9Lw8EkJ.png) 

Ta thấy rằng sw 2690 của Cisco chỉ có 24 port và 1 nguồn. Nên mình sẽ tạo 1 Power Port và 24 interface tương đương với 24 port ở phía sau của switch. 

Trước tiên để tạo power port ta làm như sau : 
Kích và `+ Add Components` và chọn `Power Ports` 

![Imgur](https://i.imgur.com/NgJcTR4.png)



![Imgur](https://i.imgur.com/MkgWqr8.png)

- `Name` : Mình sẽ đặt tên là power 1 ( nguồn 1)

- `Type` : Đối với Switch của mình là chân C14. 

- `Maximum draw`: Mức tiêu thụ năng lượng tối đa mình tạm thời để là 30w

- `Allocated draw` : Mức tiêu thụ điện năng bình thường là 4w

Sau đó bấm `Create` để tạo `power port`. Sau khi tạo ta sẽ thấy nó được xuất hiện tại đây : 

![Imgur](https://i.imgur.com/Uebsk9Z.png)

Tiếp theo đối với loại sw này, ta cần tạo 24 interface cho nó.  Và quá trình tạo cũng tương tự như trên, kích vào `+ Add Components` và chọn `Interfaces` 

![Imgur](https://i.imgur.com/rZPJTKT.png)

Tiếp theo ta nhập vào các thông tin để tạo : 

![Imgur](https://i.imgur.com/bk6uPIt.png)

- `Name` : Sử dụng [1-24] sẽ tạ ra 24 port và được đánh số từ 1-24 (nếu muốn tạo các port trong khoảng nào thì chỉ cần viết với cú pháp như sau : `[<số bắt đầu> - <Số kết thúc>]`

- `Type` : ở đây mình sẽ để là 10GBASE-T (10GE), tùy vào từng loại thiết bị mà ta đặt cho phù hợp. 

Sau đó chọn `Create` để tạo.

Sau khi tạo thì mình sẽ kiểm tra lại và thấy rằng đã có đủ 24 Interface được tạo. 

![Imgur](https://i.imgur.com/sixxzP2.png)

Như vậy đối với switch đã xong, nếu hệ thống của bạn có các kiểu thiết bị switch khác ( có 2 nguồn hoặc nhiều hơn hoặc ít hơn 24 port thì có thể làm theo cách tương tự - Ta sẽ add 2 power port và tạo số lượng interface cho phù hợp) thì có thể làm theo cách tương tự. Bây giờ nếu tạo các device cho rack, nếu xuất hiện switch cisco 2690 thì sẽ mặc định là có 24 port và 1 nguồn rồi. 

#### Server 

Các server thường sẽ có từ 1-2 nguồn, tùy vào từng loại. Mình sẽ tạo nguồn cho thiết bị `HP ProLiant DL120 G7`. Thiết bị này là server và chỉ sử dụng 1 nguồn, nên mình sẽ tạo 1 power port. Các thiết bị khác có 2 nguồn thì sẽ tạo 2 power port. 

![Imgur](https://i.imgur.com/m2uUKyL.png)

Kích vào `Power Ports` để tạo 1 chân c14 (Có thể hiểu là 1 nguồn)

![Imgur](https://i.imgur.com/57pV8m7.png)

Sau đó điền vào các thông số như sau : 

![Imgur](https://i.imgur.com/c4bLZsu.png)

- `Name` : Power 1

- `Type` : Kiểu của chân cắm này là C14 

- `Maximum draw` là lượng tiêu thụ tối đa mình tạm thời để trống. 

- `Allocated draw` : Tiêu thụ sử dụng mình đặt là 750 

- Sau đó bấm `Create` để tạo . 

![Imgur](https://i.imgur.com/IKFHowI.png)

Tương tự vậy, đối với các thiết bị khác có bao nhiêu nguồn thì ta sẽ tạo bấy nhiêu `power port`. 


Mỗi server sẽ có ít nhất 1 cổng Interface mặc định để kết nối mạng. Vì vậy khi tạo kiểu của thiết bị, mình sẽ tạo cho mỗi kiểu thiết bị là server 1 cổng interface mặc định. Các dòng máy có nhiều hơn 1 cổng thì các bạn có thể linh hoạt khai báo thêm cho các máy đó. 

Ở giao diện `Device types`, kích chọn 1 kiểu server. ở đây mình chọn server có kiểu là Dell R720xd . 

![Imgur](https://i.imgur.com/sUCjidW.png)

Kích chọn `+ Add Components` và chọn `Interfaces` để tạo 1 interface. 

Đặt tên cho cổng đầu vào và chọn loại cổng sau đó chọn `Create` để tạo 

![Imgur](https://i.imgur.com/PiZ1HyP.png)

Sau khi tạo ta sẽ thấy hiển thị như sau : 

![Imgur](https://i.imgur.com/lr20YPs.png)

#### PDU 

Với các thiết bị là PDU sẽ phải tạo 1 `power port` và tạo các `power outlet`. 

PDU của mình có 35 chân để cắm nên mình sẽ phải tạo thêm 35 `power outlet` 

Đầu tiên ta sẽ tạo 1 `Power port`, kích vào tạo power port: 

![Imgur](https://i.imgur.com/uDlf8t2.png)

Sau đó điền vào các thông số như sau : 

![Imgur](https://i.imgur.com/iZy0j2j.png)

- `Name` : Các thiết bị thường có 1 hoặc 2 nguồn nên mình tự quy định là nếu có 1 nguồn thì `power port` sẽ đặt là `power 1`, nếu có 2 nguồn ta sẽ có 2 power port tương ứng với 2 tên là `Power 1` và `Power 2` 

- `Type` : C14 

Phần điện năng tiêu thụ của cpu là không đáng kể nếu chỉ có số ít thanh pdu nhưng nếu có hàng ngàn thanh đang được sử dụng thì đó cũng là điều cần lưu ý. Nên mình vẫn đặt mức điện áp tiêu của PDU. 

Sau khi điền xong bấm `Create` để tạo. 

Vậy là mình đã tạo xong các cổng cho các thiết bị chủ yếu trong 1 tủ rack. Giờ ta sẽ tiến hành tạo các device cho rack. 

### Devices

Trong thực tế, trước khi tạo các device, ta cần có các địa chỉ IP để gán cho các devices đó. Vì thế, bạn nên tham khảo cách để tạo ra các địa chỉ IP ở đây trước khi tạo các devices : [IPAM](https://github.com/hungviet99/thuc_tap/blob/master/NetBox/IPAM.md)

Ta có thể tạo thiết bị bằng 2 cách : 

**C1** : Vào giao diện của rack và chọn add device để thêm device. Nếu device ở `U` nào thì mình chọn `U` đó sau đó nhập thông tin device tương ứng 

![Imgur](https://i.imgur.com/zW6ILmy.png)

**C2** : vào Tab `Devices` sau đó chọn `+` tại `Devices` để tạo 1 thiết bị mới. 

![Imgur](https://i.imgur.com/KFDYfpN.png)

Ở đây mình sẽ tạo bằng cách 2. 

![Imgur](https://i.imgur.com/yu3fknv.png)

- `Device` : Phần này sẽ nhập vào tên của thiết bị và loại thiết bị. Lưu ý rằng tên thiết bị trong 1 rack không thể trùng với nhau 

- `Hardware` : CHọn nhà sản xuất thiết bị, Kiểu của thiết bị. Nhập vào `Serial number` và `Asset tag`. Nếu chưa có thông tin có thể bỏ qua. 

- `Location` : Chọn site và rack sẽ đặt thiết bị. `Position` sẽ chọn vị trí (U) của thiết bị trên racks. 

Các phần sau mình tạm thời bỏ qua, kéo xuống dưới và chọn `Create` để tạo. 

![Imgur](https://i.imgur.com/AByHqn5.png)

