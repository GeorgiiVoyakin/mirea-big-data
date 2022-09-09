import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

def numbers_squares() -> None:
    print('Введите числа: ', end='')
    number = int(input())
    sum = number
    squares = number ** 2
    while sum != 0:
        number = int(input('> '))
        sum += number
        squares += number ** 2
    print(squares)


def print_numbers_n_times() -> None:
    n = int(input('Введите число: '))
    if n < 0:
        print('Число должно быть неотрицательным!')
    result = []
    i = 1
    while len(result) < n:
        for _ in range(i):
            result.append(i)
        i += 1
    print(result)

def expand_matrix_to_vector() -> None:
    matrix = np.random.randint(10, size=(3, 3))
    print('Исходная матрица:')
    print(matrix)
    vector = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            vector.append(matrix[i][j])
    print('Полученный вектор: ', vector)

def create_dict() -> None:
    a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    result = dict()
    for i in range(len(b)):
        if b[i] in result:
            result[b[i]] += a[i]
        else:
            result[b[i]] = a[i]
    print(result)

def california() -> None:
    data = fetch_california_housing(as_frame=True)
    print(data)
    # pd.concat([data['target_names'], data['target']], axis=1)
    data.info()
    data.isna()


def main():
    separator = '=' * 50
    numbers_squares()
    print(separator)
    print_numbers_n_times()
    print(separator)
    expand_matrix_to_vector()
    print(separator)
    create_dict()
    print(separator)
    california()


if __name__ == '__main__':
    main()
