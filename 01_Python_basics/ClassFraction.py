class Fraction:

    def __init__(self, top, bottom):    # Py C'tor: __init__
        self.num = top
        self.den = bottom

    def show(self):  # Py toString
        print("Fraction: ", self)

    def __str__(self):  # Py toString
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum/common, newden/common)


def gcd(m, n):  # finding the common denominator
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


print("GCD: ", gcd(20, 10))

fr1 = Fraction(9, 15)
fr2 = Fraction(6, 10)
print("GCD demo: ", fr1+fr2)

myf = Fraction(3, 5)
myf.show()
print("I ate", myf, "of the pizza")
# why not work???
myf.__str__()
str(myf)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1+f2
print("f1+f2=", f3)

