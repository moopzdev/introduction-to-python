# nested conditional
age = int(input("enter your age"))

if age <= 18:
    print("You are a minor.")
    if age > 15:
        print("You are most probably in a really rebellious phase.")

    if age < 10:
        print("You haven't seen much of the world just yet.")
else:
    print("You are an adult.")
