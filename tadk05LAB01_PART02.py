class Student:
    def __init__(self, name, surname, number, grades):
        if isinstance(number, int) and number < 21:
            self.name = name
            self.surname = surname
            self.number = number
            self.grades = grades
        else:
            raise TypeError

    def __str__(self):
        return self.name + self.surname

    def avrgscore(self):
        return int(sum(self.grades) / len(self.grades))


class Group:
    def __init__(self):
        self.students = []

    def addStudent(self, *student):
        self.students.append(student)

    def bestStudents(self, students, avrg):
        ls = []
        length = len(students) - 5
        for i in range(0, len(students)):
            ls.append((students[i], avrg[i]))
        ls.sort(key=lambda x: x[1])
        newlist = ls[length:]
        return newlist

    def __str__(self):
        return "\n".join(str(stud) for stud in self.students)


student1 = Student("student1", "anderson", 1, (90, 75, 100))

student2 = Student("student2", "anderson", 2, (10, 10, 90))

student3 = Student("student3", "anderson", 3, (90, 30, 10))

student4 = Student("student4", "anderson", 4, (100, 100, 100))

student5 = Student("student5", "anderson", 5, (90, 95, 100))

student6 = Student("student6", "anderson", 6, (90, 65, 100))

student7 = Student("student7", "anderson", 7, (90, 75, 100))

student8 = Student("student8", "anderson", 8, (90, 75, 100))

group = Group()
group.addStudent(student1, student2, student3, student4, student5, student6, student7, student8)
avrgsc = []
students = []
avrgsc.append(student1.avrgscore())
avrgsc.append(student2.avrgscore())
avrgsc.append(student3.avrgscore())
avrgsc.append(student4.avrgscore())
avrgsc.append(student5.avrgscore())
avrgsc.append(student6.avrgscore())
avrgsc.append(student7.avrgscore())
avrgsc.append(student8.avrgscore())

students.append((student1.name, student1.surname))
students.append((student2.name, student2.surname))
students.append((student3.name, student3.surname))
students.append((student4.name, student4.surname))
students.append((student5.name, student5.surname))
students.append((student6.name, student6.surname))
students.append((student7.name, student7.surname))
students.append((student8.name, student8.surname))

print("best five students: ")
print(group.bestStudents(students, avrgsc))
