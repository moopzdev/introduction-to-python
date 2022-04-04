# frozen set
fruits = set(["Durian", "apple", "banana"])
fruits.add("Cherry")
fruits.discard("Durian")
print(fruits)

veggies = frozenset(["carrot", "cabbage"])
# veggies.add("onion") .... this would caouse an error
# veggies.discard("carrot") ... this too would cause an error
