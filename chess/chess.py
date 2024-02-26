class Chessboard:
    PIECE_MAPPING = {
        6: '♔', 5: '♕', 4: '♖', 3: '♗', 2: '♘', 1: '♙',
         0: '·',
         -1: '♟',  -2: '♞',  -3: '♝',  -4: '♜',  -5: '♛',  -6: '♚'
    }

    def __init__(self):
        # Инициализация начального распределения фигур на доске
        self.board = [
            [5, 2, 3, 4, 6, 3, 2, 5],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-5, -2, -3, -4, -6, -3, -2, -5]
        ]
        self.move_history = []

    def display(self):
        # Вывод заголовков столбцов
        print("  a b c d e f g h")
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
        print(from_row, from_col, to_row,to_col)




        # Сохранение хода в историю
        self.move_history.append((from_where, to_where))

        # Проверка правил для каждой фигуры
        piece = self.board[from_row][from_col]
        if piece == 1:
            if (self.board[to_row][to_col] == 0 and ((to_row - from_row) == 1 and (to_col == from_col))):
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = 0
        elif piece == -1:  # Пешка
            if (self.board[to_row][to_col] == 0 and ((to_row - from_row) == -1 and (to_col == from_col))):
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = 0
            else:
                print("Неверный ход для пешки. Пожалуйста, проверьте шахматные правила.")
        
        if piece == 2 or piece == -2: # Конь
            if (self.board[to_row][to_col] == 0 and (((to_row - from_row) == 2 or (to_row - from_row) == -2) and ((to_col == from_col) == 1 or (to_col == from_col) == -1))):
                self.board[to_row][to_col] = piece
                self.board[from_row][from_col] = 0
            else:
                print("Неверный ход для коня. Пожалуйста, проверьте шахматные правила.")

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
