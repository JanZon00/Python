import itertools

print("Input  4 digits : ")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
n = int(input("n = "))

L = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1): 
            l = [i, j, k]
            L.append(l)
 
L2 = [l for l in L if l[0] + l[1] + l[2] != n]        
print(L2)