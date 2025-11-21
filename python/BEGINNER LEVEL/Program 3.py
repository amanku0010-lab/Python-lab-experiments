#  Ask the user for a number. Depending on whether the 
# number is even or odd, print out an appropriate message to 
# the user.

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("That's an even number!")
else:
    print("That's an odd number!")
