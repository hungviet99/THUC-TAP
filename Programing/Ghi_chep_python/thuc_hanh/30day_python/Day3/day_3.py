#4
base = int(input("Nhap base: "))
hight = int(input("Nhap hight: "))
print("Dien tich: ", 0.5 * base * hight)

#5 

a = int(input("Nhap canh thu 1: "))
b = int(input("Nhap canh thu 2: "))
c = int(input("Nhap canh thu 3: "))
print("chu_vi: ", a + b + c)

#6

length = int(input("Nhap chieu dai: "))
width = int(input("Nhap chieu rong: "))
print("Dien tich6: ", length * width)
print("Chu vi 6: ", 2 * (length + width))

#7

R = float(input("Nhap ban kinh: "))
print("Dien tich 7: ", 3.14 * R * R)
print("Chu vi 7: ", 2 * 3.14 * R)

#8 

x = 5
y = 2x -2 

print(y)

#9

x1, y1 = 2, 2
x2, y2 = 6, 10

m = (y2-y1)/(x2-x1)
print(m)

# 10

# 11

#12

int(len('python'))
int(len('jargon'))
print("python > jargon :", int(len('python')) > int(len('jargon')))
print("python < jargon :", int(len('python')) < int(len('jargon')))
print("python = jargon :", int(len('python')) == int(len('jargon')))

# 13 
print("on" in 'python' and "on" in "jargon")

# 14

print('jargon' in 'I hope this course is not full of jargon')

# 15 

# 16

a = 'python'
len(a)
b = float(len(a))
str(b)


#17

number = int(input("Nhap vao so: "))
if number % 2 == 0 : 
   print("Day la so chan")
else: 
   print("Day la so le")

# 18 

#19

# 20

#21
hours = int(input("Enter hours: "))
rate_hours = float(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate_hours)

# 22

year = int(input("Enter number of years you have lived: "))
print("You have lived for", year * 365 * 24 * 60 * 60, "seconds")
