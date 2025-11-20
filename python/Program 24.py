# Write a Regular Expression to represent all 10 digit mobile 
# numbers. Rules: 
# 1. Every number should contains exactly 10 digits.
# 2. The first digit should be 7 or 8 or 9 Write a Python 
# Program to check whether the given number is valid mobile 
# number or not? 

import re

pattern = r'^[789][0-9]{9}$'
mobile = input("Enter a mobile number: ")
if re.match(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
