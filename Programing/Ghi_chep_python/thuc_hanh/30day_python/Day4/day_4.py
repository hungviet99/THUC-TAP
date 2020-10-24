# Ngay 4

# 1. Noi chuoi

string = 'Thirty' + 'Days' + 'Of' + 'Python' 
print(string)

# 2. noi chuoi

string1 = 'Coding' + 'For' + 'All'

# 3,4. 

company = "Coding For All"
print(company)

# 5. 

print(len(company))

#6. 

print(company.upper())

#7. 

print(company.lower())

# 8.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9.

# 10. 

#11
string2 = 'Coding For All'
print(string2.replace('Coding', 'hung'))

# 12 

string3 = "Python for Everyone" 
print(string3.replace('Everyone', 'All'))

# 13

print(string2.split())

# 14 
string4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string4.split(', '))

# 15

string2[0]
# 16
string2[-1]

# 17 
string2[10]

#18
''.join(x[0] for x in string3.split()) 
# 19

''.join(x[0] for x in string2.split())
# 20

print(string2.index('C'))

#21 
print(string2.index('F'))

#22

print(string2.rfind('l'))

#23

string5 = "You cannot end a sentence with because because because is a conjunction"

print(string5.index('because'))

#24

print(string5.rindex('because'))

#25

#26

# 31

x = "30DaysOfPython"
x.isidentifier()
y = "thirty_days_of_python" 
y.isidentifier()

# 32
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(library)
print(result)

# 33 

print("I am enjoying this challenge." + "\n" + "I just wonder what is next.")

# 34 

print("8 + 6 = ",8+6,"\n","8 - 6 = ",8-6,"\n","8 * 6 = ",8*6,"\n","8 / 6 = ",8/6,"\n","8 % 6 = ",8%6,"\n","8 // 6 = ",8//6,"\n","8 ** 6",8**6)


