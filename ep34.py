totalInputCount = int(input("How many number would you like to sum? "))
currentCount = 0
sum = 0
while(currentCount < totalInputCount):
    sum += float(input("Enter a number: "))
    avg = sum / (currentCount + 1)
    currentCount += 1

print("\nThe sum of inputted", totalInputCount,
      "numbers is: ", sum, "\nwith average value of: ", avg)
