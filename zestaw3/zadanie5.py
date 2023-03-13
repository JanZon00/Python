class Bug:  
    '''Demonstracja dzialania klas, obiektow,
konstruktora, destruktora, metody __str__.'''
    
    licznik = 0
    def __init__(self):
        Bug.licznik += 1
        
    def __del__(self):
        Bug.licznik -= 1
        print("Koniec ", self.licznik, id(self))
        
    def __str__(self):
        result = str(self.licznik) + " : " + str(id(self))
        return(result)


print(Bug.__doc__)
#obj = Bug()
#obj2 = Bug()
#obj.__str__()
#del obj
#obj2.__str__()
#obj3 = Bug()
#obj3.__str__()

bugs = [] 
for i in range(100): 
    bugs.append(Bug())
    Bug.__str__
    print(bugs[-1])