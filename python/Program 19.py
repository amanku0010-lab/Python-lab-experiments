# Python program to count frequency of characters in a given file.

from collections import Counter

filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    frequency = Counter(text)

    print("\nCharacter Frequency:\n")
    for char, count in frequency.items():
        if char == " ":
            display_char = "<space>"
        elif char == "\n":
            display_char = "<newline>"
        elif char == "\t":
            display_char = "<tab>"
        else:
            display_char = char

        print(f"{display_char!r} : {count}")

except FileNotFoundError:
    print("Error: File not found.")
