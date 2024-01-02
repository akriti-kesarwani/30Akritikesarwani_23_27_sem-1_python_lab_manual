# main_script.py

from my_mpdule import addition

def main():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Use the addition function from my_module
    result = addition(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
