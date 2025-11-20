# Python program to compute the number of characters, words and lines in a file.

filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    num_chars = len(text)
    num_words = len(text.split())
    num_lines = text.count("\n") + (1 if text else 0)

    print("\nFile Statistics:")
    print("Characters :", num_chars)
    print("Words      :", num_words)
    print("Lines      :", num_lines)

except FileNotFoundError:
    print("Error: File not found.")
