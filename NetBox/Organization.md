# Tạo Organization
Phần Organization sẽ có các nhóm với các trường như sau : 

![Imgur](https://i.imgur.com/6y0SmZB.png)

Trước tiên để add được tủ racks, ta cần biết những khái niệm và cách cài đặt lần lượt như sau : 

## Tenancy

Thông thường trước khi tạo các tab trong mục `Racks` và `Sites`, ta nên tạo các nhóm khách hàng trước và các khách hàng sẽ có vai trò đối với các thiết bị. 

`tenants` đề cập đến một khách hàng cá nhân hoặc 1 tổ chức. Các đối tượng sau có thể sẽ được gán cho những người thuê : 
- Sites
- Racks
- Rack reservations
- Devices
- VRFs
- Prefixes
- IP addresses
- VLANs
- Circuits
- Virtual machines

Ở đây mình chưa có các đối tượng khách hàng thuê nên tạm thời sẽ để trống 2 trường ở mục này. 

## Sites

### Regions

Một khu vực có thể sử dụng để xác định cho một lục địa, 1 quốc gia, thành phố hoặc 1 khuân viên. 1 khu vực có thể nằm trong khu vực lớn hơn gọi là parent. Ví dụ ta có 2 khu vực là Cầu Giấy và Hà Nội thì khu vực Hà Nội có thể dùng để sử dụng làm parent của Cầu Giấy. 

Vì DC có vị trí tại quận Cầu Giấy và ở thành phố Hà Nội nên trước tiên ta sẽ tạo Regions là Hà Nội: 

Click vào `Organization` và kích vào dấu `+` để thêm 1 regions mới. 

![organization](https://i.imgur.com/4mKqB6Z.png)

![organization](https://i.imgur.com/3nOBAhA.png)

Ở đây ta sẽ tạo regions là Hà Nội : 

![Imgur](https://i.imgur.com/2yg9Q4q.png)

1. Điền tên của regions

2. Phần này nó có thể tự sinh ra cho mình nhưng cũng có thể sửa để cho khi hiển thị trên url được đẹp hơn

3. Thêm miêu tả hoặc ghi chú cho regions

Sau đó click vào `Create` để tạo regions

Tiếp theo ta sẽ tạo ra 1 regions có tên là Quận Cầu Giấy, thuộc địa phận Hà Nội nên ta sẽ để Hà Nội là Parent : 

CLick để tạo 1 region mới, và điền các thông tin như sau : 

Sau đó điền vào các thông tin với ý nghĩa tương tự như trên và bấm `Create` để tạo regions. 

![Imgur](https://i.imgur.com/e58kZ5E.png)


Sau khi tạo ta sẽ có các thông tin như sau : 

![Imgur](https://i.imgur.com/sZ0KKD9.png)


Sau khi có các `Region`, tiếp theo ta sẽ tạo các Sites

### Sites 

Cách sử dụng Site có thể phục thuộc vào tổ chức của bạn. Nhưng thông thường, 1 site có thể là 1 tòa nhà hoặc 1 khuôn viên. Một site thì nhỏ hơn 1 regions và được nằm trong 1 regions. 

Tương tự như trên, ta tạo Site như sau: 

![Imgur](https://i.imgur.com/2zaWXRF.png)

Mình có tên Công ty là Cloud 365 và đặt máy chủ tại FPT Data Center ở quận Cầu Giấy Hà Nội thì mình sẽ điền như sau: 

![Imgur](https://i.imgur.com/vo9LICM.png)

- `Name` thì có thể đặt là FPT thôi cũng được nhưng mình đặt là cloud365-FPT để cho rõ ràng hơn trong việc nhận diện tên. 

- `Slug` để khi ta kích vào xem site thì phần hiển thị trên url sẽ gọn gàng và đẹp hơn. 

- `Status` mình đặt là đang hoạt động (`Active`)

- `Region` vì vị trí của tòa nhà ở quận Cầu Giấy nên mình sẽ add vào region là Quận Cầu Giấy. 

- `Facility` : Nhà cung cấp trung tâm dữ liệu có thể có nhiều cơ sở, vì vậy mình sẽ miêu tả rõ hơn về cơ sở này. 

- `ASN` có thể tạm thời bỏ qua. 

- `Time zone` ở Việt Nam nên ta sẽ chọn timezone là `Asia/Ho Chi Minh`

- `Description` : miêu tả rõ hơn về `Site` này

Kéo xuông dưới đến phần Tenancy thì ta bỏ trống và xuống mục tiếp theo vì phía trên ta chưa có đối tượng khách hàng được tạo.

![Imgur](https://i.imgur.com/qK6fT5G.png)


Ở phần này điền các phương thức liên hệ phù hợp vào các trường tương ứng.

![Imgur](https://i.imgur.com/tCOn1Sz.png)

Ở phần tag và Comment này có thể điền mô tả rõ và cụ thể hơn về site này hoặc có thể để trống. Sau đó bấm `Create` để tạo `Site`

![Imgur](https://i.imgur.com/AwdL0V1.png)

Sau khi tạo ta có site như sau : 

![Imgur](https://i.imgur.com/AJbpgow.png)

Xong phần tạo site, ta có thể chuyển sang tạo racks

## Racks 

### Rack Roles 

Rack role được sử dụng để miêu tả vai trò của tủ racks, ta có thể đặt cho nó vai trò như sử dụng cho khách hàng hoặc để lưu trữ ....Vai trò của racks là tùy biến. 

Ta sẽ tạo 1 racks roles có tên là `customer device` với mục đích sử dụng để đặt các thiết bị khách hàng

Đầu tiên click để tạo rack roles

![Imgur](https://i.imgur.com/CrFcRp6.png) 

- `Name`: Đặt tên cho vai trò này

- `slug`: có thể để nó tự sinh ra hoặc sửa theo ý muốn

- `Color`: Chọn màu cho vai trò này

- `Description`: Thêm miêu tả chi tiết cho vai trò này 

Sau đó chọn `Create` để tạo vai trò. 

![Imgur](https://i.imgur.com/SfNj62s.png)

### Rack Groups

Mỗi racks có thể được nhóm thành các nhóm. 

Nếu mỗi `Sites` đại diện cho 1 khuôn viên thì `rack group` có thể đại diện cho 1 tòa nhà trên khuôn viên đó. Nếu mỗi `Sites` định nghĩa 1 tòa nhà thì `Racks Group` có thể đại diện cho các tầng hoặc phòng. 

Một rack group có thể bao gồm 1 racks group nhỏ hơn. Ví dụ ta có FPT data center , trong FPT data center thì có các tầng 1, 2, 3 tương ứng với các DC 1, DC 2, DC 3. 

Tạo 1 Rack Group có tên là `FPT Data Center`

![Imgur](https://i.imgur.com/tbFjDqr.png)


![Imgur](https://i.imgur.com/bZbAQYr.png)


- `Site`: sẽ chọn site `cloud365-FPT` đã tạo như ở trên 

- `Parent`: Ta sẽ để trống vì không có đối tượng group cha nào sẽ được add cho Group này. 

- `Name`: Ở đây ta sẽ đặt tên cho group này. Nên đặt tên để khi nhìn lại ta sẽ hiểu được chức năng của nó. Ở đây mình sẽ đặt là FPT Data Center

- `slug`: có thể để cho nó tự tạo hoặc mình có thể sửa cho phù hợp với ý muốn. 

- `Description` : Sử dụng để miêu tả thêm về group này


Tiếp theo ta sẽ tạo 1 rack group nữa là DC 1, 2 và 3 sau đó add cho `FPT Data Center` làm group cha. Vì trong `FPT Data Center` có 3 tầng đặt các máy chủ và mỗi tầng được gọi là các Segment 1, 2 và 3. 

![Imgur](https://i.imgur.com/EdDI7dy.png)

- `Site`: Ta sẽ chọn nó thuộc `cloud365-FPT`

- `Parent` : Ta sẽ để `rack group` ta tạo lúc trước là `FPT Data Center` làm đối tượng cha

- `Name` : Mình sẽ đặt là DC 1

- `Description` : Miêu tả rõ hơn về group này. 


Tương tự như trên, ta sẽ tạo các DC 2 và 3 

![Imgur](https://i.imgur.com/voSn3Wa.png) 


![Imgur](https://i.imgur.com/VFC9JKV.png)

Sau khi tạo ta sẽ có các group như sau : 

![Imgur](https://i.imgur.com/seH0da5.png)

Xong phần tạo group, ta chuyển sang tạo rack

### Racks

Mỗi rack thì được gán cho 1 site, chiều cao của rack được đo bằng đơn vị `U`. Các racks thường cao từ 42 `U` đến 48 `U` nhưng trong netbox ta có thể chỉ định chiều cao của rack tùy ý.  Mỗi rack được gán 1 tên và 1 id cơ sở riêng(tùy chọn). 

Một rack phải được chỉ định là 1 trong các loại sau : 
- 2-post frame
- 4-post frame
- 4-post cabinet
- Wall-mounted frame
- Wall-mounted cabinet

Mỗi rack có 2 mặt trước và sau, trên đó các thiết bị có thể được gắn. Chiều rộng Rail-to-rail có thể từ 10, 19, 21, 23 inches. 

Kích vào tạo racks 

![Imgur](https://i.imgur.com/XmmqDfe.png)

![Imgur](https://i.imgur.com/GZWbrA0.png)

- `Site` : vì thuộc site cloud365-FPT nên ta sẽ chọn `cloud365-FPT`

- `Name`: Tủ rack của mình được đánh tên là `W9`

- `Facility ID` : Nhập vào Id của rack được chỉ đinh bởi cơ sở đặt tủ rack. (id này mình không có thông tin nên mình tạm đặt là `id-w9`)

- `Group` : Tủ rack này được đặt tại DC 2 nên mình sẽ chọn nó thuộc group là `DC 2` 

- `status` : Trạng thái tủ rack vẫn đang được sử dụng 

- `role` : Tủ rack này phục vụ mục đích để đặt các thiết bị của khách hàng nên mình sẽ chọn role là `Customer devices` mà ta tạo ở phía trên.

- `Serial number` và `Asset tag` mình chưa lấy được thông tin nên mình sẽ tạm thời để trống. 

Tiếp theo là `Tenancy` ta cũng tạm thời bỏ trống vì chưa tạo `tenant`.

Ở phần `Dimension` ta có thể điền như sau : 

![Imgur](https://i.imgur.com/dbOGoY4.png)

- `Type` : của mình là kiểu `Wall-mounted cabinet`

- `Width` : 23 inches

- `Height` : được tính bằng U, tủ của mình có chiều cao là 42U. 

- `Outer dimnsions` là phần kích thước được đo phía bên ngoài tủ. Phần này tạm thời mình để trống


Chuyển đến các mục kế tiếp mình không có comment gì thêm về rack này nên mình sẽ để trống và bấm `Create` để tạo racks. 

![Imgur](https://i.imgur.com/JFfXcGZ.png)

Sau khi tạo mình đã có thông tin về tủ rack như sau : 

![Imgur](https://i.imgur.com/c94LAdT.png)


Như vậy tạm thời ta đã xong phần tạo các mục trong `Organization`. Bây giờ ta sẽ chuyển sang tạo các mục trong phần [Devices](https://github.com/hungviet99/thuc_tap/blob/master/NetBox/Devices.md)