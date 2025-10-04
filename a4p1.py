#1)Write a Python program to print Calendar of specific month of input
#year using calendar module
import calendar
import datetime
year=int(input("enter year"))
month=int(input("enter month"))
print(calendar.month(year, month))
