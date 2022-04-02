# frame

height = int(input("Input the height of frame(no units required): "))
width = int(input("Input the width of frame(no units required): "))

for row in range(0, height):
    for col in range(0, width):
        if row == 0 or row == height-1:
            print("x", end="")
        elif col == 0 or col == width-1:
            print("x", end="")
        else:
            print(" ", end="")
    print("")
