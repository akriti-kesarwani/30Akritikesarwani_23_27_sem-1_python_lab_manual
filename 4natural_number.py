# Function to print first n natural numbers and their sum
def print_natural_numbers_and_sum(n):
    natural_numbers = list(range(1, n + 1))
    sum_of_numbers = sum(natural_numbers)
    print(f"First {n} natural numbers: {natural_numbers}")
    print(f"Sum of the first {n} natural numbers: {sum_of_numbers}")
n = int(input("Enter the value of n: "))
if n > 0:
    print_natural_numbers_and_sum(n)
else:
    print("Please enter a positive integer for 'n'.")
