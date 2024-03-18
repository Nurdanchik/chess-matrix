# quicksort

import random 

array = [random.randint(0, 10) for _ in range(10)]

def bubbleSort(arr):
    if len(arr) <= 1:
        return arr 
    
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):

            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    
    arr = set(arr)
    arr = list(arr)

    return arr 

print(bubbleSort(array))