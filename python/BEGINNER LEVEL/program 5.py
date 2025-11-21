# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their 
# sum.  

def sum_or_triple_sum(a, b, c):
    total = a + b + c
    if a == b == c:
        return 3 * total
    else:
        return total

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = sum_or_triple_sum(num1, num2, num3)
print("Result:", result)
