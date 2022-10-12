import math


class Rational:
    def __init__(self, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self._numerator = 1
            self._denominator = 2
        elif denominator == 0:
            raise ZeroDivisionError("ZeroDivisionError")
        else:
            raise TypeError("numerator or denominator isn't int")

    def str(self):  # method to print rational numbers like fractions
        gc = math.gcd(self._numerator, self._denominator)
        self._numerator = self._numerator / gc
        self._denominator = self._denominator / gc
        return str(self._numerator) + "/" + str(self._denominator)

    def strtofloat(self):
        return float(self._numerator / self._denominator)


obj = Rational(2, 4)
print(obj.str(), obj.strtofloat())
