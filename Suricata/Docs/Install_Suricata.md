# Cài đặt Suricata

Suricata là một hệ thống phát hiện xâm nhập dựa trên mã nguồn mở. Nó được phát triển bởi Open Information Security Foundation (OISF). Công cụ này được phát triển không nhằm cạnh tranh hay thay thế các công tụ hiện có, nhưng nó sẽ mang lại những ý tưởng và công nghệ mới trong lĩnh vực an ninh mạng

## Cài đặt 

### Cài đặt các gói cần thiết

```
yum -y install epel-release

yum -y install jq cargo openssl-devel PyYAML lz4-devel gcc libpcap-devel pcre-devel libyaml-devel file-devel zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel tar make libnetfilter_queue-devel lua-devel wget
```

### Download suricata

- Tải về suricata từ source

```
wget https://www.openinfosecfoundation.org/download/suricata-5.0.3.tar.gz
```

- Giải nén và cài đặt suricata.

```
tar xzvf suricata-5.0.3.tar.gz
cd suricata-5.0.3
./configure --libdir=/usr/lib64 --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-lua
make install-full
```

- Kiểm tra lại phiên bản Suricata. 

```
suricata -V
```

Kết quả trả về như sau là đã thành công 

```
This is Suricata version 5.0.3 RELEASE
```

### Cấu hình Suricata

- Truy cập file cấu hình 

```
vi /etc/suricata/suricata.yaml
```

và chỉnh sửa 1 số thông tin như sau : 

```
HOME_NET: "[10.10.30.0/24, 10.10.34.0/24, 10.10.35.0/24]"
```
>Khai báo dải mạng local của bạn

```
default-rule-path: /etc/suricata/rules
rule-files:
 - suricata.rules
```

>default-rule-path: là đường dẫn đến thư mục chứa các file rules của suricata

>rule-files: khai báo các file chứa rules (nếu có nhiều file thì để nhiều dòng)

Lưu lại thay đổi và thoát. 

- Thực hiện sửa file để suricata chạy như 1 chương trình deamon

```
vi /lib/systemd/system/suricata.service
```
sau đó ghi đoạn cấu hình sau vào file: 

```
[Unit]
Description=suricata NIDS Daemon
After=syslog.target network.target

[Service]
Type=simple
ExecStart=/usr/bin/suricata -c /etc/suricata/suricata.yaml -i eth0

[Install]
WantedBy=multi-user.target
```

Chạy suricata và cho phép khởi động cùng hệ thống 

```
systemctl start suricata
systemctl enable suricata
```

### Thử 1 rule để kiểm tra hoạt động của suricata

Tạo file chứa rule và thêm 1 rule đơn giản 

```
mkdir /etc/suricata/rules
touch suricata.rules
echo 'alert icmp any any -> any any (msg: "ICMP Packet found";)' > /etc/suricata/rules/suricata.rules
```

Ở đây mình tạo file `suricata.rules` chứa rule và thêm 1 rule cảnh báo nếu phát hiện ping tới hệ thống.

Sau đó khởi động lại suricata: 

```
systemctl restart suricata
```

Sau đó ở 1 máy khác, tiến hành ping tới máy cài suricata. Tại máy suricata, kiểm tra log ta thấy đã có log ping tới hệ thống như sau là đã thành công. 

```
tail /var/log/suricata/fast.log
```

```
09/14/2020-11:34:06.756977  [**] [1:0:0] ICMP Packet found [**] [Classification: (null)] [Priority: 3] {IPv6-ICMP} fe80:0000:0000:0000:b047:62d7:3501:2366:135 -> ff02:0000:0000:0000:0000:0001:ff00:0001:0
09/14/2020-11:34:09.905913  [**] [1:0:0] ICMP Packet found [**] [Classification: (null)] [Priority: 3] {IPv6-ICMP} fe80:0000:0000:0000:b047:62d7:3501:2366:135 -> ff02:0000:0000:0000:0000:0001:ff14:acaa:0
```






