# Ansible vault 

## Giới thiệu 

Ansible Vault là 1 tính năng cho phép người dùng mã hóa các giá trị và cấu trúc dữ liệu trong các dự án Ansible. Điều này có khả năng bảo mật mọi dữ liệu nhạy cảm cần thiết để chạy các playbook ansible. Ansible tự động giải mã nội dung được mã hóa vault trong thời gian chạy khi khóa được cung cấp. 

Mỗi tệp mã hóa liên quan đến nhau phải cùng chung 1 mật khẩu. 

## Quản lý các file được mã hóa với Ansible Vault 

### Tạo file mã hóa mới 

```
ansible-vault create hungnv.yml
```

Ta sẽ nhận được nhắc nhập và xác nhận mật khẩu: 

Output
```
New Vault password:
Confirm New Vault password:
```

Sau đó ghi một nội dung ngắn vào file

```
Secret information
```

Sau đó sử dụng cat để xem nội dung đã được mã hóa hay chưa. 

```
cat vault.yml
```

Output
```
$ANSIBLE_VAULT;1.1;AES256
30633039356430363334336666396130323735366433353637303666323761366231326537643732
3164623239326634653765653164326266306634396563620a666139376561383361363666303439
33346661386666626137303061393431313266373865376635323365376139396537396662636432
6130386266656133630a393861353137316230393761303161316363626133393435393063653932
34646466323338356466616339303166613164343265306333653435666132653462
```

### Sửa file mã hóa 

```
ansible-vault edit hungnv.yml
```

Tiếp theo nhập vào mật khẩu: 

Output
```
Vault password:
```

### Xem file mã hóa 

```
ansible-vault view hungnv.yml
```

### Bỏ mã hóa 

```
ansible-vault decrypt hungnv.yml
```
Sau đó nhập vào mật khẩu : 

Output
```
Vault password:
```

Khi nhập đúng sẽ có thông báo trả về `Decryption successful`

## Chạy playbook với các file được mã hóa 

Nếu có nhiều hơn 1 file được mã hóa trong playbook, các file đó phải có chung 1 mật khẩu. 

Ví dụ mình có file `host` và file `playbook.yml` đều được mã hóa, cú pháp chạy playbook của mình như sau: 

Sử dụng `--ask-vault-pass` để cho phép nhập mật khẩu các file mã hóa khi chạy playbook.

```
ansible-playbook --ask-vault-pass -i hosts playbook.yml
```
