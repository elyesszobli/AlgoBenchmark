import time
import csv

def LireFichier(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def Pivot(arr, debut, fin):
    i = (debut-1)
    pivot = arr[fin]
    for j in range(debut, fin):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[fin] = arr[fin], arr[i+1]
    return (i+1)

def quickSort(arr, debut, fin):
    if len(arr) == 1:
        return arr
    if debut < fin:
        p = Pivot(arr, debut, fin)
        quickSort(arr, debut, p-1)
        quickSort(arr, p+1, fin)



def write_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Nom fichier", "Temps"])
        writer.writerows(results)

NomFichiers = ["fich1.txt", "fich2.txt", "fich3.txt","fich4.txt"]
algorithms = ["selectionSort", "bubbleSort", "insertionSort", "quickSort"]
results = []

for NomFichier in NomFichiers:
    lignes = LireFichier(NomFichier)
    for algorithm in algorithms:
        start_time = time.time()
        if algorithm == "selectionSort":
            selectionSort(lignes)
        elif algorithm == "bubbleSort":
            bubbleSort(lignes)
        elif algorithm == "insertionSort":
            insertionSort(lignes)
        elif algorithm == "quickSort":
            quickSort(lignes, 0, len(lignes)-1)
        end_time = time.time()
        Temps = end_time - start_time
        
        results.append([algorithm, NomFichier, Temps])

write_csv(results, "results.csv")
