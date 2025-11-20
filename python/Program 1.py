#Write a Python program to calculate number of days between two dates.
  
from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
delta = date2 - date1
print(f"{delta.days} days")