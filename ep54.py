# sets (members has no index, can add and delete members)
fruits = {"banana", "cherry", "apple"}
print(fruits)

print(type(fruits))

fish = set(["angler", "baracuda", "baracuda", "clownfish"])

fruits.add("durian")
print(fruits)
# can use fruits.update method to add new members

lis = ["pineapple", "durian", "avocado"]
fruits.update(lis)
print(fruits)

for item in fruits:
    print(item)
print(len(fruits))

if "blueberry" in fruits:
    print("yeah")
else:
    print("nope")

fruits.remove('durian')

# this will not throw an error if durian is not present in fruits.
fruits.discard('durian')

print(fruits)

fruits.clear()
print(fruits)
