# Write a program that takes a string input from the user and writes it to a text file.
input = input("Enter a string to write to a file: ")
with open("output.txt", "w") as file:
        file.write(input)
        print("The string has been written to output.txt.")

