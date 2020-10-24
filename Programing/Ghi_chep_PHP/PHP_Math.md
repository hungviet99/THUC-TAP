# PHP Math 

PHP có 1 tập hợp các hàm toán học cho phép bạn thực hiện các nhiệm vụ toán học trên các số

## PHP pi() Function

The pi() function returns the value of PI: 

```
<?php
echo(pi()); // returns 3.1415926535898
?>
```

## PHP min() and max() Functions 

`min()` và `max()` được sử dụng để tìm giá trị lớn nhất hoặc nhỏ nhất trong 1 chuỗi 

```
<?php
echo(min(0, 150, 30, 20, -8, -200));  // returns -200
echo(max(0, 150, 30, 20, -8, -200));  // returns 150
?>
```

## PHP abs() Function

Hàm `abs()` trả về giá trị tuyệt đối của 1 số

```
<?php
echo(abs(-6.7));  // returns 6.7
?>
```

## PHP sqrt() Function

Hàm `sqrt()` trả về căn bậc 2 của 1 số : 

```
<?php
echo(sqrt(16));  // returns 4
?>
```

## PHP round() Function

Hàm `round()` trả về số nguyên gần nhất của float 

```
<?php
echo(round(0.49));  // returns 0
echo(round(0.51));  // returns 1
?>
```

## Random Number 

Hàm `rand()` tạo ra 1 số ngẫu nhiên 

```
<?php
echo(rand());
?>
```

Ta có thể chỉ định khoảng số bằng cách thêm 1 số tối thiểu và 1 số tối đa. 

```
<?php
echo(rand(1, 10));
?>
```


