# 1. I would use .get() if I'm not sure a key is there so the code doesn't crash, but I would use brackets if I know the key is supposed to be there.

# 2. Exercise 8 reminds me of PivotTables in Excel because they both organize and add up data, but Python makes it easier to work with a lot of data at once.


# exercise 1 : 1 customer

customer = {
    "name": "mason",
    "email": "masong@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# exercise 2
customer["phone"] = "676-767-6767"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# exercise 3 : safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("Error: email key does not exist")

    #exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
     print(key)

# without the .items() the loop only returns keys not any values.

# exercise 5 - lookup table

tier_disc = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
discount = tier_disc.get(customer["tier"])
price = 200
final_price = price * (1 - discount)

print("Tier:", customer["tier"])
print("Discount:", f"${discount:.0%}")
print("Final Price:", f"${final_price:.2f}")

# exercise 6 - list of dictionaries

customers = [
    {"name": "mason", "tier": "platinum"},
    {"name": "nick", "tier": "gold"},
    {"name": "sarah", "tier": "silver"}
    ]
for person in customers:
    discount = tier_disc.get(person["tier"], 0)
    savings = 300 * discount

    print(f"{person['name']} ({person['tier']}): ${savings:.2f} discount")

# exercise 7 - nested catalog

catalog = {
    "hat": {"price": 9.99, "stock": 150},
    "hoodie": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")

# exercise 8 - sales by region

transactions = [
    {"region": "south", "amount": 300},
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")