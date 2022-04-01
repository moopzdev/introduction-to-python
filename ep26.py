# string part 2

fName = "Pongsathorn"
lName = "Tiranun"
age = 80
salary = 4124.8434

print("First name:", fName, "\nLast name:", lName, "\nAge:", age)
form = "First name: {0}\nLast name: {1}\nSalary:{3:.3f}\nAge:{2}"
formatted = (form.format(fName, lName, age, salary))
print(formatted)
print(formatted.count("name"))
print(formatted.startswith("First"))
