currentCount = 0
sum = 0
while(True):
    sum += float(input("Enter a number: "))
    avg = sum / (currentCount + 1)
    currentCount += 1
    if sum > 1000:
        break

print("\nThe sum of inputted", currentCount,
      "numbers is: ", sum, "\nwith average value of: ", avg)
