import os

def file_read_write_modify(input_file_path, output_file_path):
    """
    Reads a file, modifies its content, and writes the modified content to a new file.

    Args:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to the output file.
    """
    try:
        # 1. Read the file
        with open(input_file_path, 'r') as infile:
            content = infile.read()

        # 2. Modify the content (Example: Uppercase conversion)
        modified_content = content.upper()  #  You can change this line

        # 3. Write to the new file
        with open(output_file_path, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully modified '{input_file_path}' and wrote to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")  #  Catch other potential errors



def error_handling_lab():
    """
    Asks the user for a filename, handles errors if it doesn't exist or can't be read,
    and reads the file content if successful.
    """
    while True:
        filename = input("Enter the name of the file to read (or 'exit' to quit): ")
        if filename.lower() == 'exit':
            break # break from the loop
        try:
            # Attempt to open the file
            with open(filename, 'r') as file:
                content = file.read()  # Read the content
                print(f"File '{filename}' content:\n{content}")
                # You could add more processing here, like counting words, etc.

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please check the filename and try again.")
        except Exception as e:
            print(f"An error occurred while reading '{filename}': {e}")
            print("Please ensure the file exists and you have the correct permissions.")

if __name__ == "__main__":
    # --- File Read & Write Challenge ---
    # Create a dummy input file for testing
    input_file = "my_input.txt"
    try:
        with open(input_file, 'w') as f:
            f.write("This is a test file.\nIt contains some text.\nHello Python!\n")
    except Exception as e:
        print(f"Error creating dummy file: {e}")

    output_file = "my_output.txt"
    file_read_write_modify(input_file, output_file)

    # --- Error Handling Lab ---
    error_handling_lab()
