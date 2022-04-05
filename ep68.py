# List as Parameter

def displayFruit(items):
    for item in items:
        print(item)


def displayFruitTup(items):
    for item in items:
        print(item)


fruit = ["apple", "banana"]
fruitTup = ("cherry", "durian", "berry")
displayFruit(fruit)
print("\n")
displayFruitTup(fruitTup)
