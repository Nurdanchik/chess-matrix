class Chessboard:
    PIECE_MAPPING = {
        6: '♔', 5: '♕', 4: '♖', 3: '♗', 2: '♘', 1: '♙',
         0: '·',
         -1: '♟',  -2: '♞',  -3: '♝',  -4: '♜',  -5: '♛',  -6: '♚'
    }

    def __init__(self):
        # Инициализация начального распределения фигур на доске
        self.board = [
            [4, 2, 3, 5, 6, 3, 2, 4],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-4, -2, -3, -6, -5, -3, -2, -4]
        ]
        self.move_history = []
        self.white = True
        self.black = False

    def display(self):
        # Вывод заголовков столбцов
        print("   a b c d e f g h")
        print(" +----------------")


        # Итерация по строкам доски
        for i in range(8):
            # Вывод текущего номера строки
            print(f'{i + 1}|', end=' ')

            # Итерация по столбцам доски
            for j in range(8):
                # Вывод значения из доски для текущей позиции
                print(self.PIECE_MAPPING[self.board[i][j]], end=' ')

            # Завершение строки '|'
            print('|')

        # Вывод разделяющей линии после доски
        print(" +----------------")

    def move(self, from_where, to_where):
        # Проверка корректности входных данных
        if not self.is_valid_input(from_where) or not self.is_valid_input(to_where):
            print("Неверный ввод. Введите координаты в формате 'буква число' (например, 'e2').")
            return

        # Преобразование координат в индексы для обновления доски
        from_row, from_col = int(from_where[1]) - 1, ord(from_where[0]) - ord('a')
        to_row, to_col = int(to_where[1]) - 1, ord(to_where[0]) - ord('a')
        # print(from_row, from_col, to_row,to_col)




        # Сохранение хода в историю
        self.move_history.append((from_where, to_where))

        # Проверка правил для каждой фигуры
        piece = self.board[from_row][from_col]
        # Белые фигуры
        if self.white == True:
            if piece == 1: # Пешка
                if from_row == 1 and to_row == 3 and self.board[2][from_col] == 0:
                    self.board[3][from_col] = piece
                    self.board[from_row][from_col] = 0
                    self.white = False
                    self.black = True
                elif (self.board[to_row][to_col] == 0 and ((to_row - from_row) == 1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False
                elif self.board[to_row][to_col] != 0 and ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False
                else:
                    print("Неверный ход для пешки. Пожалуйста, проверьте шахматные правила.")

            if piece == 2: # Конь
                if (self.board[to_row][to_col] <= 0 and (((abs(to_row - from_row) == 2) and (abs(to_col - from_col) == 1)) or ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 2)))) or (self.board[to_row][to_col] == 0 and (((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 2)) or ((abs(to_row - from_row) == 2) and (abs(to_col - from_col) == 1)))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False
                else:
                    print("Неверный ход для коня. Пожалуйста, проверьте шахматные правила.")

            if piece == 3: # Слон белых
                if self.board[to_row][to_col] <= 0:
                    is_move = False

                    # Проверка влево вверх
                    x, y = from_row - 1, from_col - 1
                    while x >= 0 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y -= 1

                    # Проверка вправо вверх
                    x, y = from_row - 1, from_col + 1
                    while x >= 0 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y += 1

                    # Проверка вниз влево
                    x, y = from_row + 1, from_col - 1
                    while x <= 7 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y -= 1

                    # Проверка вниз вправо
                    x, y = from_row + 1, from_col + 1
                    while x <= 7 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.black = True
                        self.white = False
                    else:
                        print("Неверный ход для слона. Пожалуйста, проверьте шахматные правила.")

            if piece == 4:  # Ладья
                if self.board[to_row][to_col] <= 0:
                    is_move = False

                    # Проверка влево
                    x, y = from_row, from_col - 1
                    while y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y -= 1

                    # Проверка вправо
                    x, y = from_row, from_col + 1
                    while y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y += 1

                    # Проверка вверх
                    x, y = from_row - 1, from_col
                    while x >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1

                    # Проверка вниз
                    x, y = from_row + 1, from_col
                    while x <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.black = True
                        self.white = False
                    else:
                        print("Неверный ход для ладьи. Пожалуйста, проверьте шахматные правила.")

            if piece == 5:
                if self.board[to_row][to_col] <= 0:
                    is_move = False

                    # Проверка влево вверх
                    x, y = from_row - 1, from_col - 1
                    while x >= 0 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y -= 1

                    # Проверка вправо вверх
                    x, y = from_row - 1, from_col + 1
                    while x >= 0 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y += 1

                    # Проверка вниз влево
                    x, y = from_row + 1, from_col - 1
                    while x <= 7 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y -= 1

                    # Проверка вниз вправо
                    x, y = from_row + 1, from_col + 1
                    while x <= 7 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y += 1

                    # Проверка влево
                    x, y = from_row, from_col - 1
                    while y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y -= 1

                    # Проверка вправо
                    x, y = from_row, from_col + 1
                    while y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y += 1

                    # Проверка вверх
                    x, y = from_row - 1, from_col
                    while x >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1

                    # Проверка вниз
                    x, y = from_row + 1, from_col
                    while x <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.black = True
                        self.white = False
                    
                    else:
                        print("Неверный ход для ферзя. Пожалуйста, проверьте шахматные правила.")

            if piece == 6:
                if (self.board[to_row][to_col] <= 0 and ((to_row - from_row) == 1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False
                    
                elif (self.board[to_row][to_col] <= 0 and ((to_row - from_row) == -1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False

                elif self.board[to_row][to_col] <= 0 and ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False

                elif (self.board[to_row][to_col] == 0 and ((to_row == from_row) and (to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False

                elif (self.board[to_row][to_col] == 0 and ((to_row == from_row) and (to_col - from_col) == - 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = True
                    self.white = False
                # if (self.board[to_row][to_col] <= 0 and (abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 1)):
                #     self.board[to_row][to_col] = piece
                #     self.board[from_row][from_col] = 0
                #     self.black = True
                #     self.white = False
                # # Проверка обычных ходов вперед и назад
                # elif (self.board[to_row][to_col] <= 0 and (to_row - from_row == 1) and (to_col == from_col)):
                #     self.board[to_row][to_col] = piece
                #     self.board[from_row][from_col] = 0
                #     self.black = True
                #     self.white = False
                # elif (self.board[to_row][to_col] <= 0 and (to_row - from_row == -1) and (to_col == from_col)):
                #     self.board[to_row][to_col] = piece
                #     self.board[from_row][from_col] = 0
                #     self.black = True
                #     self.white = False
                # # Проверка хода влево
                # elif (self.board[to_row][to_col] <= 0 and (to_row == from_row and to_col - from_col == -1)):
                #     self.board[to_row][to_col] = piece
                #     self.board[from_row][from_col] = 0
                #     self.black = True
                #     self.white = False
                # # Проверка хода вправо
                # elif (self.board[to_row][to_col] <= 0 and (to_row == from_row and to_col - from_col == 1)):
                #     self.board[to_row][to_col] = piece
                #     self.board[from_row][from_col] = 0
                #     self.black = True
                #     self.white = False


                else:
                    print('Неправильный ход для короля.')

        else:
            print('Ход черных.')

        # else:
        #     print('Не твоя очередь ходить. Очередь черных.')

        if self.black == True:
            if piece == -1:  # Пешка
                if from_row == 6 and to_row == 4 and self.board[5][from_col] == 0:
                    self.board[4][from_col] = piece
                    self.board[from_row][from_col] = 0
                    self.white = True
                    self.black = False
                elif (self.board[to_row][to_col] == 0 and ((to_row - from_row) == -1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.white = True
                    self.black = False
                elif self.board[to_row][to_col] >= 0 and ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.white = True
                    self.black = False
                else:
                    print("Неверный ход для пешки. Пожалуйста, проверьте шахматные правила.")

            if piece == -2: # Конь
                if (self.board[to_row][to_col] >= 0 and (((abs(to_row - from_row) == 2) and (abs(to_col - from_col) == 1)) or ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 2)))) or (self.board[to_row][to_col] == 0 and (((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 2)) or ((abs(to_row - from_row) == 2) and (abs(to_col - from_col) == 1)))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.white = True
                    self.black = False
                else:
                    print("Неверный ход для коня. Пожалуйста, проверьте шахматные правила.")

            if piece == -3: # Слон
                if self.board[to_row][to_col] >= 0:
                    is_move = False

                    # Проверка влево вверх
                    x, y = from_row - 1, from_col - 1
                    while x >= 0 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y -= 1

                    # Проверка вправо вверх
                    x, y = from_row - 1, from_col + 1
                    while x >= 0 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y += 1

                    # Проверка вниз влево
                    x, y = from_row + 1, from_col - 1
                    while x <= 7 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y -= 1

                    # Проверка вниз вправо
                    x, y = from_row + 1, from_col + 1
                    while x <= 7 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.white = True
                        self.black = False
                    else:
                        print("Неверный ход для слона. Пожалуйста, проверьте шахматные правила.")

            if piece == -4:  # Ладья
                if self.board[to_row][to_col] >= 0:
                    is_move = False

                    # Проверка влево
                    x, y = from_row, from_col - 1
                    while y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y -= 1

                    # Проверка вправо
                    x, y = from_row, from_col + 1
                    while y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y += 1

                    # Проверка вверх
                    x, y = from_row - 1, from_col
                    while x >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1

                    # Проверка вниз
                    x, y = from_row + 1, from_col
                    while x <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.white = True
                        self.black = False
                    else:
                        print("Неверный ход для ладьи. Пожалуйста, проверьте шахматные правила.")
                
            if piece == -5:
                if self.board[to_row][to_col] >= 0:
                    is_move = False

                    # Проверка влево вверх
                    x, y = from_row - 1, from_col - 1
                    while x >= 0 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y -= 1

                    # Проверка вправо вверх
                    x, y = from_row - 1, from_col + 1
                    while x >= 0 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1
                        y += 1

                    # Проверка вниз влево
                    x, y = from_row + 1, from_col - 1
                    while x <= 7 and y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y -= 1

                    # Проверка вниз вправо
                    x, y = from_row + 1, from_col + 1
                    while x <= 7 and y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1
                        y += 1

                    # Проверка влево
                    x, y = from_row, from_col - 1
                    while y >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y -= 1

                    # Проверка вправо
                    x, y = from_row, from_col + 1
                    while y <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        y += 1

                    # Проверка вверх
                    x, y = from_row - 1, from_col
                    while x >= 0:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x -= 1

                    # Проверка вниз
                    x, y = from_row + 1, from_col
                    while x <= 7:
                        if x == to_row and y == to_col:
                            is_move = True
                        if self.board[x][y] != 0:
                            break
                        x += 1

                    if is_move:
                        self.board[to_row][to_col] = piece
                        self.board[from_row][from_col] = 0
                        self.white = True
                        self.black = False
                    
                    else:
                        print("Неверный ход для ферзя. Пожалуйста, проверьте шахматные правила.")

            if piece == -6:
                if (self.board[to_row][to_col] <= 0 and ((to_row - from_row) == 1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = False
                    self.white = True
                    
                elif (self.board[to_row][to_col] <= 0 and ((to_row - from_row) == -1 and (to_col == from_col))):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = False
                    self.white = True

                elif self.board[to_row][to_col] <= 0 and ((abs(to_row - from_row) == 1) and (abs(to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = False
                    self.white = True

                elif (self.board[to_row][to_col] == 0 and ((to_row == from_row) and (to_col - from_col) == 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = False
                    self.white = True

                elif (self.board[to_row][to_col] == 0 and ((to_row == from_row) and (to_col - from_col) == - 1)):
                    self.board[to_row][to_col] = piece
                    self.board[from_row][from_col] = 0
                    self.black = False
                    self.white = True

                else:
                    print('Неправильный ход для короля.')

        else:
            print('Ход белых.')
        # else:
        #     print('Не твоя очередь ходить. Очередь белых.')

    def is_valid_input(self, position):
        # Проверка, что ввод содержит два символа: букву и цифру
        return len(position) == 2 and position[0].isalpha() and position[1].isdigit()


# Создание экземпляра класса Chessboard
chessboard = Chessboard()

# Отображение начальной доски
chessboard.display()

# Продолжение игры
while True:
    # Вызов метода move для передвижения фигуры
    from_where = input("Откуда (например, 'e2'): ")
    to_where = input("Куда (например, 'e4'): ")
    chessboard.move(from_where, to_where)

    # Отображение обновленной доски
    chessboard.display()

    # Отображение истории ходов
    print("История ходов:", chessboard.move_history)