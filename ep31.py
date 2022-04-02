# nested loops

i = 1

while i <= 3:
    j = 1
    while j <= 5:
        print("While-loop: iteration", i, " sub-iteration", j)
        j += 1
    i += 1

for i in range(1, 5, 1):
    for j in range(5, 1, -1):
        print("For-loop: iteration", i, " sub-iteration", j)
