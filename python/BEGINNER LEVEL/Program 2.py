# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
 
n = input("Enter an integer: ")
n1 = int(n)
n2 = int(n * 2)
n3 = int(n * 3)
result = n1 + n2 + n3
print(f"The result of n + nn + nnn is: {result}")
