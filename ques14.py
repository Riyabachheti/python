# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
str = input ("Enter the string ")
while "" not in str :
    str1= input ("")
    str = str + str1

print (f"The input string is \n {str} ")