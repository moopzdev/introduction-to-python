# fibonacci
# 1,1,2,3,5,8,13,21,34,...

def fibonacci(number):
    if number <= 1:
        return number
        # return the first two numbers
    else:
        return fibonacci(number-2) + fibonacci(number-1)
        #


for i in range(8):
    print(fibonacci(i))
