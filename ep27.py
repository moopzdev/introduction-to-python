# Celsius to Farenheit Converter
temp = input(
    "Input temperature degree and unit (F for farenheit & C for Celsius): ")

degree = float(temp[:-1])
unit = temp[-1:]
# celsius
if unit == "c" or unit == "C":
    print("The input unit is Celsius")
    output = "It is equal to {} Farenheit"
    print(output.format(degree * 9/5 + 32))
# farenheit
elif unit == "f" or unit == "F":
    print("The input unit is Fahrenheit")
    output = "It is equal to {} Celsius"
    print(output.format((degree-32) * 5/9))

else:
    print("Bad input unit")
