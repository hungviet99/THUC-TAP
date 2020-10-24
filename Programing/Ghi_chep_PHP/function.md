# Hàm PHP 

PHP có hơn 1000 hàm dựng sẵn có thể được gọi trực tiếp, từ bên trong 1 tập lệnh để thực hiện tác vụ cụ thể. 

### Hàm PHP do ngừoi dùng định nghĩa 

Hàm là 1 khối các câu lệnh có thể được sử dụng nhiều lần trong 1 chương trình 

1 chức năng sẽ không thực hiện tự động khi tải trang 

Một function được thực hiện bởi 1 cuộc gọi đến chức năng

### Tạo 1 hàm do ngừoi dùng xác định trong PHP 

Một khai báo hàm do ngừoi dùng định nghĩa bắt đầu bằng từ `function`

Cú pháp: 

```
function functionName() {
  code to be executed;
}
```

### strict 

`strict` buộc mọi thứ phải được sử dụng theo cách dự định 

```
<?php declare(strict_types=1); // strict requirement

function addNumbers(int $a, int $b) {
  return $a + $b;
}
echo addNumbers(5, "5 days");

?>
```

### Khai báo kiểu cho hàm

Để khai báo kiểu cho hàm, thêm dấu hai chấm vào trước hàm và  sau đó là kiểu của hàm 

```
<?php declare(strict_types=1); 
function addNumbers(float $a, float $b) : float {
  return $a + $b;
}
echo addNumbers(1.2, 5.2);
?>
```
