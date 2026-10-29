"""An ATM menu that repeats until the user chooses to exit. The balance is
kept in a variable and updated by deposits and withdrawals.

Run: python 08_atm_menu.py

Sample session:
    1. Withdraw
    2. Deposit
    3. Check balance
    4. Exit
    Choose an option: 2
    Amount to deposit: 500
    Deposited 500.00. New balance: 1500.00
    (menu shown again)
    Choose an option: 1
    Amount to withdraw: 2000
    Insufficient funds. Balance is 1500.00
    (menu shown again)
    Choose an option: 4
    Thank you for using the ATM.
"""

balance = 1000.0

# while True keeps the menu going; the Exit option uses break to leave.
while True:
    print()
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print(f"Insufficient funds. Balance is {balance:.2f}")
        else:
            balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {balance:.2f}")
    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance += amount
            print(f"Deposited {amount:.2f}. New balance: {balance:.2f}")
    elif choice == "3":
        print(f"Current balance: {balance:.2f}")
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        # Any other input falls through to here; the loop simply repeats.
        print("Invalid option, please choose 1 to 4.")
