# string

name = "mOOPZ dEV OO"
to_be_stripped = " moopz   "
print(name[:-2])  # logging the index of character in the string
print(len(name))

print(to_be_stripped)
print(to_be_stripped.strip())
print(to_be_stripped.lstrip())
print(to_be_stripped.rstrip())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace("OO", "U"))
print(name.replace("OO", "U", 1))
print("dEV" in name)
print("dEV" not in name)
