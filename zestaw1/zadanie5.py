L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 5, 6]

S1 = set()
S1.update(L1)

S2 = set()
S2.update(L2)

print("L1 : ", L1)
print("L2 : ", L2)

cz_wspolna = S1.intersection(S2)
print("Czesc wspolna : ", cz_wspolna)

suma = S1.union(S2)
print("Suma : ", suma)