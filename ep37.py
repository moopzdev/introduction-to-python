# natural number palindrome

last = int(input("Input last postive integer: "))

for row in range(1, last+1):
    for column in range(1, row+1):
        print(column, end="")
    print("")
