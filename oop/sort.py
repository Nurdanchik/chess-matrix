# class BubbleSort:
#     def __init__(self, array):
#         self.array = array

#     def get_sorted_array(self):
#         return self.sort()

#     def sort(self):
#         for j in range(len(self.array) - 1):
#             for i in range(len(self.array) - 1):
#                 if self.array[i] >= self.array[i + 1]:
#                     self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
#         return self.array

#     def get_original_array(self):
#         return self.array
    
# # Создаем экземпляр класса с произвольным массивом
# bubble_sort_instance = BubbleSort([5, 2, 9, 1, 5, 6])

# # Выводим исходный массив
# print("Исходный массив:", bubble_sort_instance.get_original_array())

# # Вызываем метод сортировки
# bubble_sort_instance.sort()

# # Выводим отсортированный массив
# print("Отсортированный массив:", bubble_sort_instance.get_sorted_array())
class QuickSort:
    def __init__(self, array):
        self.array = array

    def get_sorted_array(self):
        return self.sort()

    def sort(self):
        if len(self.array) <= 1:
            return self.array

        else:
            num = self.array[0]
            lower = [x for x in self.array[1:] if x < num]
            greater = [x for x in self.array[1:] if x > num]
            return self._sort(lower) + [num] + self._sort(greater)

    def _sort(self, arr):
        if len(arr) <= 1:
            return arr

        num = arr[0]
        lower = [x for x in arr[1:] if x < num]
        greater = [x for x in arr[1:] if x > num]
        return self._sort(lower) + [num] + self._sort(greater)

    def get_original_array(self):
        return self.array
    
# Создаем экземпляр класса с произвольным массивом
quick_sort_instance = QuickSort([5, 2, 9, 1, 5, 6])

# Выводим исходный массив
print("Исходный массив:", quick_sort_instance.get_original_array())

# Вызываем метод сортировки
sorted_array = quick_sort_instance.sort()

# Выводим отсортированный массив
print("Отсортированный массив:", sorted_array)
