from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def courseName(self):
        pass

    @courseName.setter
    @abstractmethod
    def courseName(self, name):
        pass

    @property
    @abstractmethod
    def teacherName(self):
        pass

    @teacherName.setter
    @abstractmethod
    def teacherName(self, name):
        pass

    @property
    @abstractmethod
    def courseProgram(self):
        pass

    @courseProgram.setter
    @abstractmethod
    def courseProgram(self, program):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, name):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def room(self):
        pass

    @room.setter
    @abstractmethod
    def room(self, loc):
        pass

    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def location(self):
        pass

    @location.setter
    @abstractmethod
    def location(self, loc):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):
    @abstractmethod
    def object(self):
        pass


class Course(ICourse):
    def __init__(self, name, teacher, program):
        if isinstance(name, str) and isinstance(teacher, str) and isinstance(program, str):
            self.name = name
            self.teacher = teacher
            self.program = program
        else:
            raise TypeError

    @property
    def courseName(self):
        return self.name

    @courseName.setter
    def courseName(self, name):
        self.name = name

    @property
    def teacherName(self):
        return self.teacher

    @teacherName.setter
    def teacherName(self, name):
        self.teacher = name

    @property
    def courseProgram(self):
        return self.program

    @courseProgram.setter
    def courseProgram(self, program):
        self.program = program

    def __str__(self):
        return f'{self.name}, teacher {self.teacher}, program {self.program}'


class LocalCourse(ILocalCourse, Course):
    def __init__(self, name, teacher, program, r):
        super().__init__(name, teacher, program)
        if isinstance(r, int):
            self.r = r
        else:
            raise TypeError

    @property
    def room(self):
        return self.r

    @room.setter
    def room(self, loc):
        self.r = loc

    def __str__(self):
        return str(super().__str__()) + f' located in {self.r} room'


class OffsiteCourse(IOffsiteCourse, Course):
    def __init__(self, name, teacher, program, location):
        super().__init__(name, teacher, program)
        if isinstance(location, str):
            self.locc = location
        else:
            raise TypeError

    @property
    def location(self):
        return self.location

    @location.setter
    def location(self, loc):
        self.locc = loc

    def __str__(self):
        return str(super().__str__()) + f' is taken at {self.locc}'


class CourseFactory(ICourseFactory):
    def __init__(self, name, teacher, program, loc, courseLoc):
        self.course = courseLoc
        self.name = name
        self.teacher = teacher
        self.program = program
        self.loc = loc

    def object(self):
        if self.course == "local":
            return LocalCourse(self.name, self.teacher, self.program, self.loc)

        elif self.course == "offsite":
            return OffsiteCourse(self.name, self.teacher, self.program, self.loc)

        elif self.course == "teacher":
            return Teacher(self.teacher)


class Teacher(ITeacher):
    def __init__(self, name):
        self.teac = name

    @property
    def teacher(self):
        return self.teac

    @teacher.setter
    def teacher(self, name):
        self.teac = name

    def __str__(self):
        return f'{self.teac}'


if __name__ == '__main__':
    string = "teacher"
    course = CourseFactory("Course1", "teacherName", "program1", "someWhere", string)
    obj1 = course.object()
    print(obj1)
