# PHP Constants

Hằng số là 1 định danh (tên) cho 1 giá trị đơn giản. Giá trị không thể thay đổi trong tập lệnh 

Tên hằng hợp lệ bắt đầu bằng 1 chữ cái hoặc dấu gạch dưới, không có dấu $ trước tên hằng 

Không giống như biến, hằng số tự động toàn cục trên toàn bộ tập lệnh 

## Create a PHP Constant

Để tạo 1 hằng, sử dụng function `define()`

**Cú Pháp :**

```
define(name, value, case-insensitive)
```

- `name` : Tên hằng

- `value` : Giá trị của hằng 

- `case-insensitive` : Chỉ định xem tên hằng có phân biệt chữ hoa chữ thường hay không. Nếu có phân biệt thì k điền giá trị nầy, nếu không phân biệt sử dụng `True` 


Tạo hằng với tên phân biệt chữ hoa chữ thường 

```
<?php
define("NAME", "Nguyễn Việt Hùng");
echo NAME;
?>
```

Tạo hằng với tên không phân biệt chữ hoa chữ thường 

```
<?php
define("NAME", "Nguyễn Việt Hùng", true);
echo name;
?>
```

## PHP Constant Arrays 

Trong php 7, bạn có thể tạo hằng số và gán hằng số cho mảng 

```
<?php
define("cars", [
  "Alfa Romeo",
  "BMW",
  "Toyota"
]);
echo cars[0];
?>
```

## Constants are Global 

Các hằng số tự động là global và có thể được sử dụng trên toàn bộ tập lệnh 

```
<?php
define("NAME", "Nguyễn Việt Hùng");

function myTest() {
  echo NAME;
}
 
myTest();
?>
```
