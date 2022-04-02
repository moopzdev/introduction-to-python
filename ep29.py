# summation of numbers

i = 1
text = "Iteration {}: sum = {}, avg = {} "
sum = 0
while i <= 10:
    sum = sum + i
    avg = sum/i
    print(text.format(i, sum, avg))
    i = i + 1

print("End of Execution")
