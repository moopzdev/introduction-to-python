# chessboard

side = int(input("Input the size of chessboard(no units required): "))

for row in range(1, side+1):
    for col in range(1, side+1):
        if((row + col) % 2 == 0):
            print("x", end="")
        else:
            print("o", end="")
    print("")
