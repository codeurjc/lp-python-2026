class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def realValue(self):
        return self.num / self.den

f1 = Fraction(1,3)
f2 = Fraction(2,4)

print(f1.realValue())
print(f2.realValue())