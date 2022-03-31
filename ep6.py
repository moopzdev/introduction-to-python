# Type Conversion
from re import X


x = 10
y = 12.45
z = "200"

print(type(x))
print(type(y))
print(type(z))

result = x+y

print(result)

result = x+int(z)
print(result)

result = str(x)+z
print(result)

result = x + float(z)
print(result)