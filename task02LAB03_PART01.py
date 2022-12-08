class Notebook:
    def __init__(self, name, surname, number, birthday):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(number, str) and isinstance(birthday, str):
            self._name = name
            self._surname = surname
            self._number = number
            self._birthday = birthday
            self.l = []
        else:
            raise TypeError

    def __str__(self):
        return f'{self._name} {self._surname} , {self._number} , {self._birthday}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, s):
        self._surname = s

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        self._number = num

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, b):
        self._birthday = b

    def __add__(self, other):
        str1 = self._name + " " + self._surname + " " + self._number + " " + self._birthday
        str2 = other.name + " " + other.surname + " " + other.number + " " + other.birthday
        self.l.append(str1)
        self.l.append(str2)

        return self.l

    def __sub__(self, other):
        del self.l[other]
        return self.l

    def __mul__(self, other):
        for each in self.l:
            if each == other:
                return True
            else:
                return False


if __name__ == '__main__':
    x = Notebook("agatha", "krivokon", "+380984881024", "06.01.2004")
    y = Notebook("agatha", "krivokon", "+380984881024", "06.01.2004")
    print(x + y)
    print(x - 1)
    print(x * 'agatha krivokon +380984881024 06.01.2004')
