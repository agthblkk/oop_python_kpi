class Product:
    def __init__(self, price, descr):
        if isinstance(price, int) and isinstance(descr, str) and price > 0:
            self.price = price
            self.descr = descr
        else:
            raise TypeError("wrong type!!")

    def __str__(self):
        return str(self.price + " " + self.descr)


class Customer:
    def __init__(self, surname, name, mob):
        if isinstance(surname, str) and isinstance(name, str):
            self.name = name
            self.surname = surname
            self.mob = mob
        else:
            raise TypeError("wrong type!!")

    def __str__(self):
        return str(self.name + " " + self.surname + " " + self.mob)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.pricelist = []

    def add_product(self, *productsb):
        n = len(productsb)
        for item in range(0, n):
            self.products.append(productsb[item].descr)
            self.pricelist.append(productsb[item].price)

    def total_price(self):
        return sum(self.pricelist)


George = Customer("Super", "George", "+380000000000001")
milk = Product(10, "milk")
bread = Product(20, "bread")
water = Product(30, "water")
cart = Order(George)
ls = []
cart.add_product(milk, bread, water)
print(cart.products)
print(cart.total_price())
