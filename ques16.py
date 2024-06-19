# 16. Write a program in python that counts the frequency of each character in a string.
str1 = input("Enter first string ")
str2 = input ("Enter character to check frequency ")
count = 0
for i in str1 :
    if i == str2:
        count +=1
print (f"frequency of {str2} in {str1} is : {count} ")
