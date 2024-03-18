# quicksort

import random 

array = [13, 6, 8, 10, 7, 9]

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