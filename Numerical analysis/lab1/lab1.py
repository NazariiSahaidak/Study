# Створюємо розширену матрицю з даної матриці та вектора b.
def augmented_matrix(matrix, b):
    if len(matrix) == len(b):
        for i in range(len(matrix)):
            matrix[i].append(b[i])
        return matrix
    else:
        return -1
# Зводимо матрицю до трикутного вигляду
def upper_triangular_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        # Шукаємо індекс головного елементу.
        pivot_element = abs(matrix[i][i])
        row_of_pivot = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > pivot_element:
                pivot_element = abs(matrix[k][i])
                row_of_pivot = k
        # Переміщуємо рядок з головним елементом на позицію з індексом i.
        for k in range(i, n + 1):
            temporary = matrix[row_of_pivot][k]
            matrix[row_of_pivot][k] = matrix[i][k]
            matrix[i][k] = temporary
        # Перетворюємо всі елементи в стовпці під головним елементом в нулі
        for k in range(i + 1, n):
            m = -matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += m * matrix[i][j]
    return matrix
# Завдяки зворотньому ходу знаходимо вектор-розв'язок x
def solver(matrix):
    n = len(matrix)
    x = [0 for i in range(n)]
    try:
        for i in range(n - 1, -1, -1):
            x[i] = matrix[i][n]/matrix[i][i]
            for k in range(i - 1, -1, -1):
                matrix[k][n] -= matrix[k][i] * x[i]
        return x
    except:
        with open('output.txt', 'w') as file:
            file.write("Система є несумісною або невизначеною.")
        exit()
# Обчислюємо детермінат матриці
def determinant_of_triangular_matrix(matrix):
    determinant = 1
    matrix = upper_triangular_matrix(matrix)
    for i in range(len(matrix)):
        determinant *= matrix[i][i]
    return determinant
# Реалізуємо метод Гауса
def gause_method(matrix, b):
    matrix = augmented_matrix(matrix, b)
    if matrix != -1:
        upper_triangular_matrix(matrix)
        return solver(matrix)
    else:
        with open('output.txt', "w") as file:
            file.write("Система є несумісною.")
        exit()
# Зчитуємо матрицю та вектор з файлу.
with open("input.txt", 'r') as file:
    matrix = file.readlines()
b = [float(i) for i in matrix[-1][matrix[-1].find("=") + 1:].split()]
del matrix[-1]
matrix = [[int(i) for i in j.split()] for j in matrix]
# Обчислення результатів.
x = ', '.join(str(i) for i in gause_method(matrix, b))
determinant = str(determinant_of_triangular_matrix(matrix))
# Записуємо результати виконання у файл.
with open('output.txt', 'w') as file:
    file.write("Розв'язком системи є вектор x(" + x + ").\n")
    file.write("Детермінант заданої матриці рівний: " + determinant + ".")