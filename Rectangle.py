class Rectangle:
    def __init__(self):
        self._length = 1
        self._width = 1

    def get_length(self):
        return self._length

    def set_length(self, length):
        if isinstance(length, int) or length > 20 or length < 0:
            raise ValueError("length isn't float or > 20 or < 0")
        else:
            self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        if isinstance(width, int) or width > 20 or width < 0:
            raise ValueError("width isn't float or > 20 or < 0")
        else:
            self._width = width

    def perimetr(self):
        return 2 * self._length + 2 * self._width

    def area(self):
        return self._length * self._width


rect = Rectangle()

rect.set_length(3.0)
rect.set_width(4.0)

print(rect.perimetr(), rect.area())