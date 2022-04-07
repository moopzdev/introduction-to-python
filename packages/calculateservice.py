# calculate service module
pi = 3.14
squareRoot2 = 1.414


def addition(*args):
    total = 0
    for i in range(len(args)):
        total += args[i]
    print("summation of all inputs is =", total)


def subtraction(a, b):
    print("The difference between two number is", a-b)
