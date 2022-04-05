# factorial

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)


x = factorial(5)
print(x)
