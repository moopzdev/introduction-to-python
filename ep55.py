# set operators

# union

fruitsA = {"banana", "lemon", "avocado"}
fruitsB = {"strawberry", "kiwi", "blackcurrent"}

allFruits = fruitsA.union(fruitsB)
print(allFruits)

del(fruitsA)
del(fruitsB)

# difference ( A - B)

fruitsA = {"banana", "lemon", "avocado", "strawberry", "kiwi"}
fruitsB = {"strawberry", "kiwi", "blackcurrent", "banana"}

print(fruitsA.difference(fruitsB))
print(fruitsB.difference(fruitsA))
print(fruitsA.intersection(fruitsB))

# subset

animals = {"dog", "cat", "cow", "elephant", "deer", "lion"}
carnivores = {"dog", "cat", "lion"}
print(carnivores.issubset(animals))
print(animals.issuperset(carnivores))

# min,max

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(min(numbers))
print(max(numbers))
