# random utility

import random

for i in range(10):
    x = random.uniform(0, 100)
    print(x)

for i in range(10):
    x = random.randrange(1, 10, 1)
    print(x)

for i in range(10):
    x = random.randint(1, 5)
    print(x)

outcomes = [2, 4, 6, 8, 10, "A", "B", "C"]
for i in range(10):
    x = random.choice(outcomes)
    print(x)

random.shuffle(outcomes)
print(outcomes)

for i in range(10):
    x = random.choice("ABCDEFGH")
    print(x)
