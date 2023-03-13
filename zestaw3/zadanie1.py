import json 

with open('tramwaje.json', "r", encoding='utf-8') as read_file: 
    data = json.load(read_file)
    
przystanki = []
trams = {}
trams_sorted = {}  

for linie in data["linia"] :
    if(len(linie) > 1) :
        for value in linie["przystanek"]:
            przystanki.append(value["name"][:-3])
   
    trams[int(linie["name"])] = tuple(i for i in przystanki)
    przystanki = []

with open('tramwaje_out.json', 'w', encoding='utf-8') as file: 
    json.dump(trams, file, ensure_ascii=False)


for key in trams:
    trams_sorted[key] = len(trams[key])
    
trams_sorted = sorted(trams_sorted.items(), key=lambda x: x[1], reverse=True)

for d in trams_sorted :
    print(d, end="\n") 
    
stacje = set()
for key in trams:
    for stacja in trams[key]:
        stacje.add(stacja)
        
print("Ilosc stacji : ", len(stacje))  
