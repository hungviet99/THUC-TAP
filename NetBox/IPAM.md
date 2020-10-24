# IPAM (IP Management)

IPAM sử dụng để quản lý vag iams sát cơ sở hạ tầng địa chỉ IP, để chúng ta biết được ta đang có những vlan nào, có tổng cộng bao nhiêu địa chỉ IP, những IP nào đã sử dụng và số lượng IP khả dụng (số lượng IP chưa sử dụng).

Bố cục IPAM sẽ có các mục như sau : 

![Imgur](https://i.imgur.com/TgLBSRb.png)

Mình sẽ nói về các khái niệm và tạo các mục từ dưới lên. 

## Vlans

### Vlan Group 

Phần này sử dụng để nhóm các vlan có chung mục đích sử dụng vào trong 1 group chung. 

các vlan khác group thì có thể có các ID vè tên trùng nhau, còn chung nhóm thì không. 

Ví dụ mình có 2 vlan là Vlan 634 và vlan 635 đều sử dụng cho cụm thực tập, nên mình sẽ tạo 1 group có tên là thực tập và tiến hành add vlan đó vào. 

Để add Vlan Group, thực hiện như sau : 

Kích vào dấu `+` để tạo 1 vlan group. 

![Imgur](https://i.imgur.com/is6kwTU.png)

Sau đó ta sẽ điền như sau : 

![Imgur](https://i.imgur.com/Qaz0708.png)

- `Site` mình sẽ đặt vlan group này thuộc site đã tạo ở mục Organization là `cloud365-FPT` 

- `Name`: Là tên của vlan group mình đặt là `Thực tập`

- `Slug`: Thường thì mình để tự sinh ra hoặc bạn cũng có thể sửa theo ý muốn để nó hiển thị trên URL được đẹp. 

- `Desscription`: Mô tả thêm cho VLAN Group này . 

Tương tự như vậy hãy tạo các Vlan Group theo hệ thống quản lý của bạn. 

### VLANs

Phần này sẽ tạo ra các vlan, những vlan nào có chung mục đích sử dụng có thể nhóm vào chung 1 nhóm gọi là Vlan Group. Mỗi Vlan được xác định bằng Tên và ID. 

Mỗi Vlan có thể dk gán cho Site hoặc/và Vlan Group và có các trạng thái hoạt động như : `Active`, `Reserved`, `Deprecated`. 

Như đã nói ở trên, các vlan có thể có cùng ID và Name nếu nó khác `Vlan Group`. Ở đây mình đã tạo các vlan để kiểm chứng : 

![Imgur](https://i.imgur.com/GYftBrq.png)

Như hình trên ta thấy 2 vlan thuộc Group khác nhau đều có thể đặt cùng tên và ID nhưng 2 vlan trong cùng group là `634` và `635` thì không thể cùng tên và ID. 

Vì Vlan mình sử dụng cho các device trước đó tạm thời chưa thuộc nhóm nào nên mình sẽ tạo 1 vlan và không thêm vào `Vlan Group`. 

Kích vào `+` để tạo 1 vlan 

![Imgur](https://i.imgur.com/5NDLtHc.png) 

Nhập vào các thông số để tạo : 

![Imgur](https://i.imgur.com/AFDg8j8.png)

- `ID`, `Name` : Nhập vào id và tên Vlan được đặt và quy định trong mạng của bạn. 

- `Status` : Trạng thái hiện tại của vlan ( đang được sử dụng, đang chờ, ...)

- `Site` : Vlan này được đặt trên Site nào. 

- `Group` : VLan này mình không thêm vào nhóm vlan cụ thể nào. 

- `Role` mình tạm thời bỏ qua. 

- `Description` : miêu tả thêm cho vlan này. 

![Imgur](https://i.imgur.com/PhSzJ3Z.png)

Phần `Tenancy` bỏ qua vì mình không tạo đối tượng khách hàng ngay từ đầu 

Phần `Tags` mình cũng không đặt, nếu muốn bạn có thể đánh tags cho mục này bằng cách nhập vào các tag. Ví dụ `vlan`

## VRF

Mỗi VRF về cơ bản là 1 bảng đinh tuyến riêng. VRF thương được sử dụng để ngăn cách các khách hàng và các tổ chức với nhau trong mạng. 

Mỗi VRF được gán một tên duy nhất. Bất kỳ prefix hoặc địa chỉ IP nào không được gán cho VRF sẽ thuộc về global. 

Phần này tạm thời mình bỏ qua. 

## Aggregates

### RIRs (Regional Internet Registries)

RIR chịu trách nhiệm phân bổ không gian địa chỉ. Có năm RIR là ARIN, RIPE, APNIC, LACNIC và AFRINIC. Tuy nhiên, 1 số không gian địa chỉ được sử dụng nội bộ, được xác định trong RFC 1918 và 6598. Ngoài ra còn có các cơ quan đăng ký cấp thấp hơn phục vụ 1 khu vực địa lý cụ thể. 

Mỗi Aggregate phải được gán cho 1 RIR.

Dưới đây là năm RIR: 

![Imgur](https://i.imgur.com/k9fCOkc.png)

Tạo 1 RIR như sau : 

Chọn tab `+` : 

![Imgur](https://i.imgur.com/alj1GFW.png)

Mình sẽ tạo 1 RIR cho vùng ở Việt Nam : 

![Imgur](https://i.imgur.com/Jed1KL5.png)

- `Name` : Nhập vào tên của RIR cho vùng Việt Nam là `APNIC` 

- `Slug` : mình để tự sinh 

- Tiếp theo có thể kích chọn private nếu sử dụng cho các địa chỉ là private 

- `Description` mô tả thêm cho cơ quan này (Phần này mình bỏ qua)

Sau đó chọn `Create` để tạo. 

Tiếp theo tại các `Aggregates` 

### Aggregates

Sử dụng để xác định 1 dải địa chỉ lớn, xác định phân bổ cấp cao nhất. 

Một số không gian địa chỉ riêng được sử dụng phổ biến chẳng hạn như: 

- 10.0.0.0/8 (RFC 1918)
- 100.64.0.0/10 (RFC 6598)
- 172.16.0.0/12 (RFC 1918)
- 192.168.0.0/16 (RFC 1918)

Mỗi Prefix sẽ tự sắp xếp theo Aggregates của nó nếu tồn tại. Lưu ý rằng bạn chỉ nên tạo Aggregates cho các dải IP thực sự được phân bổ cho tổ chức của bạn, hoặc các dải được sử dụng riêng. 

Mình sẽ tạo Agregates cho 1 dải IP private với địa chỉ lớn nhất là `10.0.0.0/8`

![Imgur](https://i.imgur.com/Haq3yxe.png)

![Imgur](https://i.imgur.com/B2cSH4c.png)

- `Prefix` : Nhập vào dải địa chỉ lớn nhất 

- `Rir` : Cơ quan đăng ký Internet (Phần này đã tạo trước đó, kích xuống dưới và chọn Cơ quan đăng ký)

- `Date added` : Chọn ngày khởi tạo. 

- `Description` : Nhập vào mô tả cho phần này hoặc để trống. 

- `Tags`: Đánh tag cho phần này. 

Sau đó chọn `Create` để tạo. 

Tương tự đó, khi muốn tạo prefix ta sẽ tạo 1 Agregates là 1 địa chỉ phân bổ ở mức cao nhất của địa chỉ mà bạn định sử dụng. 

Mình có tạo 2 agregates như sau : 

![Imgur](https://i.imgur.com/bAxyjHX.png)

## Prefixes

### Prefixes 

Nhập vào địa chỉ mạng và subnet của dải địa chỉ để cấp cho các thiết bị 

Prefix có các Status sau: 

- `Container` : Tóm tắt về prefix con
- `Active` : Đang hoạt động  
- `Reserved` : Chỉ định sử dụng trong tương lai 
- `Deprecated` : Không còn sử dụng 

Mình có 1 địa chỉ mạng là `68.183.224.0/20` thì sẽ khai báo như sau : 

![Imgur](https://i.imgur.com/eAd0iK0.png)

- `prefix` : Nhập vào địa chỉ mạng và subnet mask 

- `Status` : là Active 

- `VRF`, `Role` : Nếu có tạo VRF hoặc Role ở các bước trước thì có thể chọn. Phần này mình để trống 

- `Description`: Phần này mô tả thêm cho prefix này. 

và tích chọn `Is a pool` - tức là tất cả địa chỉ IP của mạng này có thể sử dụng 

phần `Site/VLAN Assignment` : 

Chọn `Site` và `VLAN` cho prefix. Bỏ qua phần VLAN group vì như đã nói ở trên, vlan này không thuộc vlan group nào. 

![Imgur](https://i.imgur.com/58aMjsJ.png)

Có thể đánh tags hoặc bỏ qua và kích `Create` để tạo. 

## IP addresses

Một địa chỉ IP bao gồm một địa chỉ máy chủ duy nhất (IPv4 hoặc IPv6) và mặt nạ mạng con của nó. Mặt nạ của nó phải khớp chính xác với cách địa chỉ IP được cấu hình trên một giao diện trong thế giới thực.

Giống như tiền tố, một địa chỉ IP có thể được gán tùy ý cho VRF (nếu không, nó sẽ xuất hiện trong bảng "toàn cầu"). Địa chỉ IP được tổ chức tự động theo tiền tố gốc trong VRF tương ứng của chúng.

Cũng giống như tiền tố, mỗi địa chỉ IP có thể được gán một trạng thái và vai trò. Các trạng thái trong NetBox bao gồm các phần sau:

- Active
- Reserved
- Deprecated 
- DHCP

Để tạo địa chỉ IP ta chú ý đến 2 trường sau : 

![Imgur](https://i.imgur.com/rlac55o.png)

Trường `New IP` sử dụng để tạo mới từng địa chỉ IP 1. Thường sử dụng để tạo các địa chỉ là `Gateway` hoặc tạo các địa chỉ `Nat`. Trường thứ 2 là `Bulk Create` sử dụng để tạo hàng loạt các địa chỉ ip. 

Trước tiên mình sẽ tạo 1 địa chỉ là gateway của mạng này : 

![Imgur](https://i.imgur.com/MGq39db.png)

- `Address` : Nhập vào địa chỉ là gateway (Bạn cũng có thể tạo địa chỉ IP ở đây)

- `Status` là Active 

- Bỏ qua các phần là `Role`, `VRF`, `DNS Name`  

- `Description` : Mô tả về địa chỉ IP này 

![Imgur](https://i.imgur.com/s2uAwsx.png)

Bỏ qua phần `Tenantcy` và `NAT IP`

- `Tags` : Nhập vào tag cho địa chỉ IP, nếu không nhập có thể bỏ qua và chọn `Create` để tạo. 

Tiếp đến ta sẽ tạo 1 loạt các địa chỉ IP để cấp cho các thiết bị : 

Chuyển sang tab `Bulk Create` để tạo nhiều địa chỉ IP 

![Imgur](https://i.imgur.com/MPqAPRI.png)

- `Address pattern` : Nhập vào để tạo nhiều địa chỉ IP trong khoảng từ [2-20] sẽ tạo ra các địa chỉ `68.183.224.2` `->` `68.183.224.20`. 

- `Status` :  Active

- `Description` để mô tả chi tiết cho IP này. Sau đó chọn `Create` để tạo cùng lúc nhiều địa chỉ IP. 

> Lưu ý : Sử dụng đến đâu thì ta nên khai báo đến đó. Không nên khai báo quá nhiều các địa chỉ IP với trạng thái Active mà chưa dùng đến vì như vậy sẽ làm khó khăn trong công tác quản lý thông tin địa chỉ IP
