balance = 1000

while True:
    print("welcome to bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = int(input("Enter option: "))

    if option == 1:
        print("]check Balance:", balance)

    elif option == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Balance:", balance)

    elif option == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Remining balance:", balance)
        else:
            print("Insufficient Balance!")

    elif option == 4:
        print("Thank you")
        break

    else:
        print("Invalid Option!")