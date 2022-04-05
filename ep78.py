# function to get summation and average

def summation(number):
    total = 0
    for i in number:
        total += i
    avg = total/len(number)
    return total, avg


x = [1, 2, 3, 4, 5, 6]
print(summation(x))
