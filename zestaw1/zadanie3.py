l = 12
miarka = "|"

for i in range(0, 12):
    miarka += "...|"
miarka += "\n"

for i in range(0, 13):
    if(i == 9):
        miarka = miarka +  str(i) + "  "
    elif(i > 9):
        miarka = miarka + str(i) + "  "
    else:    
        miarka = miarka +  str(i) + "   "
        
print(miarka)    