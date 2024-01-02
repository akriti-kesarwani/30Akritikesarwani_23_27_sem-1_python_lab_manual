# main_script.py

from bank_module import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of $1000
    account = BankAccount(1000)

    # Display initial balance
    print(f"Initial Balance: ${account.check_balance()}")

    # Deposit money
    deposit_amount = float(input("Enter the amount to deposit: "))
    account.deposit(deposit_amount)
    print(f"Balance after deposit: ${account.check_balance()}")

    # Withdraw money
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    success, new_balance = account.withdraw(withdraw_amount)
    
    if success:
        print(f"Withdrawal successful! New Balance: ${new_balance}")
    else:
        print(f"Withdrawal failed. Reason: {new_balance}")

if __name__ == "__main__":
    main()
