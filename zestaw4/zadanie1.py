class Baza(object):
    def __new__(cls, *args):
        print("-> Baza __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- Baza __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> Baza __init__", x)
        super().__init__()
        print("-- Baza __init__")
        self.x = x
        print("<- Baza __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-Baza-")

class A(object):
    def __new__(cls, *args):
        print("-> A __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- A __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> A __init__",x)
        super().__init__(x)
        print("-- A __init__")
        self.x = x
        print("<- A __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-A-")


class B(Baza):
    pass

class C(B):
    pass

class D(A, C, B, Baza):
    # tu nie definiować __new__
    pass

### SCENARIUSZ 1: 
print(B.mro()) #klasa B dziedziczy po klasie nadrzędnej Baza, klasa nadrzędna od
#Pythona3 dziedziczy po object
b = B(123)  #__new__ wywołuję się gdy tworzony jest obiekt, __init__ 
#inicjalizuje obiekt
b.id()
print(b) #metoda specjalna __str__ zwraca 123

### SCENARIUSZ 2: 
print(C.mro()) # MRO : C -> B -> Baza -> Object
c = C(456) #podobnie jak w scenariuszu 1
c.id()
print(c)

### SCENARIUSZ 3: 
print(D.mro()) #Klasy w nowym stylu przeszukiwane są tylko raz najpierw
#od lewej do prawej potem wgłąb
d = D(789) #tworzymy obiekt, wywołuje się metoda __new__ klasy A
#następnie super().__init__(x) wywołuje konstruktor klasy bazowej
d.id()
print(d)

### SCENARIUSZ 4: 
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d),id() albo B(d),id() itp.

