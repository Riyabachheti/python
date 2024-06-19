# 22. Write a python program that returns the minimum and maximum values in a list of numbers.

# taking the number of elements in the list 
n = int(input (" Enter the number of elements in list "))
lst = []

# taking n elements of the list and appending them in the empty list 
for i in range (0,n):
    num = int (input (" Enter numbers of the list "))
    lst.append(num)

print ("The maximum value of the list is : ", max(lst))

print ("The minimum value of the list is : ", min(lst))