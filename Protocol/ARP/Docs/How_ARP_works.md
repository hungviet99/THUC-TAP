# Address Resolution Protocol - ARP 

Hầu hết các chương trình máy tính sử dụng địa chỉ IP để gửi/nhận tin nhắn. Tuy nhiên, việc truyền/nhận thực tế xảy ra qua địa chỉ vật lý(MAC). 

Tất cả các hệ điều hành trong mạng đều giữ một bộ nhó cache ARP. Mỗi khi một máy chủ yêu cầu địa chỉ MAC để gửi 1 gói tin đến một máy chủ khác trong mạng LAN, nó sẽ kiểm tra bộ nhớ cache ARP của nó để xem bản dịch địa chỉ IP sang MAC đã tồn tại hay chưa. Nếu có, thì không cần thực hiện yêu cầu mới. Nếu không tồn tại bản ghi giữa địa chỉ IP và địa chỉ MAC đó thì sẽ có 1 yêu cầu được đưa ra và ARP sẽ được thực hiện. 

ARP phát 1 yêu cầu tới tất cả các máy trong mạng LAN và hỏi xem có máy nào biết chúng đang sử dụng địa chỉ IP cụ thể đó không. Khi một máy nhận ra địa chỉ IP là của mình, nó sẽ gwuri trả lời để ARP cập nhật vào bộ nhớ cahe địa chỉ MAC ứng với địa chỉ IP đó để sử dụng cho tương lai và tiếp tục giao tiếp.

whatis-arp_desktop.png
![](./image/whatis-arp_desktop.png)
