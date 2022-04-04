# *agrs

def add(*numbers):
    result = 0
    for item in numbers:
        result += item
    print(result)


add(10, 20)
add(1, 2, 3)
add(30, -50)
