# passing single argument to a function

def greetUser(name):
    print("Hello", name, "!")


greetUser("Jonathan")
greetUser("David")
greetUser(5)

# passing multiple arguments to a function


def greetFullName(fName, lName):
    print("Hello", fName, lName, "!")


greetFullName("David", "Smith")
greetFullName("123", 456)
