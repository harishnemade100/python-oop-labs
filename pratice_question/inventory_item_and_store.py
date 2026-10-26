"""
Q2. Inventory Item and Store
Create Product and Inventory classes. Support adding stock, removing stock, searching by name, and listing low-stock items.

Tests: object relationships, class vs. instance attributes, __repr__ and __str__
Twist: two products with the same SKU should be treated as equal. Implement __eq__ and __hash__ correctly and explain why both are needed.
"""
class Product:
    def __init__(self, id, name, stock, price):
        self.id = id
        self.name = name
        self.stock = stock 
        self.price = price

    def add_stock(self, quantity):
        if quantity <=0 :
            raise ValueError ("Quantity Should in Positive")

        self.stock += quantity

    def remove_stock(self, quantity):
        if quantity <=0 :
            raise ValueError ("Quantity Should in Positive")

        if quantity > self.stock:
            raise ValueError ("Insufficent Stocks")

        self.stock -= quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.name} - Stock: {self.stock}"

    def __repr__(self):
        return (
            f"Product(sku={self.id!r}, name={self.name!r}, "
            f"stock={self.stock}, price={self.price})"
        )


class Inventory:

    LOW_STOCK_LIMIT = 5

    def __init__(self):
        self.product = {}

    def add_product(self, product):
        if product.id in self.product:
            raise ValueError ("Product is Already Persent")

        self.product[product.id] = product

    def add_stock(self, id, quantity):
        if id not in self.product:
            raise ValueError ("Product not Found")

        self.product[id].add_stock(quantity)


    def remove_stock(self, id, quantity):
        if id not in self.product:
                raise ValueError ("Product not Found")
    
        self.product[id].remove_stock(quantity)

    def search_by_name(self, name):
        result = []

        for product in self.product.values():
            if name.casefold() in product.name.casefold():
                result.append(product)

        if len(result) ==0:
            raise ValueError ("Prodcut not Found")

        return result
    
    def low_stock(self):

        result = []

        for product in self.product.values():
            if self.LOW_STOCK_LIMIT > product.stock:
                result.append(product)

        if len(result) ==0:
                raise ValueError ("Prodcut not Found")
    
        return result


inventory = Inventory()

p1 = Product("SKU101", "Laptop", 10, 50000)
p2 = Product("SKU102", "Keyboard", 3, 1000)
p3 = Product("SKU103", "Mouse", 2, 500)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Add and remove stock
inventory.add_stock("SKU102", 5)
inventory.remove_stock("SKU101", 2)

print("Search:", inventory.search_by_name("lap"))
print("Low stock:", inventory.low_stock())

# Equality and hashing
p4 = Product("SKU101", "Different Laptop", 50, 60000)

print(p1 == p4)            # True
print(hash(p1) == hash(p4))  # True
print(len({p1, p4}))       # 1

# String representations
print(str(p1))
print(repr(p1))




            

        

    