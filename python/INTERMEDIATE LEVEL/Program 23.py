# Write a program that accepts date of birth along with the other personal details of a person. Throw an exception if an 
# invalid date is entered.

from datetime import datetime

class InvalidDateError(Exception):
    """Custom exception for invalid dates."""
    pass

def get_date_of_birth():
    dob_input = input("Enter Date of Birth (DD-MM-YYYY): ")

    try:
        # Try to parse the input date
        dob = datetime.strptime(dob_input, "%d-%m-%Y")
        return dob
    except ValueError:
        # Raise custom exception for invalid date
        raise InvalidDateError("Invalid Date of Birth entered!")

def main():
    try:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender: ")

        dob = get_date_of_birth()

        print("\n--- Personal Details ---")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Gender: {gender}")
        print(f"Date of Birth: {dob.strftime('%d-%m-%Y')}")

    except InvalidDateError as e:
        print("\nError:", e)

if __name__ == "__main__":
    main()
