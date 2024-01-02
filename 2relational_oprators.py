# Function to perform arithmetic operations
def perform_arithmetic(num1, num2):
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    
    # Check if num2 is not zero to avoid division by zero
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division by zero is not allowed.")

# Function to perform relational operations
def perform_relational(num1, num2):
    print("Equal:", num1 == num2)
    print("Not Equal:", num1 != num2)
    print("Greater Than:", num1 > num2)
    print("Less Than:", num1 < num2)
    print("Greater Than or Equal To:", num1 >= num2)
    print("Less Than or Equal To:", num1 <= num2)

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
print("\nArithmetic Operations:")
perform_arithmetic(num1, num2)

# Perform relational operations
print("\nRelational Operations:")
perform_relational(num1, num2)
