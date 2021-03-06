# Custom các cột trong wireshark

Theo mặc định, wireshark sẽ hiển thị các cột như: 

- No. -Frame number của file pcap
- Time -giây được chia nhỏ thành nano giây từ frame đầu tiên của filepcap
- Source -Địa chỉ IP nguồn của gói tin 
- Destination -Địa chỉ IP đích của gói tin
- Protocol -Giao thức được sử dụng 
- Length -độ dài frame (tính bằng byte)
- info 

![](../images/colum1.png)

Để hiển thị thêm 1 số cột hoặc loại bỏ những cột không mong muốn, có thể làm như sau: 

## Ẩn cột

Để loại bỏ 1 cột, kích chuột phải vào trường tiêu đề của cột.

![](../images/colum2.png)

Ví dụ mình muốn loại bỏ cột time, mình sẽ kích chuột phải vào thanh tiêu đề, sau đó bỏ tích chọn cột time. 

![](../images/colum3.png)

Ta thấy rằng cột time đã được loại bỏ. 

![](../images/colum4.png)

## Xóa cột 

Giả sử muốn xóa cột `time` khỏi các trường tiêu đề, hãy kích chuột phải vào tên của cột và chọn `Remove this Column` 

![](../images/colum5.png)

Ta thấy rằng cột đã hoàn toàn bị xóa.

![](../images/colum6.png)

## Thêm cột 

Để thêm cột, hãy nhấp chuột phải vào bất cứ tiêu đề cột nào, sau đó chọn `column preferences` . 

![](../images/colum7.png)

Sau đó chọn colum và tích dấu `+` để thêm 1 cột mới. 

![](../images/colum8.png)

Ta thấy rằng đã xuất hiện thêm 1 trường new cloumn. Bây giờ hãy kích đúp vào trường title để đặt tên cho cột.

![](../images/colum9.png)

Mình sẽ tạo thêm 2 cột lần lượt là `Source port` và `destination port`. Đầu tiên, mình sẽ tạo source port. 

Đặt tên cho title là `src port` và chọn type là `Source Port`.

![](../images/colum10.png)

Tương tự như vậy, tạo thêm 1 cột mới và đặt tên cho title là `des port`, chọn type là `Destination Port`. 

Sau đó kích chọn OK để lưu lại. 

![](../images/colum11.png)

Ta thấy rằng đã có thêm 2 cột là `Src Port` và `Des Port`. 

![](../images/colum12.png)


## Định dạng cột thời gian

Để định dạng lại cột thời gian, kích vào view, sau đó chọn `Time Display Format`. 

![](../images/colum13.png)

Tại đây có rất nhiều các tùy chọn về format thời gian, mình chọn sử dụng format cho thời gian là UTC. 

![](../images/colum14.png)

Ta thấy rằng định dạng thời gian đã được thay đổi. 

![](../images/colum15.png)

## Tạo 1 cột tùy chỉnh

Để tạo thêm 1 cột tùy chỉnh, ví dụ ta muốn tạo thêm cột `Request command` của gói tin FTP, ta kích chuột phải vào trường `Request command` và chọn `Apply as Column`.

![](../images/colum15.png)

**Tài liệu tham khảo** 

https://unit42.paloaltonetworks.com/unit42-customizing-wireshark-changing-column-display/