# pariring greetings and people

greetings = ["Hello", "Hi", "Greetings", "Good Morning", "Salutations"]
people = ["Alfred", "Bruce", "Charlie", "Denver", "Eugene"]
results = []
for x in greetings:
    for y in people:
        results.append(x+" "+y)
print(results)


results = [x+" "+y for x in greetings for y in people]
print(results)
