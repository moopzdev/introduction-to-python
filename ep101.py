# Module Date/Time
import datetime

result = datetime.datetime.now()
print(result.year)
print(result.month)
print(result.day)
print(result)

newDate = datetime.datetime(2022, 4, 7)
print(newDate)

# Adjusting output formatting
print(result)
# date only
print(result.strftime("%x"))
# time only
print(result.strftime("%X"))
print(result.strftime("%c"))

print(result.strftime("%H:%M:%S %p"))

# day of the year
print(result.strftime("%j"))

# day of the week
print(result.strftime("%a"))
print(result.strftime("%A"))

# index of weekday
print(result.strftime("%w"))

# month
print(result.strftime("%b"))
print(result.strftime("%B"))

print(result.strftime("%A %d %B %Y"))

# d/m/y
print(result.strftime("%d/%m/%Y"))
