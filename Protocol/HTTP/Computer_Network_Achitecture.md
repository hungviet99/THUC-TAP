# Computer Network Achitecture 

Kiến trúc mạng máy tính là cách tổ chức máy tính và cách phân bổ nhiệm vụ cho máy tính 

Có 2 loại kiến trúc mạng máy tính được sử dụng : 

- Peer-To_Peer Network

- Client/Server Network

## 1. Peer-To-Peer 

### Đặc điểm 

Peer-to-peer là mạng trong đó tất cả các máy tính được liên kết với nhau với các đặc quyền và trách nhiệm như nhau để xử lý dữ liệu 

Peer-to-peer hữu ích cho các môi trường nhỏ, thường có tối đa 10 máy tính 

Peer-to-peer không có máy chủ chuyên dụng  

Các quyền đặc biệt được gán cho mỗi máy tính để chia sẻ tài nguyên, nhưng điều này có thể dẫn đến sự cố nếu máy tính có tài nguyên bị hỏng. 

### Ưu điểm 

Nó ít tốn kém hơn vì k có máy chủ chuyên dụng 

Nếu 1 máy tính ngưng hoạt động nhưng các máy tính khác vẫn hoạt động 

Dễ dàng để thiết lập và bảo trì vì mỗi máy tính tự quản lý. 

### Nhược điểm 

Không thể sao lưu dữ liệu vì dữ liệu ở các vị trí khác nhau 

Nó có 1 vấn đề bảo mật như thiết bị được quản lý chính nó

## Client/Server netwwork 

Là mô hình mạng mà người dùng cuối được gọi là client để truy cập các tài nguyên như video, tệp, bài hát ... từ máy tính trung tâm được gọi là máy chủ. 

Central controller được gọi là máy chỉ trong khi tấy cả các máy tính khác trong mạng được gọi là máy khách  

Một server thực hiện tất cả các hoạt động chính như bảo mật và quản lý mạng 

Server chịu trách nhiệ, quản lý tất cả các tài nguyên như file, folder, printer, ... 

Tất cả các máy khách liên lạc với nhau thông qua 1 máy chủ. Nếu client1 muốn gửi dữ liệu đến client2 thì trước tiên nó sẽ gửi yêu cầu đến server để xin phép, server sẽ gửi phản hồi đến máy khách 1 để bắt đầu giao tiếp với máy khách 2. 

### Ưu điểm 

Có thể sao lưu dữ liệu dex dàng vì là 1 hệ thống tập trung

Có 1 máy chủ chuyên dụng giúp cải thiện hiệu suất chung của toàn hệ thống

Bảo mật tốt hơn khi 1 máy chỉ duy nhất quản lý các tài nguyên được chia sẻ. 

Nó cũng làm tăng tốc độ của các tài nguyên chia sẻ

### Nhược điểm 

Tốn kém vì phải có 1 máy chủ chuyên dụng yêu cầu bộ nhớ lớn 

Đòi hỏi quản trị chuyên nghiệp để quản lý tất cả tài nguyên. 




