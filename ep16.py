'''
Control Structure
if expression:
    statement
'''

age = int(input("Input your age : "))

if 0 <= age and age < 10:
    print("You are a kid")
elif 10 <= age and age < 20:
    print("You are a teenager")
elif 20 <= age and age < 30:
    print("You are in your twenties")
else:
    print("By your age, you should already reach financial freedom")
