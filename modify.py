file = open("input.txt", "w")
file.write("Hello World!") 
file.write("Goodbye World!")
file.write("Hello again!")
file.close()

def modify_content(content):
    # Example modification: make all text uppercase
    return content.upper()

# Read from source file
with open("input.txt", "r") as infile:
    original_content = infile.read()

# Modify the content
modified_content = modify_content(original_content)

# Write to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modified content written to output.txt.")


def read_file_safely():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

read_file_safely()
