# Bank Account Program

# database
accounts = {"Alfred": 30000, "Brian": 1000}


def getBalance():
    print("The available balances are: ", accounts)


def deposit(amount):
    if not(type(amount) is int or type(amount) is float):
        raise Exception("Only numbers are accepted as valid inputs.")
    if amount <= 0:
        raise Exception("The deposit amount must be a positive number.")

    print(amount, "deposited into Account")
    accounts["Alfred"] += amount


def withdraw(amount):
    if amount <= 0:
        raise Exception("The withdraw amount must be a positive number.")
    if amount > accounts["Alfred"]:
        raise Exception("Not enough balance to withdraw")
    print(amount, "withdrawn from Account")
    accounts["Alfred"] -= amount


def transfer(amount):
    if amount <= 0:
        raise Exception("The transfer amount must be a positive number.")
    print(amount, "transferred to Brian")
    if amount > accounts["Alfred"]:
        raise Exception("Not enough balance to transfer")
    accounts["Alfred"] -= amount
    accounts["Brian"] += amount


try:
    getBalance()
    deposit(999.9)
    getBalance()
    withdraw(900)
    getBalance()
    transfer(500)
    getBalance()
except Exception as e:
    print("Error:", e)
