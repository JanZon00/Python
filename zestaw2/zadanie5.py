def fun(N) :
    indexes = []
    print(bin(N))
    binary = str(bin(N)[2:])
    print(binary)

    for b in range(0, len(binary)):
        if(binary[b] == '1'):
            indexes.append(b)
    print(indexes)
    
    przerwa = 0
    length = len(indexes)
    for i in range(0, length - 1):
        if length > 1 :
            nowa_przerwa = indexes[i + 1] - indexes[i] - 1
            if nowa_przerwa > przerwa:
                przerwa = nowa_przerwa
    return przerwa            

x = int(input("X : "))
print(fun(x))

