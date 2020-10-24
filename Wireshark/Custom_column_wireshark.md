# Custom các cột trong wireshark

Theo mặc định, wireshark sẽ hiển thị các cột như: 

- No. -Frame number của file pcap
- Time -giây được chia nhỏ thành nano giây từ frame đầu tiên của filepcap
- Source -Địa chỉ IP nguồn của gói tin 
- Destination -Địa chỉ IP đích của gói tin
- Protocol -Giao thức được sử dụng 
- Length -độ dài frame (tính bằng byte)
- info 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum1.png)

Để hiển thị thêm 1 số cột hoặc loại bỏ những cột không mong muốn, có thể làm như sau: 

## Ẩn cột

Để loại bỏ 1 cột, kích chuột phải vào trường tiêu đề của cột.

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum2.png)

Ví dụ mình muốn loại bỏ cột time, mình sẽ kích chuột phải vào thanh tiêu đề, sau đó bỏ tích chọn cột time. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum3.png)

Ta thấy rằng cột time đã được loại bỏ. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum4.png)

## Xóa cột 

Giả sử muốn xóa cột `time` khỏi các trường tiêu đề, hãy kích chuột phải vào tên của cột và chọn `Remove this Column` 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum5.png)

Ta thấy rằng cột đã hoàn toàn bị xóa.
![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum6.png)


## Thêm cột 

Để thêm cột, hãy nhấp chuột phải vào bất cứ tiêu đề cột nào, sau đó chọn `column preferences` . 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum7.png)

Sau đó chọn colum và tích dấu `+` để thêm 1 cột mới. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum8.png)

Ta thấy rằng đã xuất hiện thêm 1 trường new cloumn. Bây giờ hãy kích đúp vào trường title để đặt tên cho cột.

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum9.png)

Mình sẽ tạo thêm 2 cột lần lượt là `Source port` và `destination port`. Đầu tiên, mình sẽ tạo source port. 

Đặt tên cho title là `src port` và chọn type là `Source Port`.

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum10.png)

Tương tự như vậy, tạo thêm 1 cột mới và đặt tên cho title là `des port`, chọn type là `Destination Port`. 

Sau đó kích chọn OK để lưu lại. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum11.png)

Ta thấy rằng đã có thêm 2 cột là `Src Port` và `Des Port`. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum12.png)


## Định dạng cột thời gian

Để định dạng lại cột thời gian, kích vào view, sau đó chọn `Time Display Format`. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum13.png)

Tại đây có rất nhiều các tùy chọn về format thời gian, mình chọn sử dụng format cho thời gian là UTC. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum14.png)

Ta thấy rằng định dạng thời gian đã được thay đổi. 

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum15.png)

## Tạo 1 cột tùy chỉnh

Để tạo thêm 1 cột tùy chỉnh, ví dụ ta muốn tạo thêm cột `Request command` của gói tin FTP, ta kích chuột phải vào trường `Request command` và chọn `Apply as Column`.

![](https://github.com/hungviet99/thuc_tap/blob/master/Wireshark/image/colum15.png)

**Tài liệu tham khảo** 

https://unit42.paloaltonetworks.com/unit42-customizing-wireshark-changing-column-display/