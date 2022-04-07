# main program

# modules in sub-folder can be imported by the syntax folderName.ModuleName.py

# renaming module
import packages.calculateservice as calc
from packages.calculateservice import addition as add
# importing specific functions from module


calc.addition(25, 45, 12)
calc.subtraction(45, 13)
print(calc.pi)
print(calc.squareRoot2)


add(25, 45, 102)
