# Function to check if a number is an Armstrong number
num = int(input("Enter a number: "))
num_digits = len(str(num))
sum_of_digits = sum(int(digit) ** num_digits for digit in str(num))
if sum_of_digits == num:
 print(num," is an Armstrong Number.")
else:
 print(num," is not an Armstrong Number.")