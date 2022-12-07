import math


class Rational:
    def __init__(self, numerator, denominator):
        if denominator != 0:
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ZeroDivisionError("ZeroDivisionError")

    def str(self):  # method to print rational numbers like fractions
        gc = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / gc
        self.denominator = self.denominator / gc
        return str(self.numerator) + "/" + str(self.denominator)

    def strtofloat(self):
        return float(self.numerator / self.denominator)

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __add__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        numeratorFinal = num1 + num2  # adding numerator of given numbers
        gc = math.gcd(int(numeratorFinal), int(finalDenominator))  # to reduce form
        numeratorFinal = numeratorFinal / gc
        finalDenominator = finalDenominator / gc
        return Rational(numeratorFinal, finalDenominator)

    def __sub__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        numeratorFinal = num1 - num2  # adding numerator of given numbers
        gc = math.gcd(int(numeratorFinal), int(finalDenominator))  # to reduce form
        numeratorFinal = numeratorFinal / gc
        finalDenominator = finalDenominator / gc
        return Rational(numeratorFinal, finalDenominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 == num2

    def __ne__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 != num2

    def __lt__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 < num2

    def __gt__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 > num2

    def __le__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 <= num2

    def __ge__(self, other):
        finalDenominator = math.lcm(self.denominator, other.denominator)  # find the least common multiple
        div1 = finalDenominator / self.denominator  # find number which we should multiply with numerator of first
        # number
        num1 = div1 * self.numerator  # multiplying
        div2 = finalDenominator / other.denominator  # find number which we should multiply with numerator of second
        # number
        num2 = div2 * other.numerator  # multiplying
        return num1 >= num2


if __name__ == "__main__":
    x1 = Rational(3, 31)
    y1 = Rational(21, 27)
    print(x1 + y1)
