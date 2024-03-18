import random 

array = [13, 6, 8, 10, 7, 9]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        n=arr[0]
        lower = []
        greater = []
        
        for i in arr[1:]:
            if i <= n:
                lower.append(i)
            
            elif i > n:
                greater.append(i)
    
    return quicksort(lower)+[n]+quicksort(greater)

print(quicksort(array))