# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print ( "{} {}".format(self, x) )
    
    @classmethod
    def class_foo(self, x):
        print ( "class_foo({}, {})".format(self, x) )
        pass
    
    @staticmethod
    def static_foo(x):    
        print ( "static_foo({})".format(x))

a = A()
a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a,123) # ditto
a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # ditto
a.static_foo(123) # wykonanie static_foo(123)
A.static_foo(123) # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class MyABC(object):
    __metaclass__ = ABC

    @abstractmethod
    def my_abstract_method(self):
        print("Abstract")

class A(ABC):
    pass

class B(A):
    pass
    
ABC.register(A)
print(issubclass(A, ABC))

ABC.register(B)
print(issubclass(B, ABC))

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class D(object):

    def __init__(self):
        self._x = None
        self.threshold = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < self.threshold:
            raise ValueError("x can't be lesser than {}".format(self.threshold))
        else:
            self._x = value


d = D()
d.x = 14
print (d.x)

d.x = 2
print (d.x)