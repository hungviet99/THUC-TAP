# Ansible concepts

## Inventory

Danh sách các node được quản lý, nó được lưu trong file `hosts`. Trong file inventory, bạn có thể chỉ định thông tin như địa chỉ IP của mỗi node được quản lý,.. Inventory cũng có thể tổ chức các node được quản lý như tạo và lồng các node được quản lý vào các nhóm để mở rộng quy mô dễ dàng hơn. 

Vị trí mặc định cho inventory là 1 file có tên `/etc/ansible/hosts`. 

## Collections

Collections là 1 định dạng phân phối cho nội dung Ansible có thể bao gồm playbooks, roles, modules và plugins. Bạn có thể cài đặt và sử dụng collection thông qua Ansible Galaxy.

## Modules

Mỗi module có 1 mục đích sử dụng cụ thể, từ quản lý người dùng trên 1 loại cơ sở dữ liệu cụ thể đến quản lý các giao diện VLAN trên 1 loại thiết bị mạng cụ thể. Bạn có thể gọi 1 module với 1 nhiệm vụ hoặc gọi nhiều module khác nhau trong 1 playbook. 

## Task 

Các đơn vị hành động trong ansible. Bạn có thể thực thi 1 nhiệm vụ duy nhất bằng cách sử dụng `ad-hoc command`. 

## Playbooks

Danh sách nhiệm vụ có thứ tự, được lưu để chạu các tác vụ theo thứ tự đó nhiều lần. Playbook có thể bao gồm các biến cũng như các nhiệm vụ. 

## Ansible Role

Ansible role được sử dụng để đơn giản hóa playbook. Nghĩa là khi ta làm việc với Ansible playbook, ta có thể dễ dàng phân chia các nhiệm vụ thành các vai trò khác nhau. Ngoài ra, những vai trò này có thể được sử dụng lại trong tương lai.

Khi tạo ra 1 role, sẽ có các thư mục tương ứng được tạo ra như: `defaults`, `handlers`, `meta`, `molecule`, `tasks`, `templates`, `vars`

Chức năng của từng thư mục role:

- `tasks`: danh sách các nhiệm vụ chính mà vai trò thực thi. 

- `handlers`: trình xử lý, có thể được sử dụng trong hoặc ngoài role

- `defaults`: các biến mặc định cho role, các biến này có độ ưu tiên thấp nhất trong số các biến có sẵn, và có thể dễ dàng bị ghi đè bởi bất kỳ biến nào khác, bao gồm các biến inventory

- `vars`: Nó lưu trữ các biến được sử dụng trong các vai trò. Nó có mức độ ưu tiên cao nhất và chúng ta chỉ có thể ghi đè bằng cách chuyển các biến qua CLi. Nó cũng có 1 file `main.yml`

- `templates`: Nó chứa các mẫu mà ta có thể triển khai thông qua vai trò này. Nó không có file `main.yml`

- `meta`: Siêu dữ liệu cho role, bao gồm cả phần phụ thuộc role. 

