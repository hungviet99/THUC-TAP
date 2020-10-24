# Bài tập ngày 3

1. Khai báo tuổi của bạn dưới dạng biến số nguyên

```
age = int(22)
```

2. Khai báo chiều cao của bạn dưới dạng biến float

```
height = float(1.68)
```

3. Khai báo một biến số phức

```
variable = complex(1, -2)
```

4. Viết tập lệnh nhắc người dùng nhập `base` và `hight` của tam giác và tính diện tích của tam giác này (diện tích = 0,5 x b x h).

```
base = int(input("Nhap base: "))
hight = int(input("Nhap hight: "))
print("Dien tich: ", 0.5 * base * hight)
```

5. Viết một tập lệnh nhắc người dùng nhập cạnh a, cạnh b và cạnh c của tam giác. Tính chu vi hình tam giác (chu vi = a + b + c).

```
a = int(input("Nhap canh thu 1: "))
b = int(input("Nhap canh thu 2: "))
c = int(input("Nhap canh thu 3: "))
print ("chu_vi: ", a + b + c)
```

6. Nhận chiều dài và chiều rộng của một hình chữ nhật bằng cách sử dụng dấu nhắc. Tính diện tích của nó (diện tích = dài x rộng) và chu vi (chu vi = 2 x (dài + rộng))

```
length = int(input("Nhap chieu dai: "))
width = int(input("Nhap chieu rong: "))
print("Dien tich6: ", length * width)
print("Chu vi 6: ", 2 * (length + width))
```

7. Nhận bán kính của hình tròn bằng lời nhắc. Tính diện tích (diện tích = pi x r x r) và chu vi (c = 2 x pi x r) trong đó pi = 3,14.

```
R = float(input("Nhap ban kinh: "))
print("Dien tich 7: ", 3.14 * R * R)
print("Chu vi 7: ", 2 * 3.14 * R)
```
8. Tính hệ số góc, hệ số x và giao điểm y của y = 2x -2

```
x = 5
y = 2x -2

print(y)
```

9. Độ dốc là (m = y2-y1/x2-x1). Tìm hệ số góc giữa điểm (2, 2) và điểm (6,10)

```
x1, y1 = 2, 2
x2, y2 = 6, 10

m = (y2-y1)/(x2-x1)
print(m)
```

10. So sánh các độ dốc trong nhiệm vụ 8 và 9.

11. Tính giá trị của y (y = x ^ 2 + 6x + 9). Cố gắng sử dụng các giá trị x khác nhau và tìm ra giá trị x y bằng 0.

12. Tìm độ dài của 'python' và 'jargon' và thực hiện một phát biểu so sánh sai.

```
int(len('python'))
int(len('jargon'))
print("python > jargon :", int(len('python')) > int(len('jargon')))
print("python < jargon :", int(len('python')) < int(len('jargon')))
print("python = jargon :", int(len('python')) == int(len('jargon')))
```

13. Sử dụng `and` toán tử để kiểm tra xem có tìm thấy 'on' trong cả 'python' và 'jargon' không

```
print("on" in 'python' and "on" in "jargon")
```
14. `I hope this course is not full of jargon`. Sử dụng toán tử in để kiểm tra xem có `jargon` trong câu hay không.

```
print('jargon' in 'I hope this course is not full of jargon')
```

15. Không có 'on' ở cả `dragon` và `python`

16. Tìm độ dài của văn bản `python` và chuyển đổi giá trị thành float và chuyển nó thành chuỗi

```
a = 'python'
len(a)
b = float(len(a))
str(b)
```

17. Số chẵn chia hết cho 2 và số dư bằng không. Làm thế nào để bạn kiểm tra xem một số là số chẵn hay không bằng cách sử dụng python?

```
number = int(input("Nhap vao so: "))
if number % 2 == 0 :
   print("Day la so chan")
else:
   print("Day la so le")
```
18. Phép chia tầng của 7 cho 3 bằng giá trị được chuyển đổi int là 2,7.

19. Kiểm tra xem type '10' có bằng 10 không

20. Kiểm tra xem int('9.8') có bằng 10 không

21. Viết tập lệnh nhắc người dùng nhập giờ và xếp hạng mỗi giờ. Tính lương của người đó?

```
hours = int(input("Enter hours: "))
rate_hours = float(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate_hours)
```

22. Viết một tập lệnh nhắc người dùng nhập số năm. Tính số giây một người có thể sống. Giả sử ai đó sống đến trăm tuổi

```
year = int(input("Enter number of years you have lived: "))
print("You have lived for", year * 365 * 24 * 60 * 60, "seconds")
```
23. Viết một tập lệnh python hiển thị bảng sau