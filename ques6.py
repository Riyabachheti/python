# Write a program that reads the content of a text file and prints it to the console

with open("output.txt", "r") as file:
        text= file.read()
        print("The string written in output.txt is :\n",text)
