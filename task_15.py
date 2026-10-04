def discount(total):
    if total >= 1000:
        return total * 0.10
    return 0


def tax(amount):
    return amount * 0.05


items = []

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    items.append({
        "name": name,
        "qty": qty,
        "price": price,
        "total": qty * price
    })

subtotal = 0

for item in items:
    subtotal += item["total"]

disc = discount(subtotal)
amount = subtotal - disc
gst = tax(amount)
final = amount + gst

print("\nShopping Bill")

for item in items:
    print(
        item["name"],
        "Qty:", item["qty"],
        "Price: {:.2f}".format(item["price"]),
        "Total: {:.2f}".format(item["total"])
    )

print()
print("Subtotal:", "{:.2f}".format(subtotal))
print("Discount:", "{:.2f}".format(disc))
print("Tax:", "{:.2f}".format(gst))
print("Final Amount:", "{:.2f}".format(final))
