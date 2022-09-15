print("I am python")

x = open("file.txt", 'w')
print("Hello World", file = x)
x.close()

from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.ctime)
print(today.day)
print(today.month)

byear = input('Enter your birth year')
bmonth = input('Enter your birth month')
bday = input('Enter your birth day')

year = today.year
month = today.month
day = today.day
