# phone number

phoneBook = {"191": "police", "1112": "pizza",
             "1678": "bullshit", "090-996-9848": "Moo"}


def searchNumber(message):
    for key, value in phoneBook.items():
        if value == message:
            print("Dial:", key, "for", value)


searchNumber("Moo")
