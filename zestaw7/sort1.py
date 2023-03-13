import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  # liczba elementów, można zmieniać
FPS = 60  # klatki na sekundę do parametru interval 

tablica = MonitorowanaTablica(0, 1000, N, "R") # zbadaj też opcje: "S", "A", "T"

###############################################
############ Przykład: Insertion Sort #########
def insertionsort(L, left, right):
    t0 = time.perf_counter()
    while (left+1 < right):
        j = left+1
        while ((j > 0) and (L[j-1] > L[j])):
            temp = L[j-1]
            L[j-1] = L[j]
            L[j] = temp
            j -= 1

        left += 1
    delta_t = time.perf_counter() - t0
    return delta_t

############## BUBBLE ##########################
def bubblesort():
    t0 = time.perf_counter()
    for i in range(0, len(tablica)-1):
        for j in range(0, len(tablica)-1 - i):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
                
    delta_t = time.perf_counter() - t0
    return delta_t

############## SHELL ##########################
def shellsort():
    t0 = time.perf_counter()
    left = 0
    right = len(tablica)-1
    h = 1
    while h <= (right-left) // 9:
        h = 3*h+1
    while h > 0:
        for i in range(left+h, right+1):
            j = i
            item = tablica[i]
            while j >= left+h and item < tablica[j-h]:
                tablica[j] = tablica[j-h]
                j = j-h
            tablica[j] = item
        h = h // 3
    delta_t = time.perf_counter() - t0
    return delta_t 

############## MERGE ##########################
def mergesort(L, left, right):
    t0 = time.perf_counter()
    if left < right:
        middle = (left + right) // 2
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)
    
    delta_t = time.perf_counter() - t0
    return delta_t 
                
def merge(L, left, middle, right):
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1

    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1

    for i in range(right - left +1):
        L[left + i] = T[i]
        
############## QUICK SORT ##########################
def quicksort(L, left, right):
    t0 = time.perf_counter()
    if left >= right:
        return
    L[left], L[(left+right) // 2] = L[(left+right) // 2], L[left]
    pivot = left
    for i in range(left + 1, right + 1):
        if L[i] < L[left]:
            pivot += 1
            L[pivot], L[i] = L[i], L[pivot]
    L[left], L[pivot] = L[pivot], L[left]
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

    delta_t = time.perf_counter() - t0
    return delta_t 
 
############## Tim SORT ##########################    

def timsort(array):
    t0 = time.perf_counter()
    min_run = 51
    n = len(array)

    for i in range(0, n, min_run):
        insertionsort(array, i, min((i + min_run - 1), n))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):

            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            left=array[start:midpoint + 1]
            right=array[midpoint + 1:end + 1]
            merged_array = np.concatenate((left, right))
            
            array[start:start + len(merged_array)] = merged_array

        size *= 2

    delta_t = time.perf_counter() - t0
    return delta_t 

#algorytm = "Insertion"
#delta_t = insertionsort(tablica, 0, len(tablica))                

#algorytm = "Bubble"
#delta_t = bubblesort()

#algorytm = "Shell"
#delta_t = shellsort()

#algorytm = "Merge"
#delta_t = mergesort(tablica, 0, len(tablica)-1)

#algorytm = "Quick"
#delta_t = quicksort(tablica, 0, len(tablica)-1)

algorytm = "Tim"
delta_t = timsort(tablica)
###############################################
###############################################
print(f"Sortowanie: {algorytm}")
print(f"Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")
###############################################

# konfiguracja wyświetlania histogramu
plt.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(16, 8))
container = ax.bar(np.arange(0, len(tablica), 1), tablica.pelne_kopie[0], align="edge", width=0.8)
fig.suptitle(f"Sortowanie: {algorytm}")
ax.set(xlabel="Indeks", ylabel="Wartość")
ax.set_xlim([0, N])
txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

# funkcja aktualizująca stan poszczególnych klatek do wyświetlenia
def update(frame):
    txt.set_text(f"Liczba operacji = {frame}")
    for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
        rectangle.set_height(height)
        rectangle.set_color("darkblue")

    idx, op = tablica.aktywnosc(frame)
    if op == "get":
        container.patches[idx].set_color("green")
    elif op == "set":
        container.patches[idx].set_color("red")

    return (txt, *container)

# tu akumulowana jest animacja, wyświetlna komendą show
ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./FPS, repeat=False)
plt.show()