# Sử dụng Wireshark để xác định máy chủ và người dùng. 

## Thông tin máy chủ từ traffic DHCP

Bất kỳ máy chủ nào tạo traff trong mạng đều phải có 3 số nhận dạng là: địa chỉ MAC, địa chỉ IP, hostname.

Trong hầu hết các trường hợp, cảnh báo cho hoạt động đáng ngờ dựa trên địa chỉ IP.


Sử dụng trafic dhcp [tại đây](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/Traffic/dhcp.pcap). Mở Wireshark và sử dụng filter là dhcp.

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host1.png)

Chọn 1 gói tin chứa request DHCP. Đi tới phần chi tiết khung và mở rộng dòng cho giao thức Dynamic Host Configguration Protocol

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host2.png)

Sau khi kích vào phần mở rộng ta sẽ thấy được thông tin về địa chỉ MAC của client và hostname của client. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host3.png)

Để xem thông tin về IP và địa chỉ MAC của server, hãy xem gói tin ACK (gói tin được gửi từ DHCP server). Sau đó hãy kích vào Ethernet II. 
 
![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host4.png)

Ta thấy được địa chỉ MAC nguồn (chính là địa chỉ MAC của DHCP server), và địa chỉ IP của DHCP server. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host5.png)

Như vậy, từ gói tin DHCP, ta có thể lấy được thông tin máy chủ bao gồm địa chỉ MAC, địa chỉ IP và Hostname. 

## Mô hình thiết bị và hệ điều hành từ lưu lượng truy cập HTTP 

Chuỗi User-agent từ các header trong traffic HTTP có thể tiết lộ hệ điều hành. Nếu lưu lượng HTTP đến từ thiết bị Android, ta cũng có thể xác định nhà sản xuất và kiểu thiết bị. 

Sử dụng lưu lượng để thực hành [tại đây](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/Traffic/host-and-user-ID-pcap-03.pcap.zip). 

Sử dụng filter để lọc ra các gói tin http 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host6.png)

Kích chuột phải vào 1 trong các gói tin sau đó chọn `Follow` -> `TCP Stream` 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host7.png)

Từ luồng TCP, sau khi quan sát User-Agent. Ta có thể thấy người dùng truy cập đang sử dụng hệ điều hành  Windows 7 và trình duyêt chome để truy cập. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host8.png)


**(Windows NT 6.1; Win64; x64)** : Thể hiện rằng đây là windows 7. 

Thông số đằng sau NT cho ta biết được đó là hệ điều hành gì. 

- Windows NT 5.1: Windows XP
- Windows NT 6.0: Windows Vista
- Windows NT 6.1: Windows 7
- Windows NT 6.2: Windows 8
- Windows NT 6.3: Windows 8.1
- Windows NT 10.0: Windows 10

Sử dụng lưu lượng truy cập của Android [tại đây](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/Traffic/host-and-user-ID-pcap-04.pcap.zip).

Mở file bằng wireshard và sử dụng filter là `http`. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host9.png)

Sau đó, kích chuột phải vào 1 trong các gói tin http rồi chọn `Follow` -> `TCP Stream`. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host10.png)

Từ User-Agent, ta có thể thấy rằng người dùng truy cập web đang sử dụng android phiên bản 7.1.2 và kiểu máy của thiết bị này là `LM-X210APM` 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host11.png)

Tìm kiếm nhanh trên Google với kiểu máy trên ta có thể thấy được đó là `LG Phoenix 4`. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/user-host12.png)

**Lưu ý:**  Không phải tất cả các lưu lượng HTTP đều là lưu lượng truy cập web, vậy nên 1 số yêu cầu HTTP không tiết lộ trình duyệt hoặc hệ điều hành. Khi muốn tìm kiếm thông tin thông qua lưu lượng http, có thể phải thử 1 số yêu cầu http khác nhau trước khi tìm thấy lưu lượng truy cập trình duyệt web. 

Vì ngày càng có nhiều trang web sử dụng HTTPS nên phương pháp xác định thông tin thông qua HTTP có thể khó khăn. 

**Tài liệu tham khảo**

https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/
