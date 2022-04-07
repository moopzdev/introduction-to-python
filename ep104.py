# password cracker
# supposing 3 digit passowrd = 132
# This may cause your machine to heat up

import random

ATM_PASSWORD = "133"
result = ""  # storing the randomized password


while ATM_PASSWORD != result:
    result = ""
    for letter in range(len(ATM_PASSWORD)):
        guess = random.choice("0123456789")
        result = "".join(guess)+str(result)
        print("CURRENT GUESS=", result)
print("THE CRACKED PASSWORD IS", result)
