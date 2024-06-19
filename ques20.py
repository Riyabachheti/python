# 20. Write a python program that takes a list of numbers and returns their sum

# taking the number of elements in the list 
n = int(input (" Enter the number of elements in list "))
lst = []

# taking n elements of the list and appending them in the empty list 
for i in range (0,n):
    num = int (input (" Enter numbers of the list "))
    lst.append(num)

# taking sum of the elements 
sum = 0
for i in lst :
    sum += i
print ("The sum of elements in the list is ", sum)
