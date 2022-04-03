# tuple ...basically an immutable list
tup = (1, 2, 3, 4, 5)
lis = [1, 2, 3, 4, 5]
print(tup)
print(lis)
print(type(tup))
print(type(lis))
lis[0] = "dexter"
# tup[0] = "dexter" ...this would throw an error because tuple is meant for storing constants.
print(lis)
print(tup[-2])

# cloning into a list, reassigning values, convert back into a tuple
lis2 = list(tup)
lis2[0] = "dexter"
lis2.pop()
tup = tuple(lis2)
print(tup)

if "dexter" in tup:
    print("dexter is in the tuple")
else:
    print("dexter isn't in the tuple")

print(len(tup))

for i in range(len(tup)):
    print(tup[i])

x = ("is this a tuple?",)  # add trailing comma to define a tuple
print(type(x))

tup = tup+tuple(lis)
print(tup)

x = tup.count(4)
print(x)

y = tuple(reversed(tup))
print(y)
