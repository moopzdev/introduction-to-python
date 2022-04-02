# matching prices and products
products = ["cola", "cigs pack", "wine"]
price = [12, 60, 500]

for x, y in zip(products, price):
    print("\nproducts:", x, "\nprice:", y)

# reversing the price list
for x, y in zip(products, price[::-1]):
    print("\nproducts:", x, "\nprice:", y)
