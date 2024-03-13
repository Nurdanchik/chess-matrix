# quick sort 

import random 

array =[random.randint(0, 9000) for _ in range(10)]

array.append(0)

def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    
    else:
        n = arr[0]
        lower = []
        greater = []

        for num in arr[1:]:
            if num <= n:
                lower.append(num)
            
            elif num > n:
                greater.append(num)

    # return lower + [n]  + greater
    return quicksort(lower) + [n] + quicksort(greater)

print(quicksort(array))