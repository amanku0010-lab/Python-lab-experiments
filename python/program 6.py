# Write a Python program to test whether a passed letter is a vowel or not 

def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    return letter in vowels

char = input("Enter a single letter: ")

if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is not a vowel.")
else:
    print("Please enter a single alphabetic character.")