# find the maximum and minimum value in the list
numbers = []
odds = []
evens = []
while True:
    x = int(input("Input numbers (-ve number ends the input loop): "))
    if x < 0:
        break
    if x % 2 == 0:
        evens.append(x)
    if x % 2 != 0:
        odds.append(x)
    numbers.append(x)

print(numbers)
print("The odd number in the list are : ", odds)
print("The even number in the list are : ", evens)
