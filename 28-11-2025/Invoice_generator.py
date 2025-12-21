import csv

items = []
total = 0

with open("orders.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for i in reader:
        item = i[0]
        quantity = int(i[1])
        price = float(i[2])
        items.append((item, quantity, price))
        total += quantity * price

def final_writer(items, total):
    report = ""
    for item_tuple in items:
        report += f"""
    Item Name: {item_tuple[0]}
    Item Quantity: {item_tuple[1]}
    Item Price: {item_tuple[2]}
    -----------------------------
"""
    report += f"\nTotal Amount: {total}\n"

    with open("notex.txt", "w") as f:
        f.write(report)

final_writer(items, total)
print("Invoice generated successfully!")
