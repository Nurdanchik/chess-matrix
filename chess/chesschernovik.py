# # def move():
# #     print('Введи куда ты хочешь подвинуть фигуру в формате (е4 - е5)')
# #     for i in range(3):
# #         i = 0
# #         i+=1
# #         print(f'{i}...')
# #         time.sleep(1)
# #     fromwhere = input('Откуда: ')
# #     towhere = input('Куда: ')


# import time

# def move(chess_board):
#     print('Введи куда ты хочешь подвинуть фигуру в формате (е4 - е5)')
#     for i in range(3, 0, -1):
#         print(f'{i}...')
#         time.sleep(1)

#     fromwhere = input('Откуда: ')
#     towhere = input('Куда: ')

#     # Извлечение координат из ввода
#     start_col, start_row = ord(fromwhere[0].lower()) - ord('a'), 8 - int(fromwhere[1])
#     end_col, end_row = ord(towhere[0].lower()) - ord('a'), 8 - int(towhere[1])

#     # Проверка корректности координат
#     if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
#         print('Некорректные координаты. Попробуйте снова.')
#         return

#     # Проверка, что на начальной клетке есть фигура
#     if chess_board[start_row][start_col] == ' ' or chess_board[start_row][start_col] == 'P':
#         print('На выбранной клетке нет фигуры. Попробуйте снова.')
#         return

#     # Дополнительные проверки правил шахмат могут быть добавлены здесь

#     # Обновление доски
#     chess_board[end_row][end_col] = chess_board[start_row][start_col]
#     chess_board[start_row][start_col] = ' '

#     print('Ход сделан успешно.')

# # Пример использования
# move(chess_board)
# print(chess_board)

