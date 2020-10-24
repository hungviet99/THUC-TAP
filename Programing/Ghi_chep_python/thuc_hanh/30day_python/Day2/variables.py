# Day 2: 30 Days of python programming


first_name = "Hung"
last_name = "Nguyen"
full_name = "Nguyen Viet Hung"
country = "Viet Nam"
city = "Ha Noi"
age = 22
year = 2020
is_married = "yes"
is_true = "yes"
is_light_on = "on"

Version, cong_ty = 3.6, "NhanHoa"

#print(type(first_name))
#print(type(last_name))
#print(type(full_name))
#print(type(country))
#print(type(city))
#print(type(age))
#print(type(year))
#print(type(is_married))
#print(type(is_true))
#print(type(is_light_on))

print("first_name: ", len(first_name))
print("last_name: ", len(last_name))
#print("full_name: ", len(full_name))
print("Comparison first_name > last_name: ", len(first_name) > len(last_name))
print("Comparison first_name < last_name: ", len(first_name) < len(last_name))

## Khai bao bien 

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two 
division = num_one/num_two 
remainder = num_one % num_two
exp = num_one ** num_two 
floor_division = num_one // num_two
print(total, "\n", diff, "\n", product, "\n", division, "\n", remainder, "\n", exp, "\n", floor_division)

# Hinh Tron
R = 30
### Dien tich hinh tron 
area_of_circle = 3.14 * (R * R)
circum_of_circle = 2 * R * 3.14
print("Dien tich hinh tron: ", area_of_circle)
print("Chu vi hinh tron: ", circum_of_circle)

## input R

r = int(input("Nhap vao ban kinh: "))
S = 3.14 * (r * r)
print("Dien tich hinh tron (input R): ", S)

## Nhap ten
name = input("Nhap ten: ")
ho = input("Nhap ho: ")
country = input("Nhap quoc gia: ")
tuoi = input("Nhap vao tuoi: ")
