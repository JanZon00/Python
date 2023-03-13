levels = []

def elementLevel(l, x):
    for i in l :
        if isinstance(i, list) :
            elementLevel(i, x+1)
        else:
            levels.append(x)  

def findMostInner(l, y):
    for i in l :
        if isinstance(i, list) :
            if y+1 == max_level :
                i.append(max(i) + 1)
            findMostInner(i, y+1)
       
l = [1, [2, 3], [4, [5, [6,[7,8],[9, 10], 11], 12], [13, 14], 15]]
print(l)
x = y = 0
elementLevel(l, x)
max_level = max(levels)

if max_level == 0 :
    l.append(max(l) + 1)
else:    
    findMostInner(l, y)
    
print(l)

