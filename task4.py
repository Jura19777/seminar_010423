"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        rows = []
        for row in self.data:
            rows.append("\t".join(str(elem) for elem in row))
        return "\n".join(rows)

    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

print("Первая матрица")
matrix1 = Matrix([[31, 54, 22], [37, 41, 43], [51, 87, 86]])
print(matrix1)

print("Вторая матрица")
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix2)

print("Сложение матриц")
matrix_sum = matrix1.add(matrix2)
print(matrix_sum)