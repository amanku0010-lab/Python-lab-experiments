# Ask the user for a string and print out whether this string is a palindrome or not.
  
user_input = input("Enter a string: ")
normalized = user_input.replace(" ", "").lower()

if normalized == normalized[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")