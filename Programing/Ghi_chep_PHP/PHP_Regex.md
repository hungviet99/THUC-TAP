# PHP Regex

`preg_match()` : Trả về  1 nếu kết quả được tìm thấy và trả về 0 nếu không tìm thấy. 

`preg_match_all()` : Trả về số lần mẫu được tìm thấy trong chuỗi, cũng có thể là 0

`preg_replace()`: Trả về 1 chuỗi mới trong đó các mẫu phù hợp đã được thay thế bằng 1 chuỗi khác. 


### 

- `preg_match()` 

```
<?php
$str = "Visit W3Schools";
$pattern = "/w3schools/i";
echo preg_match($pattern, $str); // Outputs 1
?>
```

- `preg_match_all()` 

```
<?php
$str = "The rain in SPAIN falls mainly on the plains.";
$pattern = "/ain/i";
echo preg_match_all($pattern, $str); // Outputs 4
?>
```

- `preg_replace()`

```
<?php
$str = "Visit Microsoft!";
$pattern = "/microsoft/i";
echo preg_replace($pattern, "W3Schools", $str); // Outputs "Visit W3Schools!"
?>
```




