# Multiplication Table

x = int(input("input the start multiplier: "))
y = int(input("input the end multiplier: ")) + 1


for i in range(x, y, 1):
    print("\n")
    print("Multiples of", i)
    for j in range(1, 13, 1):
        print(i, "x", j, "=", i*j)
