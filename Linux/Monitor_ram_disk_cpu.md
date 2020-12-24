# Monitor ram, disk, cpu

## 
Xem những process tốn nhiều ram nhất (xem từ dưới lên) 

```
ps aux --sort:rss
```

hoặc xem bằng MB 

```
ps aux --sort:rss | awk 'NR>1 {$6=int($6/1024)"M";}{ print;}'
```

## fio

Lệnh `fio` thường được sử dụng để kiểm tra iops(input output per second) của ổ cứng , cho biết mỗi giây ổ cứng có thể thực hiện bao nhiêu thao tác IO. 

**Cài đặt**

```
yum install -y epel-release
yum install fio -y
```

Mình sẽ sử dụng lượng dữ liệu được ghi là 512M trên 4job nên khối lượng được ghi vào sẽ là 2G : 

**test ghi**

```
fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```
- --name chỉ định tên công việc.
- --ioengine xác định cách thức công việc tạo ra I/O
- --iodepth số tiến trình tạo ra để thực hiện công việc
- --rw=randwrite sử dụng chỉ để test việc ghi dữ liệu
- --bs kích thước blog sử dụng cho 1 đơn vị I/O Mặc định giá trị này là 4096.
- --direct nếu giá trị này là 1 thì test I/O không sử dụng vùng đệm
- --size dung lượng dữ liệu dùng để đọc hoặc ghi của 1 job
- --numjob số lượng job
- --runtime thời gian tối đa để chạy lệnh này
- --group_reporting nhóm kết quả các job thành một báo cáo

Kết quả đầu ra như sau : 

![Imgur](https://i.imgur.com/3l1jGC5.png)

1. IOPS : là số lần thực hiện thao tác IO trong 1 giây

2. BW : Tốc độ đọc trung bình 
3. Dung lượng thực hiện io trên giây

**test đọc**

```
fio --name=randread --ioengine=libaio --iodepth=1 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

![Imgur](https://i.imgur.com/0LQ6Yor.png)

**Test đọc và ghi**

```
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
```

![Imgur](https://i.imgur.com/sW6HrvD.png)


## dd command 

Kiểm tra tốc độ ghi disk

```
dd if=/dev/zero of=test01 bs=1M count=1024 conv=fdatasync
```

Kiểm tra tốc độ ghi ram 

```
dd if=/dev/zero of=test01 bs=1M count=1024
```

