# square art

side = int(input("Input the size of square(no units required): "))

for row in range(1, side+1):
    for column in range(1, side+1):
        print("x", end="")
    print("")
