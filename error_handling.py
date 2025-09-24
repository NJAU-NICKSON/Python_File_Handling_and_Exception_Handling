# A simple Python script to demonstrate error handling when reading a file.
def read_file_with_error_handling():
    """Asks the user for a filename and handles read errors."""
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            print("\nFile contents:\n")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_file_with_error_handling()
