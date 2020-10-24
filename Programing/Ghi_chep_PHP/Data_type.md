# Data type

PHP có hỗ trợ các kiểu dữ liệu sau : 

```
String
Integer
Float (floating point numbers - also called double)
Boolean
Array
Object
NULL
Resource
```

### PHP String 

```
<?php
$x = "Hello world!";
$y = 'Hello world!';

echo $x;
echo "<br>";
echo $y;
?>
```

### PHP integer 

Một số nguyên phải có ít nhất 1 chữ số 

Một số nguyên không được có dấu thập phân 

Một số nguyên có thể là dương hoặc âm 

Hàm `var_dump()` trả về kiểu giá trị và giá trị dữ liệu 

```
<?php
$x = 5985;
var_dump($x);
?>
```

### PHP Float

Là 1 số có dấu thập phân hoặc số ở dạng hàm mũ 

### PHP Boolean

Boolean trả về 2 giá trị true hoặc false


### PHP Array

Một mảng lưu trữ nhiều giá trị trong một biến duy nhất.

```
<?php  
$cars = array("Volvo","BMW","Toyota");
var_dump($cars);
?>  
```

### PHP Object

Là 1 kiểu dữ liệu lưu trữ dữ liệu và thông tin về cách xử lý dữ liệu đó 

Trong php,  1 đối tượng phải được khai báo rõ ràng 

Đầu tiên ta khai báo 1 đối tượng , với điều này chúng tôi sử dụng từ khóa class. Class là 1 cấu trúc có thể chứa các thuộc tính và phương thức 

```
<?php
class Car {
  function Car() {
    $this->model = "VW";
  }
}

// create an object
$herbie = new Car();

// show object properties
echo $herbie->model;
?>
```

