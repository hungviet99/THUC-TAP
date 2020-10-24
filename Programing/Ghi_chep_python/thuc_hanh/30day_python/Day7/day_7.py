it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. 
print(len(it_companies))
# 2. 
it_companies.add('Twitter')
print(it_companies)

#3
it_companies.update(['NhanHoa', 'FPT'])
print(it_companies)

#4 
it_companies.remove('FPT')

#5
#Nếu xóa 1 mục k tồn tại, remove sẽ sinh lỗi còn discard thì không.

#6
C = A.union(B)
print(C)
#7
A.difference(B)

#9
type(A)
type(B)

#10.

#11
A.symmetric_difference(B)
#12
del A
del B

#13
set_age = set(age)

#14

#String là kiểu số nguyên
#List là kiểu liệt kê các giá trị được viết trong dấu ngoặc vuông
#tuple là bộ các giá trị được sắp xếp theo thứ tự và không hề thay dổi , được viết bằng dấu ngoặc tròn
#set là một tập hợp không có thứ tự và không được lập chỉ mục. Trong Python, các tập hợp được viết bằng dấu ngoặc nhọn.

#15

strings = "I am a teacher and I love to inspire and teach people"
lists = []
for word in strings:
    if word not in lists:
        lists.append(word)

print(len(lists))