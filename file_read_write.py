# A simple Python script to read a file and modify its content.

def modify_file(input_file, output_file):
    """Reads a file, modifies its content, and writes to a new file."""
    try:
        with open(input_file, "r") as f_in:
            content = f_in.read()

        # Example modification: make text uppercase
        modified_content = content.upper()

        with open(output_file, "w") as f_out:
            f_out.write(modified_content)

        print(f"Modified file saved as: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")
    modify_file(input_file, output_file)
