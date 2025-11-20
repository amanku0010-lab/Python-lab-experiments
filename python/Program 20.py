# Python program to print each line of a file in reverse order.

filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            print(line[::-1])
except FileNotFoundError:
    print("Error: File not found.")
