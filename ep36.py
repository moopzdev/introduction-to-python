# find the maximum and minimun numbers

from json.encoder import INFINITY


totalInputCount = int(input("How many number would you like to input? "))
currentCount = 0
max = -INFINITY
min = INFINITY

while(currentCount < totalInputCount):
    number = float(input("Enter a number: "))
    if number > max:
        max = number
    if number < min:
        min = number
    currentCount += 1
print("\nFrom your inputs:\nmax: ", max, "\tmin:", min)
