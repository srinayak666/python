
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

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

f1=Fraction(2,3)
f2=Fraction(3,4)
f4=Fraction(3,4)
f3 = f1 + f2
print(f3)
print(f1==f2)
print(f4==f2)