# Write a program that prompts the user to enter his name. The program then greets the person with his name. But if the 
# person’s name is ‘Rahul’ and exception is thrown and he is asked to quit the program.

class QuitProgramException(Exception):
    pass

try:
    name = input("Enter your name: ")

    if name.strip().lower() == "rahul":
        raise QuitProgramException("Access denied. Please quit the program.")

    print(f"Hello, {name}! Welcome!")

except QuitProgramException as e:
    print(e)
