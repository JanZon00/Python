from functools import singledispatch, singledispatchmethod

class Negator:
    @singledispatchmethod
    def calc(self, arg):
        raise NotImplementedError("Cannot resolve")

    @calc.register
    def _(self, arg: int):
        return type(arg)
    
    @calc.register
    def _(self, arg: float):
        return type(arg)
    
    @calc.register
    def _(self, arg: str):
        return type(arg)
    
    @calc.register
    def _(self, arg: bool):
        return type(arg)


a = Negator()
print(a.calc(12))
print(a.calc(True))
print(a.calc(1.5))
print(a.calc("Ala"))


@singledispatch
def fun(arg):
    print(arg)
    
@fun.register(float)
def _(arg1, arg2):
    print(arg1 + arg2)

@fun.register(int)
def _(arg1, arg2):
    print(arg1 + arg2)

@fun.register(str)
def _(arg1, arg2):
    print(arg1 + arg2)
        
        
a = 1.5
b = 1.7
fun(a, b)
print("-----------")
a = 2
b = 4
fun(a, b)
print("-----------")
a = "Hello"
b = " World"
fun(a, b)