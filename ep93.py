# writing file content
# second argument "w" is write, "r" is read, "a" is append
try:
    fw = open("./ep93.txt", "w", encoding="utf-8")
    # fw.write("Hello World!!!!") write accepts string
    # writelines accepts iterables
    fw.writelines(["Hello Darling!", "\nToday is a beautiful day!"])
    fw.write("\nHello World!")
    fw.close()

    fr = open("./ep93.txt", "r", encoding="utf-8")
    lines = fr.readlines()
    for x in lines:
        print(x)

    fa = open("./ep93.txt", "a", encoding="utf-8")
    for i in range(5):
        name = input("Enter your message: ")
        fa.writelines("\n" + name)
    fa.close()
    fr.close()

except FileNotFoundError:
    print("Could not find file with such name.")
