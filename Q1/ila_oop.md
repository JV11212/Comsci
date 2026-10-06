The Four Pillars of OOP in a Sari-Sari Store System

1. Encapsulation
This is the gathering all the information about one item/product (name, price, quantity) and placing it together in one place, instead of having separate messy variables scattered around. For example, a Product object keeps its own name, price, and quantity together, and only special commands like sell() or restock() can change them. This keeps the data of the products organized, so you don't accidentally edit the wrong item's info.

2. Abstraction
This means hiding the all the unnecessary details and only showing what's needed. When the store clerk wants to sell an item, they can just call something like sellItem(). They don't need to know exactly how the program checks stock or updates numbers. They just need to run a simple command. This makes the system easier and also simpler to use.

3. Inheritance
This means creating a "general" product type, then making more specific types based on it, without rewriting everything. For example, you can have a basic Product class, then create a PerishableProduct (like bread or eggs) that adds an expiration date, using the same basic info (name, price, quantity) from the original Product. This avoids repeating the same code for every product type.

4. Polymorphism
This means different types of products can respond differently to the same action/method. For example, if you call showInfo() on any product, a perishable item will also show its expiration date, while a regular item won't, even though you used the same method name for both.

Small Group Proposal: A Simpler Inventory System

The problem: Using separate variables for each item (name1, price1, qty1, name2, price2, qty2...) is messy and hard to manage, especially if lots of products are added.

Our solution: Create a Product class that stores one item's name, price, and quantity together. Then create an Inventory class that holds a list of these Product objects, plus simple methods to add, remove, and display items.

# Product info
names = []
prices = []
quantities = []

# Add a product
names.append("Instant Noodles")
prices.append(15)
quantities.append(50)

names.append("Soap")
prices.append(20)
quantities.append(40)

# Shows all products
for i in range(len(names)):
    print("Name:", names[i])
    print("Price:", prices[i])
    print("Quantity:", quantities[i])
    print("------")

# Remove a product (example: remove "Soap")
item_to_remove = "Soap"
if item_to_remove in names:
    index = names.index(item_to_remove)
    names.pop(index)
    prices.pop(index)
    quantities.pop(index)
Why this is better:

Instead of 15 separate variables for 5 items, we could just make 5 Product objects. Adding a new item is easy. You just need to create a new Product and add it to the list. All the info for one item are grouped together, so all information is safe and can't be mixed up. It's easier to add new features later, like expiration dates.
