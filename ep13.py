# Body Mass Index Calculator
# BMI = weight / (height **2)

weight = float(input("Input your weight in kg: "))
height = float(input("Input your height in cm: "))/100
BMI = weight / height ** 2
print("Your BMI is: ", BMI)
