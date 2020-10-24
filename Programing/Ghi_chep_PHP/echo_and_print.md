# Echo/Print

Có 2 cách để xuất dữ liệu ra màn hình trong PHP là `echo` and `print` 

`echo` không có giá trị trả về tỏng khi `print` có giá trị trả về là 1 nên có thể sử dụng trong biểu thức 

## PHP echo 

Câu lệnh echo có thể được sử dụng có hoặc không có dấu ngoặc đơn : `echo` hoặc `echo()` 

Cách xuất văn bản bằng echo (có thể chứa HTML): 

```
<?php
echo "<h2>PHP is Fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
?>
```

Cách xuất văn bản và các biến bằng lệnh echo

```
<?php
$txt1 = "Learn PHP";
$txt2 = "Nguyen Viet Hung";
$x = 5;
$y = 4;

echo "<h2>" . $txt1 . "</h2>";
echo "Study PHP " . $txt2 . "<br>";
echo $x + $y;
?>
```

## Print

Lệnh print có thể sử dụng có hoặc không có dấu ngoặc đơn : `print` hoặc `print()`

Cách xuất văn bản bằng print : 

```
<?php
print "<h2>PHP is Fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";
?>
```

Cách xuất văn bản và các biến bằng lệnh print

```
<?php
$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";
$x = 5;
$y = 4;

print "<h2>" . $txt1 . "</h2>";
print "Study PHP at " . $txt2 . "<br>";
print $x + $y;
?>
```

