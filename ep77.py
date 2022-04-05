# lambda function
# code editor converted lambda function to named function on save ... bruh
def sum(x, y): return x+y


print(sum(12, 30))


def power(x):
    return lambda a: x ** a


y = power(5)

res = y(4)

print(res)
