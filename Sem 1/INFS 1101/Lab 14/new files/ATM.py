# Gowshikrajan
# 60307390
# INFS 1101 - 16
# ATM

balance = 1000
MAX_WDRAW = 500
sessionWD = 0
C_PIN = 1234

print("Welcome to INFS1101 ATM!")

pin = int(input("Please enter your 4-digit pin: "))
while pin != C_PIN:
    print("Incorrect PIN. Try again.")
    pin = int(input("Please enter your 4-digit pin: "))

print("Access granted!")

print("\nMain Menu: ")
print("1. Check balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")
choice = int(input("Select an option: "))
while choice != 4:
    if choice == 1:
        print(f"Your current balance is QAR{balance}.")
    elif choice == 2:
        amountDP = int(input("Enter deposit amount: "))
        balance += amountDP
        print(f"Succesfully deposited QAR{amountDP}. New balance: QAR{balance}.")
    elif choice == 3:
        amountWD = int(input("Enter withdraw amount: "))
        if sessionWD + amountWD <= 500:
            sessionWD += amountWD
            balance -= amountWD
            print(f"Successfully withdrew QAR{amountWD}. New balance: QAR{balance}.")
        else:
            print("Sorry! You can only withdraw up to QAR500 per day.")
    print("\nMain Menu: ")
    print("1. Check balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")
    choice = int(input("Select an option: "))

print("Thank you for using INFS1101 ATM! Goodbye!")
