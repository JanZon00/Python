
m = int(input("Podaj szerokość : "))
n = int(input("Podaj wysokość : "))

layer_frame = ""
layer = ""
rectangle = ""

for i in range(0, m):
    for j in range(0, 4):
        if(j == 0):  
            layer_frame += "+"
        else:    
            layer_frame += "-"
layer_frame += "+\n"
layer += layer_frame

for i in range(0, m):
    for j in range(0, 4):
        if(j == 0):  
            layer += "|"
        else:    
            layer += " "
layer += "|"

for i in range(0, n):
    rectangle = rectangle + "\n" + layer

rectangle = rectangle + "\n" + layer_frame           
print(rectangle)        