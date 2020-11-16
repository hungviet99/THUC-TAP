# Ansible 

Ansible là một công cụ, phần mềm cung cấp khả năng tự động hóa đơn giản nhưng mạnh mẽ để hỗ trợ máy tính đa nền tảng. Nó sử dụng chủ yếu cho những người sử dụng nó để triển khai ứng dụng, cập nhật trên máy trạm và máy chủ, quản láy cấu hình, cung cấp đám mây, điều phối dịch vụ nội bộ và gần như bất cứ điều gì mà quản trị viên hệ thống thực hiện hàng tuần hoặc hàng ngày. 

### Cách Ansible hoạt động 

Trong Ansible có 2 loại máy tính là `control node` và `managed nodes`. `Control node` là một máy tính chạy Ansible, phải có ít nhất 1 `control node`. `Managed node` là bất kỳ thiết bị nào đang được quản lý bởi `control node`. 

Ansible hoạt động bằng cách kết nối các node trên mạng, sau đó gửi 1 chương trình nhỏ gọi là module ansible đến node đó. 

Ansible thực thi các module qua SSH và xóa chúng khi hoàn tất. Yêu cầu duy nhất cho tương tác này là nút điều khiển Ansible của bạn có quyền truy cập đăng nhập vào các node được quản lý. SSh key là cách phổ biển nhất để cung cấp quyền truy cập, nhưng các hình thức xác thực khác cũng được hỗ trợ, truy nhiên nó có thể không an toàn khi giao tiếp qua mạng hoặc nguy cơ lộ mật khẩu trong file inventory. 



