odd = False

while odd == False:
    podstawa = int(input("Wprowadz dlugosc podstawy trojkata : "))
    if(podstawa %2 != 0):
        odd = True
    
for i in range(int((podstawa + 1)/2)):
    for j in range(podstawa):
        if((i == j or i == 0) or i == podstawa - j - 1):  
            print('*',sep="", end = '')
        else:    
            print(' ',sep="", end = '')    
    print()