# nested conditional
age = int(input("enter your age"))

if age <= 18:
    print("You are a minor.")
    if age > 15:
        pass  # the pass statement helps prevent errors in empty if conditionals, loops and definitions
    if age < 10:
        print("You haven't seen much of the world just yet.")
else:
    print("You are an adult.")
