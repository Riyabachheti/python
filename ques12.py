# 12. Write a python program that calculates the sum of the digits of a given number.
num = int (input ("Enter the number "))
# converting the number to string  
str_num = str(num) 
sum = 0
for i in range (0,len(str_num)):
    digit = int (str_num[i])
    sum += digit
print (f"The sum of digits of the number is {sum}")

'''
n=int(input("enter a number : "))
sum=0
while(n>0):
    i=int(n%10)
    n=int(n/10)
    sum=sum+i
print("the sum of digits is ",sum)'''