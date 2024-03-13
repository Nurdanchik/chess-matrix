# array = []
# array2 = []

# size = int(input('Размер число х число: '))

# # Fill the first array with values (i + 1)
# for i in range(size):
#     array.append([])
#     for j in range(size):
#         array[i].append(i + 1)

# # Fill the second array with values (i - 1)
# for i in range(size):
#     array2.append([])
#     for j in range(size):
#         array2[i].append(i - 1)

# # Print the first array
# print("Array 1:")
# for i in array:
#     print(i)

# # Print the second array
# print("Array 2:")
# for j in array2:
#     print(j)

# class TicTacToe:

#     pairs = {1:'X',
#              0:'O'} 

#     def __init__(self):
#         self.board = [
#             [0, 0, 0]
#             [0, 0, 0]
#             [0, 0, 0]
#         ]

#     def display(self):
#         for i in self.pairs:
#             print(i)

#     def move(self):
#         to_row = int(input('Row: '))
#         to_col = int(input('Column: '))

# display = TicTacToe()

# print(display.display())