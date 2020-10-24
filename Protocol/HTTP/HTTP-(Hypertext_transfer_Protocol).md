# HTTP (Hypertext transfer Protocol)

HTTP là 1 giao thức truyền siêu văn bản, HTTP đã được sử dụng bởi sáng kiến thông tin toàn cầu từ năm 1990. Phiên bản đầu tiên của HTTP là HTTP/0.9 là 1 giao thức đơn giản để truyền dữ liệu thô trên internet

HTTP/1.0 được định nghĩa bởi RFC-1945 

HTTP/1.1 được ghi nhận trong RFC 2068 lần đầu tiên vào năm 1997, đặc điểm kỹ thuật lỗi thời bỏi RFC 2616 năm 1999. Giao thức này nghiêm ngặt hơn HTTP/1.0 để đảm bảo thực hiện đáng tin cậy các tính năng của nó. 

## Hoạt động 

Giao thức HTTP là 1 giao thức `request`/`response`. Phía Client gửi yêu cầu đến máy chủ dưới dạng phương thức request, máy chủ phản hồi với 1 dòng trạng thái (response). 

### HTTP - requests
 
Là phương thức để chỉ ra hành động mong muốn được thực hiện trên tài nguyên đã xác định. Cấu trúc của 1 HTTP Request: 

- 1 requests-line = method + URI-Request + HTTP version. Giao thức HTTP định nghĩa 1 tập các phương thức GET, POST, HEAD, PUT ... Client có thể sử dụng 1 trong các phương thức đó để gửi requests lên server. 

Hầu hết các giao tiếp http được bắt đầu bởi 1 tác nhân người dùng và bao gồm 1 yêu cầu được áp dụng cho tài nguyên trên 1 số máy chủ gốc.  

