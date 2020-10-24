# PHP String 

String là 1 chuỗi các ký tự, như "Xin Chào" 

Một số hàm thường được sử dụng để thao tác chuỗi 

- `strlen()` - trả về độ dài của chuỗi 

```
<?php
echo strlen("Hello world!"); 
?>
```

- `str_word_count()` - Đếm số từ trong 1 chuỗi 

```
<?php
echo str_word_count("Hello world!"); // outputs 2
?>
```

- `strrev()` Trả về 1 chuỗi đảo ngược 

```
<?php
echo strrev("Hello world!"); // outputs !dlrow olleH
?>
```

- `strppos()` - Tìm kiếm 1 văn bản trong 1 chuỗi 

Nếu 1 văn bản được tìm thấy, nó sẽ trả về vị trí ký tự đầu tiên của văn bản đó trong chuỗi

```
<?php
echo strpos("Hello world!", "world"); // outputs 6
?>
``` 

- str_replace() - Thay thế văn bản trong 1 chuỗi 

Hàm thay thế 1 số ký tự bằng 1 số ký tự khác trong chuỗi 

```
<?php
echo str_replace("world", "Dolly", "Hello world!"); // outputs Hello Dolly!
?>
```
