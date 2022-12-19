class Organization:
    def __init__(self, name, address, phone, numOfWorkers):
        self._name = name
        self._address = address
        self._phone = phone
        self._numOfWorkers = numOfWorkers

    def __str__(self):
        return '{self._name}, {self._address}, {self._phone}, {self._numOfWorkers}'.format(self=self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, n):
        self._address = n

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, n):
        self._phone = n

    @property
    def numOfWorkers(self):
        return self._numOfWorkers

    @numOfWorkers.setter
    def numOfWorkers(self, n):
        self._numOfWorkers = n


class Department(Organization):
    def __init__(self, name, address, phone, numOfWorkers, specialization, bachelors, specialists, mags):
        super().__init__(name, address, phone, numOfWorkers)
        self._specialization = specialization
        self._bachelors = bachelors
        self._specialists = specialists
        self._mags = mags

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, n):
        self._specialization = n

    @property
    def bachelors(self):
        return self._bachelors

    @bachelors.setter
    def bachelors(self, n):
        self._bachelors = n

    @property
    def specialists(self):
        return self._specialists

    @specialists.setter
    def specialists(self, n):
        self._specialists = n

    @property
    def mags(self):
        return self._mags

    @mags.setter
    def mags(self, n):
        self._mags = n


class Faculty:
    def __init__(self, name, numOfStudents, phone):
        self._name = name
        self._numOfStudents = numOfStudents
        self._phone = phone
        self._deps = {}

    def __str__(self):
        return '{self._name}, {self._numOfStudents}, {self._phone}'.format(self=self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, n):
        self._phone = n

    @property
    def numOfStudents(self):
        return self._numOfStudents

    @phone.setter
    def numOfStudents(self, n):
        self._numOfStudents = n

    def addDep(self, dep):
        self._deps[1] = dep

    def showDeps(self):
        return self._deps


x = Department("name1", "address1", "+380984881024", 111, 19, 21, 31, 39)
y = Faculty("name11", 150, "+380984881024")
y.addDep(x)
print(y.showDeps())
