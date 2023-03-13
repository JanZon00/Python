def odwracanie(L, left, right) :
    
    idx = left
    for i in range(left, right):
        if left == right :
            break
        else:
            for j in range(0, right-left):
                temp = L[idx+1]
                L[idx+1] = L[idx]
                L[idx] = temp
                idx += 1
                
            idx = left
            right -= 1    
    return L

def odwracanieRekurencja(L):
    if len(L) == 0:
        return []
    return [L[-1]] + odwracanieRekurencja(L[:-1])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list:", L)

left, right = -1, -1

while(not((left>=0 and right >= 0) and (right >= left) and (right <= len(L) - 1))) :
    left = int(input("Podaj zakres lewy : "))
    right = int(input("Podaj zakres prawy : "))

listbeg = L[0:left:1]
listend = L[right+1:len(L)+1:1]      
print("Reversed list (iter):",odwracanie(L, left, right)) #iteracyjnie

reversedList = (odwracanieRekurencja(L[left:right+1]))
print("Reversed list (recur, back to original):",listbeg + reversedList + listend)  #rekurencyjnie