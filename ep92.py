# reading file content
try:
    fr = open("./ep992.txt", "r", encoding="utf-8")
    print(fr.read())
except FileNotFoundError:
    print("Could not find file with such name.")
