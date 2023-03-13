from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

        
    def __abs__(self):
        pass

    def __repr__(self):
        rep = 'Zespolona(' + str(self.r) + ',' + str(self.i) + ')'
        return rep

    def __str__(self):
        c = complex(self.r, self.i)
        return str(c)

    def __add__(self, other):
        if hasattr(other, 'r'):
            c = complex(self.r,self.i) + complex(other.r, other.i)
        else:
            c = complex(self.r + other,self.i)    
        return c

    def __sub__(self, other):
        c = complex(self.r,self.i) - complex(other.r, other.i)
        return c

    def __mul__(self, other):
        c = complex(round(other*self.r) , round(other*self.i))    
        return c

    def __radd__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __rsub__(self, other):
        self = self.conjugate() 
        re = other - self.r
        im = self.i
        c = complex(re, im)
        return c

    def __eq__(self, other):
        if(self.i == other.i and self.r == other.r):
            return True
        return False

    def __ne__(self, other):
        if(self.i != other.i and self.r != other.r):
            return True
        return False

    def __pow__(self, other):
        r = sqrt(self.r ** 2 + self.i ** 2) ** other
        tg = self.argz()
        re = cos(other * tg)
        im = sin(other * tg)
        self.r = re
        self.i = im
        c = self.__mul__(r)
        return c


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)