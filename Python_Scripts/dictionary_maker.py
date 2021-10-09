from datetime import date
import sys

print("------------Dictionary Maker------------\n")
# Display text >>---> print("\t----      ----\n\t-- --    -- --\n\t--  --  --  --\n\t--   ----   --\n\t--    --    --\n\t--          --")


username = str(input("Enter target's Username: "))
first_name = str(input("Enter target's First Name: "))
last_name = str(input("Enter target's Last Name: "))
middle_name = str(input("Enter target's Middle Name: "))
age = int(input("Enter target's age: "))
birth_year = int(input("Input target's Date of Birth: "))
birth_month = int(input("Enter Birth Month(Ex: If January Enter: 1): "))
birth_date = int(input("Enter Birth Date: "))

fd_first_name = ''
fd_middle_name = ''
fd_last_name = ''
fd_username = ''
fd_age = 0
fd_birth_year = 0
fd_birth_month = 0
fd_birth_date = 0

if username != '':
    fd_username = username

if first_name != '':
    fd_first_name = first_name

if middle_name != '':
    fd_middle_name = middle_name

if last_name != '':
    fd_last_name = last_name

if age != 0:
    fd_age = age

if birth_year != 0:
    fd_birth_year = birth_year

if birth_month != 0:
    fd_birth_month = birth_month

if birth_date != 0:
    fd_birth_date = birth_date

if birth_year == 0 and age != 0:
    current_year = int(date.today().year)

    fd_birth_year = current_year - age

if birth_year != 0 and age == 0:
    fd_age = current_year - fd_birth_year

x0 = ''
x1 = fd_first_name
x2 = fd_middle_name
x3 = fd_last_name
x4 = fd_username
x5 = str(fd_age)
x6 = str(fd_birth_year)
x7 = str(fd_birth_month)
x8 = str(fd_birth_date)
x9 = fd_first_name.lower()
x10 = fd_middle_name.lower()
x11 = fd_last_name.lower()

if fd_birth_year < 2000:
    age_2_digits = fd_birth_year%100
    x12 = str(age_2_digits)
else:
    x12 = ''
    print("wrong")

var = [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,'123','1234','12345']
symbols = ['@','#','$','_','-']

file = sys.stdout

sys.stdout = open('dic.txt','w')

for y in var:
    for z in var:
        print(y+z)
        for i in symbols:
            print(y+i+z)

for x in var:
    for y in var:
        for z in var:
            print(x+y+z)
sys.stdout = file

sys.stdout.close()
