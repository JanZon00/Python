from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Kwadrat(Prostokat):
    def __init__(self, x):
        self.x = x

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    return Prostokat.x *  Prostokat.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, a, b):
    Prostokat.x = a
    Prostokat.y = b
    return Prostokat.x * Prostokat.y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    return Kwadrat.x * Kwadrat.x

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, a):
    Kwadrat.x = a
    return Kwadrat.x * Kwadrat.x
# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime
polaPowierzchni([a,b,c])