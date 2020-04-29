
class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __add__(self, other_fraction):
        new_num = self.num*other_fraction.den +self.den*other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num,new_den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

f1=Fraction(2,3)
f2=Fraction(3,4)
f3 = f1 + f2
print(f3)