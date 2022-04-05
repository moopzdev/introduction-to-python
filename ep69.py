# function with return


def add(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result


print("The sum is", add(15, 42, 487, 111, 33))

# silly lottery

x = input("enter the lottery number:")


def randomNumber(x):
    if len(x) < 2:
        return
    if x == "99":
        print("You won the lottery.")
        return 1000
    else:
        print("Better luck next time.")
        return 0


print("You earned $", randomNumber(x))
