import datetime


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


class MondayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 100
        self.ingr1 = "tomatoes "
        self.ingr2 = "cucumbers "
        self.ingr3 = "chicken "
        self.sause = "ketchup "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class TuesdayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 90
        self.ingr1 = "lettuces "
        self.ingr2 = "pumpkin "
        self.ingr3 = "chicken slices "
        self.sause = "bbq "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class WednesdayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "onion "
        self.ingr2 = "corn "
        self.ingr3 = "chicken slices "
        self.sause = "bbq "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class ThursdayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "onion "
        self.ingr2 = "corn "
        self.ingr3 = "chicken slices "
        self.sause = "bbq "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class FridayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "onion "
        self.ingr2 = "corn "
        self.ingr3 = "chicken slice "
        self.sause = "bbq "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class SaturdayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "onion "
        self.ingr2 = "chicken bones "
        self.ingr3 = "chicken slices "
        self.sause = "bbq "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


class SundayP(Pizza):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.price = 130
        self.ingr1 = "garlic "
        self.ingr2 = "banana "
        self.ingr3 = "chicken slices "
        self.sause = "sweet sauce "
        self.additional = ""
        self.addPrice = 10

    def showIng(self):
        return self.ingr1 + self.ingr2 + self.ingr3 + self.sause

    def priceCheck(self):
        if self.additional == "":
            return str(self.price * self.q)
        else:
            return str((self.price + self.addPrice) * self.q)

    def addIng(self, ingr):
        self.additional += " " + ingr

    def customerPizza(self):
        if self.additional == "":
            wholeP = self.showIng()
        else:
            wholeP = self.showIng() + self.additional
        return wholeP

    def __str__(self):
        return '{self.base}, {self.size} cm, {self.price}'.format(self=self)


def chooseOption(chooser):
    print("how many pizzas you want?")
    num = int(input())
    thisPizza = chooser(num)
    print("your pizza is today's pizza with: " + thisPizza.showIng() + " something to add? yes/no")
    answer = input()
    ind = True
    if answer == "yes":
        while ind:
            print("enter ingridient to add: ")
            ing = input()
            thisPizza.addIng(ing)
            print("is this all? yes - for yes, no - for no")
            answer1 = input()
            if answer1 == "yes":
                ind = False
    print("your pizza is with: " + thisPizza.customerPizza() + " and total price: " + thisPizza.priceCheck())


if __name__ == '__main__':
    weekday = datetime.datetime.today().weekday()
    if weekday == 0:
        chooseOption(MondayP)
    if weekday == 1:
        chooseOption(TuesdayP)
    if weekday == 2:
        chooseOption(WednesdayP)
    if weekday == 3:
        chooseOption(ThursdayP)
    if weekday == 4:
        chooseOption(FridayP)
    if weekday == 5:
        chooseOption(SaturdayP)
    if weekday == 6:
        chooseOption(SundayP)
