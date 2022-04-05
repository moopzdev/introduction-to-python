# Recursive Function


# def a(numbers):
#     if numbers >= 5:
#         return print("This is the end of this recursive function.")
#     else:
#         print("The argument is currently ", numbers)
#         numbers += 1
#         a(numbers)


def summation(number):
    if number == 1:
        return number
    else:
        return number + summation(number-1)


x = summation(5)
print(x)
