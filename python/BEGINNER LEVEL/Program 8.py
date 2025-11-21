# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you 
# don’t know what a divisor is, it is a number that divides evenly into another number.

num = int(input("Enter a number: "))
divisors = [i for i in range(1, num + 1) if num % i == 0]

print("Divisors of", num, "are:", divisors)
