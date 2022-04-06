# Exception try... except, Exception , finally , raise Exception

while True:
    try:
        username = input("Enter your name: ")
        if username == "Moo":
            raise Exception("You are already exiled.")
        userInput1 = int(input("input a number: "))
        if userInput1 < 0:
            raise Exception("negative number not allowed :)")
        userInput2 = int(input("input another number: "))
        if userInput1 == 0 and userInput2 == 0:
            break

        result = userInput1 / userInput2
        print(result)
    except ValueError:
        print("Only numbers are valid as inputs.")
    except ZeroDivisionError:
        print("How dare you divide a number by zero?")
    except Exception as e:
        print(e)

    # else:
    #     print("Now what's next?")

    finally:
        print("Let us try again.", username)
print("End of program")
