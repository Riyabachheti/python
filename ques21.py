# 21. Write a python program that counts the occurrences of a specific element in a list.

# taking the number of elements in the list 
n = int(input (" Enter the number of elements in list "))

lst = []

# taking n elements of the list and appending them in the empty list 
for i in range (0,n):
    element = input (" Enter element in the list ")
    lst.append(element)

str = input("Enter the element to find its occurance ")

count = 0
for i in lst:
    if i == str:
        count += 1

print(f"The count of occurance of {str} is : {count}")
