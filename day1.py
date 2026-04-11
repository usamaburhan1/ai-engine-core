print("it works")
# A dataset of 5 salespeople
sales_data = [
    {"name": "Alex", "sales": 4200},
    {"name": "Maria", "sales": 7800},
    {"name": "James", "sales": 3100},
    {"name": "Sarah", "sales": 9200},
    {"name": "Tom", "sales": 5600}
]

print(sales_data[0]["name"])
print(sales_data[1]["name"])
print(sales_data[2]["name"])
print(sales_data[3]["name"])
print(sales_data[4]["name"])

for person in sales_data:
  print(person["name"])

names = [person["name"] for person in sales_data]
print(names)

names = list(map(lambda person: person["name"], sales_data))
print(names)

all_sales = [person["sales"] for person in sales_data]
print(all_sales)

highest_sale = max(all_sales)
print(highest_sale)

all_sales = list(map(lambda person : person["sales"], sales_data))
highest_sale = max(all_sales)
print(highest_sale)

highest_sale = max(person["sales"] for person in sales_data)
print(highest_sale)

all_sales = [person["sales"] for person in sales_data]
sales_above_5000 = [sale for sale in all_sales if sale > 5000]
print(sales_above_5000)
#using loop
for person in sales_data:
    if person["sales"] > 5000:
        print(person["name"], person["sales"])


above_5000 = list(filter(lambda person: person["sales"] > 5000, sales_data))
print(above_5000)
#above lambda saves true values(as filter is used) on sales more than 5000 but stores them along with name and sales
#below we specificaly ask just for sales
above5k = list(map(lambda person: person["sales"], above_5000))
print(above5k)

above5000 = list(map(lambda p: p["sales"], filter(lambda p: p["sales"] > 5000, sales_data)))
print(above5000)