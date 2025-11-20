# Python program to perform read and write operations on a file. 

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data written to {filename}.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

def main():
    filename = "example.txt"
    data_to_write = "Hello, this is a test file.\nThis is the second line."
    write_to_file(filename, data_to_write)
    content = read_from_file(filename)
    if content:
        print("\nContent of the file:")
        print(content)

if __name__ == "__main__":
    main()

