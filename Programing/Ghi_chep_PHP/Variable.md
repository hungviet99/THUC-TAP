# Biến trong PHP 

### Biến đầu vào 

Biến trong php bắt đầu bằng dấu `$`, theo sau là tên của biến 

Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới

Một tên biến không thể bắt đầu bằng một số

Tên biến chỉ có thể chứa các ký tự chữ và số dưới (Az, 0-9 và _)

Tên biến là phân biệt chữ hoa chữ thường ( $agevà $AGElà hai biến khác nhau)

**Lưu ý**: Khi gán văn bản cho 1 biến phải có dấu ngoặc kép mở và đóng cho đoạn văn bản đó. 

php không có lệnh khai báo 1 biến,  nó được tạo ngay khi gán giá trị cho nó. 

Một biến có thể có một tên ngắn (như x và y) hoặc một tên mô tả nhiều hơn (tuổi, carname, Total_volume).

### Biến đầu ra 

trong php, `echo` được sử dụng để xuất dữ liệu ra màn hình 

vd : 

```
<?php
$txt = "W3Schools.com";
echo "I love $txt!";
?>
```
hoặc 

```
<?php
$txt = "W3Schools.com";
echo "I love " . $txt . "!";
?>
```

tổng 2 biến 

```
<?php
$x = 5;
$y = 4;
echo $x + $y;
?>
```

### Phạm vi biến PHP 

php có 3 phạm vi biến đó là : 

- local

- global

- static

Biến bên ngoài hàm có phạm vi toàn câu và chỉ có thể truy cập bên ngoài hàm  

1 Biến khai báo bên trong hàm có phạm vi local và chỉ có thể truy cập bên trong hàm đó 

Để biến toàn cầu có thể được truy cập bên trong hàm, hãy sử dụng global. 

Ví dụ : 

```
<?php
$x = 5;
$y = 10;

function myTest() {
  global $x, $y;
  $y = $x + $y;
} 
```

Hoặc có thể sử dụng biến toàn cục lưu trong 1 mảng `$GLOBALS[index]` , có thể sử dụng mảng để cập nhật các biến toàn cục trực tiếp 

Ví dụ : 

```
<?php
$x = 5;
$y = 10;

function myTest() {
  $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
}

myTest();
echo $y; // outputs 15
?>
```

