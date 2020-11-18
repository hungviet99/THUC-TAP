# Ansible 

Ansible là một công cụ, phần mềm cung cấp khả năng tự động hóa đơn giản nhưng mạnh mẽ để hỗ trợ máy tính đa nền tảng, giúp giảm bớt thời gian cho các nhiệm vụ lặp đi lặp lại. Nó sử dụng chủ yếu cho những người sử dụng nó để triển khai ứng dụng, cập nhật trên máy trạm và máy chủ, quản lý cấu hình, cung cấp đám mây, điều phối dịch vụ nội bộ và gần như bất cứ điều gì mà quản trị viên hệ thống thực hiện hàng tuần hoặc hàng ngày.

Ansible được ra đời vào tháng 2 năm 2012 bởi redhad, đến nay đã được 8 năm và phiên bản ổn định gần nhất được ra đời vào tháng 10 năm 2020
### Cách Ansible hoạt động 

Trong Ansible có 2 loại máy tính là `control node` và `managed nodes`. `Control node` là một máy tính chạy Ansible, phải có ít nhất 1 `control node`. `Managed node` là bất kỳ thiết bị nào đang được quản lý bởi `control node`. 

Ansible hoạt động bằng cách kết nối các node trên mạng, sau đó gửi 1 chương trình nhỏ gọi là module ansible đến node đó. 

Ansible thực thi các module qua SSH và xóa chúng khi hoàn tất. Yêu cầu duy nhất cho tương tác này là nút điều khiển Ansible của bạn có quyền truy cập đăng nhập vào các node được quản lý. SSh key là cách phổ biển nhất để cung cấp quyền truy cập, nhưng các hình thức xác thực khác cũng được hỗ trợ, truy nhiên nó có thể không an toàn khi giao tiếp qua mạng hoặc nguy cơ lộ mật khẩu trong file inventory. 

### Use Cases

#### Cấp phép (Provisioning)

Tự động hóa, quản lý và kết nối các giai đoạn vòng đời của 1 ứng dụng. Có thể hiểu đơn giản là thiết lập 1 máy chủ sẵn sàng để được quản lý. 

`provision` -> `configure` -> `deploy` -> `manage`

#### Quản lý cấu hình (Management configuration)

Quản lý hệ thống với các tập lệnh cấu hình nhất quán, cần ít người hơn và tốn ít thời gian hơn để duy trì. 

#### Triển khai ứng dụng (App Deployment)

Triển khai ứng dụng nhất quán, tất cả đều từ 1 khuôn khổ chung

- Playbook 

    - Có thể lặp lại và tin cậy 
    - Đơn giản để viết và duy trì


#### Phân phối liên tục (Continuous Delivery)

Xây dựng phần mềm theo cách "release early, release often" - "phát hành sớm, phát hành thường xuyên".

Thường xuyên cung cấp các bản cập nhật, chỉ yêu cầu sự can thiệp của con người khi cần thiết. 

Việc chia hàng nghìn máy chủ thành các nhóm có thể quản lý và cập nhật 100 máy chủ cùng một lúc là cực kỳ đơn giản

#### Tự động hóa bảo mật (Security Automation)

Tự động hóa tích hợp các giải pháp bảo mật khác nhau, điều tra và ứng phó với các mối đe dọa trong toàn hệ thống theo cách thống nhất 

#### Điều phối  (Orchestration)

Ansible : Công cụ có thể sắp xếp các nhiệm vụ phức tạp của mình 1 cách đơn giản

Xây dựng trật tự từ sự hỗn loạn 

Tập hợp những thứ khác nhau thành 1 thể thống nhất 








