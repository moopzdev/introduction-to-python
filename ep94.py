# file deletion
import os

fileName = "ep94.txt"

try:
    # fw = open("ep94.txt", "w", encoding="utf-8")

    if os.path.exists(fileName):
        os.remove(fileName)
        print(fileName, " is successfully deleted.")
    else:
        raise Exception(
            "The file with such name does not exist in this directory.")

except Exception as e:
    print(e)
