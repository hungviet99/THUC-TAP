# PHP Numbers 

Tìm hiểu về Integers, Floats, and Number Strings

## PHP Numbers

PHP nó cung cấp chuyển đổi kiểu dữ liệu tự động 

Nếu gán giá trị nguyên cho 1 biến, nó sẽ tự động là 1 số nguyên. Sau đó, nếu gán 1 chuỗi cho cùng 1 biến, biến đó sẽ thay đổi thành string 

## PHP Integers

Một số nguyên là 1 số không có phần thập phân 

Giới hạn số nguyên trong khoảng `-2147483648` đến `2147483647`, giá trị nhỏ hơn hoặc lớn hơn trong khoảng này được coi là float.

Nếu 1 biến là số nguyên và 1 biến float nhân với nhau ra số nguyên thì nó vẫn nhận là float vì 1 trong các toán hạng là float. VD: 4 * 2,5 = 10 

Một số quy tắc : 

- 1 số nguyên phải có ít nhất 1 chữ số 

- Một số nguyên không được có dấu thập phân 

- 1 số nguyên có thể là dương hoặc âm 

- 1 Số nguyên có thể được chỉ định theo 3 định dạng : Thập phân , thập lục phân hoặc bát phân 

- PHP có các hàm sau để kiểm tra xem loại biến có phải số nguyên hay không 

```
is_int()
is_integer() - alias of is_int()
is_long() - alias of is_int()
```

VD: 

```
<?php  
$x = 5985;
var_dump(is_long($x));

echo "<br>";

$y = 59.5;
var_dump(is_int($y));

echo "<br>";

$z = 5.5;
var_dump(is_integer($z));

echo "<br>";

$t = 59;
var_dump(is_int($t));
?>   
```

## PHP Floats 

Float là 1 số có dấu thập phân hoặc số ở dạng số mũ 

Kiểu float thường có thể lưu giá trị lên tới 1.7976931348623E+308, có độ chính xác tối đa là 14 số 

PHp dùng các hàm sau để kiểm tra xem biến có phải float hay không

```
is_float()
is_double()
```

### PHP Infinity 

Giá trị số lớn hơn `PHP_FLOAT_MAX` được coi là vô hạn 

PHP sử dụng các hàm sau để kiểm tra xem nó là hữu hạn hay vô hạn : 

```
is_finite()
is_infinite()
```

### PHP NaN

NaN là viết tắt của Not a Number

Để kiểm tra giá trị không phải số, ta sử dụng hàm sau : `is_nan()`

### PHP Numerical Strings 

Hàm `is_numeric()` kiểm tra 1 biến có phải là số hay không. Nếu là số thì trả về true, nếu không phải số sẽ trả về fail 

### Ép kiểu 
`int` hoặc `integer` hoặc `intval` dùng để chuyển đổi 1 giá trị thành số nguyên. 


```
<?php
// Cast float to int 
$x = 23465.768;
$int_st = (int)$x;
echo $int_st;
  
echo "<br>";

// Cast string to int
$x = "23465.768";
$int_cast = (int)$x;
echo $int_cast;
?>  
```
