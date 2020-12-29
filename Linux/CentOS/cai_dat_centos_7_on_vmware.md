# Cài CentOS 7 trên máy ảo Vmware

Trước tiên ta [download](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso) **Centos7**

### Cài Centos7 trên máy ảo vmware

<img src="https://i.imgur.com/v9LJtac.png">

**Chọn *Typical (recommended)* => *Next***

<img src="https://i.imgur.com/9efqPYA.png">

***Installer disc image file iso*. Chọn *Browser* sau đó tìm đến ổ lưu file iso Centos7**

<img src="https://i.imgur.com/8sVWNx1.png">

**Đặt tên cho máy ảo và chọn vị trí cài đặt**

<img src="https://i.imgur.com/e6FJiu5.png">

**Tiếp theo ta chỉ định dung lượng ổ cứng cấp cho Centos7. `Next`** 

<img src="https://i.imgur.com/a6UXkbn.png">

**Finish**

<img src="https://i.imgur.com/kGEv24O.png">

**Ta có thể chỉnh dung lượng *RAM* cấp cho CentOS7:**

**Chọn `Edit virtual machine settings`**

<img src="https://i.imgur.com/IjNtHM6.png">

**Chọn `Memory` sau đó chọn dung lượng ram cho *CentOS7*, ở đây nên đặt là 1GB nếu máy có ram 4GB trở xuống.**

<img src="https://i.imgur.com/jd28Kr6.png">

**Bắt đầu cài đặt :**

<img src="https://i.imgur.com/svcdMe3.png">

<img src="https://i.imgur.com/u3sAmJ2.png">

**Giao diện cấu hình Date & Time , Language , Network & Hostname , Installation Destination , Software Selection**

<img src="https://i.imgur.com/yflZiOz.png">

**Đặt ngày, giờ và click *Done***

<img src="https://i.imgur.com/OTnY8lQ.png">

**Click `Installation Destination` , chọn đĩa cứng và tích `I will configure Partitioning`**

<img src="https://i.imgur.com/CIMiL3H.png">

**Màn hình cấu hình phân vùng đĩa cứng hiện lên, tích vào dấu + để thêm phân vùng đĩa.**

<img src="https://i.imgur.com/EjnAc7b.png">

mình thêm 3 phân vùng là /boot để dành cho phần khởi động, / là nơi chứa toàn bộ dữ liệu máy chủ và phân vùng swap để làm bộ nhớ trao đổi.

<img src="https://i.imgur.com/LPwom7q.png">

<img src="https://i.imgur.com/G625Y5f.png">
Ta cũng có thể phân vùng swap sau khi cài đặt xong với quyền root.

**Trở lại trang bắt đầu và click `Begin Installation`**

<img src="https://i.imgur.com/9qrG73z.png">  

 
**Quá trình cài đặt bắt đầu. Ta đặt `Password` cho `Root` và tạo `User`**  


<img src="https://i.imgur.com/ig56Hyw.png">

Đợi 1 lát..

**`Reboot now`**

<img src="https://i.imgur.com/vEkG5wb.png">

**Nhập tài khoản mật khẩu mới tạo để đăng nhập, như vậy là đã thành công.**

<img src="https://i.imgur.com/HiiYS1J.png">

**Kiểm tra phân vùng đĩa và vùng trao đổi**

<img src="https://i.imgur.com/0KvHRVx.png">

> **Note:** RAM (Random Access Memory):bộ nhớ truy cập ngẫu nhiên: Khi mở một phần mềm thì dữ liệu sẽ được truyền tải từ ổ đĩa cứng lên RAM và truyền tải vào CPU để xử lý, sau đó lưu ngược lại vào ổ cứng vì RAM có tốc độ rất nhanh hơn rất nhiều lần so với ổ cứng. RAM không thể lưu trữ được dữ liệu khi ngừng cung cấp nguồn cho nó, tức là khi tắt máy dữ liệu trên Ram sẽ bị xóa sạch  
ROM (Read Only Memory): bộ nhớ chỉ đọc : là 1 loại phương tiện lưu trữ vĩnh viễn dữ liệu trên máy tính hoặc các thiết bị điện tử, khi bị ngắtt điện, dữ liệu vẫn giữ nguyên không hề thay đổi hay mất đi.