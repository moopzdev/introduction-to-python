#function and callbacks

def multiMax(x, y, z):
    a = getMax(x, y)
    b = getMax(a, z)
    return b


def getMax(x, y):
    if x > y:
        return x
    else:
        return y


max = multiMax(10, 5, 15)
print("the max number is", max)
