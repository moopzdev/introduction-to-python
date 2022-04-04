# dictionary
colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
print(colors["apple"])
print(colors)
colors.update({"papaya": "green"})
print(colors)
colors.update({'apple': 'green'})
print(colors)

for color in colors.keys():
    print(color)

for color in colors.values():
    print(color)


for k, v in colors.items():
    print("key=", k, ":", 'values=', v)

colors.pop("papaya")
print(colors)

colors.popitem()
print(colors)

x = colors.copy()
print("x==>", x)

colors.clear()
print(colors)

# del colors
