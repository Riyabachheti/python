# 25. Write a program that copies the contents of one text file to another.
def copy_file_contents(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            # Read the contents of the source file
            contents = src.read()
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as dest:
            # Write the contents to the destination file
            dest.write(contents)
        
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except IOError:
        print("An error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
source_file = 'output.txt'
destination_file = 'ques25.txt'
copy_file_contents(source_file, destination_file)
