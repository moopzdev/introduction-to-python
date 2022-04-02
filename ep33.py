# break/continue

i = 1
while i <= 10:
    if i == 5:
        break
    print("iteration number", i)
    i += 1
    if i % 2 != 0:
        continue
    print("Odd iteration number")

print("End of Execution")
