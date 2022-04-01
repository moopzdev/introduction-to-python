# Body Mass Index Calculator
# BMI = weight / (height **2)

weight = float(input("Input your weight in kg: "))
height = float(input("Input your height in cm: "))/100
BMI = weight / height ** 2
print("Your BMI is: ", BMI)

'''
18
18.5
23
25
30

'''
if BMI < 18:
    rating = "Too Skinny"
elif BMI < 23:
    rating = "Fit"
elif BMI < 25:
    rating = "A bit chubby"
elif BMI < 30:
    rating = "Fat"
else:
    rating = "Dangerously Fat"

print("Your BMI rating: ", rating)
