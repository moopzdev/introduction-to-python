# phone number

phoneBook = {"191": "police", "1112": "pizza",
             "1678": "bullshit", "090-996-9848": "Moo"}


def searchNumber(message):
    for key, value in phoneBook.items():
        if value == message:
            return print("Dial:", key, "for", value)

    return print("No data found.")


message = input("Input a phonebook entry: ")
searchNumber(message)
