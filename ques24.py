# 24. Write a program that acts as a simple calculator. 
# It should take two numbers and an operator (+, -, *, /) as input and print the result.

def simple_calculator():
    try:
        # Taking inputs
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        # Performing the operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operator!"
        
        # Printing the result
        print("The result is:", result)
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator function
simple_calculator()
