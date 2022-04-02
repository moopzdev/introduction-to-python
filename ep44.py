# Number Sorter
numbers = []
while True:
    x = int(input("Input a number: "))
    if x < 0:
        break
    numbers.append(x)
print("Before sorting, ", numbers)
numbers.sort()
print("Afrer sorting(increasing), ", numbers)
numbers.reverse()
print("Afrer sorting(decreasing), ", numbers)
print("End of Program")
