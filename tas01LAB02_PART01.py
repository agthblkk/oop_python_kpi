class Ticket:
    def __init__(self, id):
        if isinstance(id, int):
            self.id = id
            self.price = 10
            self.total = 0
        else:
            raise TypeError

    def howmuch(self):
        return self.price

    def buy(self, quantity):
        self.total += self.price * quantity

    def totalP(self):
        return self.total

    def __str__(self):
        return '{self.id}, {self.price}'.format(self=self)


class Advanceticket(Ticket):
    def __init__(self, id):
        super().__init__(id)
        self.priceA = self.price - (self.price * 40 / 100)
        self.total = 0

    def howmuch(self):
        return self.priceA

    def buy(self, quantity):
        self.total += self.priceA * quantity

    def totalP(self):
        return self.total

    def __str__(self):
        return 'A ticket number {self.id}, costs {self.priceA}'.format(self=self)


class Studentticket(Ticket):
    def __init__(self, id):
        super().__init__(id)
        self.priceS = self.price - (self.price * 50 / 100)
        self.total = 0

    def howmuch(self):
        return self.priceS

    def buy(self, quantity):
        self.total += self.priceS * quantity

    def totalP(self):
        return self.total

    def __str__(self):
        return 'A ticket number {self.id}, costs {self.priceS}'.format(self=self)


class Lateticket(Ticket):
    def __init__(self, id):
        super().__init__(id)
        self.priceL = self.price + (self.price * 10 / 100)
        self.total = 0

    def howmuch(self):
        return self.priceL

    def buy(self, quantity):
        self.total += self.priceL * quantity

    def totalP(self):
        return self.total

    def __str__(self):
        return 'A ticket number {self.id}, costs {self.priceL}'.format(self=self)


if __name__ == '__main__':
    t = Ticket(1)
    tS = Studentticket(2)
    tA = Advanceticket(1)
    tL = Lateticket(3)
    tS.buy(11)
    tA.buy(3)
    tL.buy(1)
    t.buy(3)
    print(str(t.totalP()) + " for regular tickets, " + str(tS.totalP()) + " for student tickets")
    print(str(tL.totalP()) + " for late tickets, " + str(tA.totalP()) + " for advance tickets")
