# list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list of numbers
names = ["Alfred", "Brutus", "Charlie", "Danny", "Eugene"]  # list of names

# list constructor
names = list(["Alfred", "Brutus", "Charlie", "Danny", "Eugene"])

# accessing list members
print(names[0])
print(names[3])
print(names[-1]+names[0])
print(numbers[3:-1])

# editting values of members
print("initial list of numbers: ", numbers)
numbers[2] = 9
print("list of numbers: ", numbers)
sum = 0
for number in numbers:
    sum += number
print(sum)

# checking for member's presence
if 8 in numbers:
    print("it's here")
else:
    print("it's not here")

# length
print(len(numbers))

# looping with length
for i in range(len(numbers)):
    print(numbers[i])

# append
names.append("Falco")
print(names)

# insert
names.insert(4, "Giorno")
print(names)

# remove,pop,del,copy,clear
names.remove("Giorno")
print(names)
names.pop()
print(names)
del names[0]
print(names)
x = names.copy()
print(x)
names.clear()
print(names)
all = x+numbers
print(all)

# count
print(all.count(9))
