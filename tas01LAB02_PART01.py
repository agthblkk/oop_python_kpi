import json
import datetime
from random import randrange


class Ticket:
    def __init__(self, id, event, date, price, discount):
        if isinstance(id, int):
            self.id = id
            self.event = event
            self.date = str(date)
            self.discount = discount
            self.price = 10 - (price * self.discount / 100)
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
        return '{self.id}, {self.price} for {self.event}, {self.date}'.format(self=self)


class Advanceticket(Ticket):
    def __init__(self, id, event, date, price, discount):
        super().__init__(id, event, date, price, discount)


class Studentticket(Ticket):
    def __init__(self, id, event, date, price, discount):
        super().__init__(id, event, date, price, discount)


class Lateticket(Ticket):
    def __init__(self, id, event, date, price, discount):
        super().__init__(id, event, date, price, discount)


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def randomDate(start, end):
    diff = end - start
    intDelta = (diff.days * 24 * 60 * 60) + diff.seconds
    random_second = randrange(intDelta)
    return start + datetime.timedelta(seconds=random_second)


# def diffBetweenTwoDates(d1, d2):
#     delta = d2 - d1
#     return delta.days


if __name__ == '__main__':
    # random date between which we will choose next dates of events and current date
    d1 = datetime.datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.datetime.strptime('6/1/2019 1:30 AM', '%m/%d/%Y %I:%M %p')
    d3 = datetime.datetime.strptime('1/1/2020 1:30 AM', '%m/%d/%Y %I:%M %p')

    dayOfBuyingATicket = randomDate(d1, d2)
    data1 = randomDate(dayOfBuyingATicket, d3)
    data2 = randomDate(dayOfBuyingATicket, d3)
    data3 = randomDate(dayOfBuyingATicket, d3)
    event1 = "StarWars Event"
    event2 = "Java Event"
    event3 = "Saturnalia Event"

    # delta1 = diffBetweenTwoDates(dayOfBuyingATicket, data1)
    # delta2 = diffBetweenTwoDates(dayOfBuyingATicket, data2)
    # delta3 = diffBetweenTwoDates(dayOfBuyingATicket, data3)

    dict = {}

    ticket1 = Ticket(1, event1, data1, 10, 0)
    ticket2 = Advanceticket(2, event2, data2, 10, 40)

    dict["ticket1"] = ticket1.__dict__
    dict["ticket2"] = ticket2.__dict__

    write(dict, "data.json")

    m = read("data.json")
    for item in dict:
        print(m[item]['id'])
