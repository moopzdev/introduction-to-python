# tower of hanoi

def hanoi(n, a, b, c):
    if n == 0:
        return
    hanoi(n-1, a, c, b)
    print("moving plate", n, "to", c)
    hanoi(n-1, b, a, c)


hanoi(3, "A", "B", "C")
