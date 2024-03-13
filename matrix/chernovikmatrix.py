# size  = int(input())
# array = []
# for i in range(size):
#     array.append([])
#     for j in range(size):
#         if array[i] == 0:
#             array[i].append(1)
#         elif array[i] =! 0:
#             array[i].append(0)
#         elif array[i] == -1:
#             array[i][1,-1].append(0)
        
# print(array)

# size = int(input())
# array = []

# for i in range(size):
#     array.append([])
#     for j in range(size):
#         if i == 0 or i == size - 1:
#             array[i].append(1)
#         elif j == 0 or j == size - 1:
#             array[i].append(1)
#         else:
#             array[i].append(0)


# for j in array:
#     print(j)

# from random import randint
# import random

# size = 6
# array = []
# sum3x3 = 0

# for i in range(size):
#     array.append([])
#     for j in range(size):
#         array[i].append(random.randint(1,50))

# for j in array:
#     print(j)

# column1 = 0
# column2 = 2
# def findbiggest3x3(column1,column2):
#     for i in range([column1],[column2]):
#         for j in range([column1],[column2]):
#             array[i][j]+=sum3x3
#             continue
    
#     column1, column2 += 1
    

# sum = 0
# biggests3x3 = []
# for i in range(size):
#     for j in range(size):
#         if (i + 3 >= size):
#             break
#         if j + 3 >= size:
#             break
        
#         sum2=0
#         array2 = []
#         for k in range(i, i+3):
#             array2.append([])
#             for m in range(j, j+3):
#                 sum2 += array[k][m]
#                 array2[k - i].append(array[k][m])


#         if (sum2 > sum):
#             sum = sum2
#             biggests3x3 = array2

# print(sum,biggests3x3)


        


# target = 4
# answer = False 

# for i in range(size):
#     for j in range(size):
#         if array[i][j] == target:
#             answer = True

# print(answer)