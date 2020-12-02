# Ansible user guide

## Các công cụ dòng lệnh Ansible

### ansible

Là 1 cộng cụ đơn giản để thực hiện các công việc từ xa. Lệnh này cho phép xác định và chạy 1 tác vụ duy nhất dựa trên 1 tập các máy chủ.

Cú pháp: 

```
ansible <host-pattern> [options]
```

### ansible-config

Cú pháp: 

```
ansible-config [view|dump|list] [--help] [options] [ansible.cfg]
```

### ansible-console

Cú pháp: 

```
ansible-console [<host-pattern>] [options]
```

### ansible-doc

Ansible-doc hiển thị thông tin về các modul được cài đặt trong thư viện ansible. Nó hiển thị danh sách ngắn gọn về các plugin và mô tả ngắn của chúng, có thể tạo 1 đoạn ngắn có thể dán vào playbook.

Cú pháp: 

```
ansible-doc [-l|-F|-s] [options] [-t <plugin type> ] [plugin]
```

### ansible-galaxy

Lệnh ansible-galaxy quản lý các vai trò Ansible trong kho lưu trữ được chia sẻ, mặc định là Ansible Galaxy https://galaxy.ansible.com

Cú pháp:

```
ansible-galaxy [delete|import|info|init|install|list|login|remove|search|setup] [--help] [options] ...
```

### ansible-inventory

Lệnh được sử dụng để hiển thị hoặc kết xuất khoảng không quảng cáo đã định cấu hình khi Ansible nhìn thấy nó.

Cú pháp: 

```
ansible-inventory [options] [host|group]
```

### ansible-playbook

Lệnh sử dụng để chạy các playbook ansible. 

Cú pháp: 

```
ansible-playbook [options] playbook.yml [playbook2 ...]
```

### ansible-pull

Cú pháp: 

```
ansible-pull -U <repository> [options] [<playbook.yml>]
```

### ansible-vault

Sử dụng để mã hóa bất kỳ tệp dữ liệu có cấu trúc nào được Ansible sử dụng. 

Cú pháp: 

```
ansible-vault [create|decrypt|edit|encrypt|encrypt_string|rekey|view] [options] [vaultfile.yml]
```

## Ad-Hoc

Ad-Hoc command cho phép ta thực hiện các task đơn, các yêu cầu độc lập đến các máy được quản lý. 

Nó giúp thực hiện nhanh, thực hiện hàng loạt các tác vụ như khởi động os, khởi động hoặc stop các dịch vụ, kiểm tra trạng thái của các dịch vụ, xem nội dung file hoặc cây thư mục.. trên các máy chủ được quản lý. 

### Chuyển tập tin 

```
ansible managed_node -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

### Quản lý các gói 

Cài đặt nhưng không cập nhật gói `packets`

```
ansible managed_node -m yum -a "name=packets state=present"
```

Cài đặt gói `packets` ở phiên bản mới nhất 

```
ansible managed_node -m yum -a "name=packets state=latest"
```

Gỡ cài đặt gói `packets`

```
ansible managed_node -m yum -a "name=packets state=absent"
```

### User và Group 

modul user cho phép dễ dàng tạo và thao tác các tài khoản người dùng hiện có, cũng như xóa các tài khoản người dùng đang tồn tại 

```
ansible all -m user -a "name=foo password=<crypted password here>"
```

```
ansible all -m user -a "name=foo state=absent"
```

### Quản lý dịch vụ 

Khởi động dịch vụ 

```
ansible webservers -m service -a "name=httpd state=started"
```

Khởi động lại dịch vụ 

```
ansible webservers -m service -a "name=httpd state=restarted"
```

Stop dịch vụ 

```
ansible webservers -m service -a "name=httpd state=stopped"
```

### Thu thập dữ liệu 

Lấy các thông tin về hệ thống của bạn 

```
ansible all -m setup
```

## Làm việc với Inventory 

Vị trí file inventory mặc định `/etc/ansible/hosts`. 

Ví dụ dưới đây cho thấy cách tổ chức các host trong file inventory

```
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```

- Các tiêu đề trong `[]` là tên nhóm, được sử dụng để phân loại hệ thống và quyết định hệ thống của bạn đang kiểm soát vào thời điểm nào và cho mục đích gì. 


Có thể chỉ định loại kết nối và người dùng: 

```
[webservers]

other1.example.com     ansible_connection=ssh        ansible_user=root
other2.example.com     ansible_connection=ssh        ansible_user=user1
```

Sử dụng var để đặt biến cho nhóm, các biến nhóm được áp dụng cho tất cả các nhóm cùng 1 lúc. Đây là 1 các thuận tiện để áp dụng cho nhiều máy chủ cùng 1 lúc.

```
[atlanta]
host1
host2

[atlanta:vars]
ntp_server=ntp.atlanta.example.com
proxy=proxy.atlanta.example.com
```

### Nhóm mặc định 

Có 2 nhóm mặc định là: `all` và `ungrouped`. `all` chứa tất cả các máy chủ còn `ungrouped` chứa tất cả các máy chủ không thuộc group nào. 


## Playbook

Playbook là ngôn ngữ cấu hình, triển khai và điều phối Ansible. Chúng có thể mô tả chính sách mà bạn muốn hệ thống của mình thực thi hoặc 1 tập các bước trong quy trình công nghệ thông tin. 

Ở mức độ cơ bản, playbook có thể được sử dụng để quản lý cấu hình và triển khai cho các máy từ xa.

### Ví dụ về playbook

Playbook được thể hiện ở định dạng YAML, là 1 mô hình cấu hình hoặc 1 quy trình. 

```
---
- hosts: webservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: root
  tasks:
  - name: ensure apache is at the latest version
    yum:
      name: httpd
      state: latest
  - name: write the apache config file
    template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf
    notify:
    - restart apache
  - name: ensure apache is running
    service:
      name: httpd
      state: started
  handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```

Playbook có thể chứa nhiều plays. 
