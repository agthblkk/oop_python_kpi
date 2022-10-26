class Pizza:
    def __init__(self, quantity):
        if isinstance(quantity, int):
            self.q = quantity
            self.base = "dough"
            self.size = 30
            self.price = 0
        else:
            raise TypeError

    def showIng(self):
        return self.base

    def priceCheck(self):
        return self.price * self.q

    def __str__(self):
        return '{self.base}, {self.size} cm'.format(self=self)


class potd1(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 100
        self.ingr1 = "tomatoes"
        self.ingr2 = "cucumbers"
        self.ingr3 = "chicken"
        self.sause = "ketchup"
        self.additional = ""

    def showIng(self):
        return self.ingr1 + " " + self.ingr2 + " " + self.ingr3 + " " + self.sause

    def priceCheck(self):
        return self.price * self.q

    def addIng(self, ingr):
        self.additional += ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP
    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)

class potd2(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 90
        self.ingr1 = "lettuces"
        self.ingr2 = "pumpkin"
        self.ingr3 = "chicken slices"
        self.sause = "bbq"
        self.additional = ""

    def showIng(self):
        return self.ingr1 + " " + self.ingr2 + " " + self.ingr3 + " " + self.sause

    def priceCheck(self):
        return self.price * self.q

    def addIng(self, ingr):
        self.additional += ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP
    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)

class potd3(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "onion"
        self.ingr2 = "corn"
        self.ingr3 = "chicken slices"
        self.sause = "bbq"
        self.additional = ""

    def showIng(self):
        return self.ingr1 + " " + self.ingr2 + " " + self.ingr3 + " " + self.sause

    def priceCheck(self):
        return self.price * self.q

    def addIng(self, ingr):
        self.additional += ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)

if __name__ == '__main__':
    cust1 = potd1(3)
    print(cust1.showIng());
    cust1.addIng(" corn")
    print("total price is: " + str(cust1.priceCheck()))
    print("your order is ready, pizza with: " + cust1.customerPizza())

    cust2 = potd2(1)
    print(cust2.showIng());
    cust1.addIng(" smth")
    print("total price is: " + str(cust2.priceCheck()))
    print("your order is ready, pizza with: " + cust2.customerPizza())

    cust3 = potd3(3)
    print(cust3.showIng());
    cust3.addIng(" smth")
    print("total price is: " + str(cust3.priceCheck()))
    print("your order is ready, pizza with: " + cust3.customerPizza())



