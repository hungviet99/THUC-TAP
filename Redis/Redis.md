# Redis (Remote Dictionary Server)

Redis là kho lưu trữ dữ liệu dạng key-value trong RAM. Nó được sử dụng để xây dựng các web app có performance và khả năng scalable cao. 

Redis sử dụng các cấu trúc dữ liệu như `String`, `List`, `hashes`, `sets`, `bitmaps`, `hyperloglogs`. 

## Các đặc điểm của redis :

là 1 loại in-memory storage, tức là toàn bộ database của nó được lưu tại RAM.
Vì dữ liệu của redis được lưu tại ram nên khi truy xuất có thể tránh được sự chậm trễ do thời gian tìm kiếm.

- Số lượng data type được định nghĩa trong Redis nhiều hơn so với các loại key-value storage khác

  - String: văn bản hoặc dữ liệu nhị phân có kích thước lên tới 512MB.

  - List: tập hợp các String được sắp xếp theo thứ tự như khi được thêm vào.

  - Set: tập hợp chưa được sắp xếp.

  - ZSet: tập hợp được sắp xếp theo giá trị.

  - Hashes: cấu trúc dữ liệu dùng để lưu trữ danh sách theo key-value.

  - Bitmap: kiểu dữ liệu cho phép thực hiện các tác vụ quy mô bit.

  - HyperLogLogs: cấu trúc dữ liệu xác suất để ước tính các thành phần duy nhất trong một tập dữ liệu.

Redis có thể sao chép data sang nhiều slaves khác nhau.

Redis có thể cấu hình theo dạng Cluster với kỹ thuật Master-Slave giúp hệ thống redis luôn sẵn sàng đáp ứng

- Kiến trúc master-slave trên redis

`Master Node` : Tiến trình chính, chạy và xử lý các kết nối với client

`Slave Node` : Tiến trình phụ, chayỵ cùng tiến trình chính và giám sát tiến trình chính. Tiến trình phụ cũng thực hiện việc ghi, dump dữ liệu định kỳ vào ổ cứng để backup.

Vì tất cả các Redis Slave đang có tập dữ liệu mới nhất (bằng cách sao chép từ Redis Master), nếu bất kỳ Redis Slave nào gặp sự cố, các Redis Slave khác sẽ phục vụ các yêu cầu đọc.

> Lưu ý: Theo mặc định mỗi máy bạn có Redis là Redis Master, bạn phải thay đổi vai trò của máy redis thành Slave bằng cách sử dụng lệnh 'slaveof'.

## Các tính năng chính 

- Hiệu suất cao :

Nó có thể xử lý hơn 120000 yêu cầu mỗi giây 

- Dễ sử dụng: 

Nó rất dễ sử dụng, dữ liệu có thể được lưu trữ bằng lệnh `SET` và có thể được truy xuất bằng lệnh `GET`. 

- Tính khả dụng cao: 

Nó hỗ trợ sao chép master/slave để đảm bảo dữ liệu có sẵn cao 

- Hỗ trợ nhiều ngôn ngữ:

Redis hỗ  trợ các ngôn ngữ như Python, JavaScript 

Redis thường được sử dụng cùng với các cơ sở dữ liệu khác. Các yêu cầu thường xuyên được lưu trữ trong bộ nhớ cache, từ đó khi truy vấn sẽ giảm được thời gian truy vấn vì nó tránh được truy vấn xuống cơ sở dữ liệu.

## Một số công ty nổi tiếng cũng sử dụng Redis như : 

- Snapchat

- Twitter

- Weibo

- GitHub