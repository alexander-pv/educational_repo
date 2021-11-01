"""
Первая строка содержит число 1≤n≤10^4, вторая — n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""

import random
import sys
import cProfile


def count_sort(array_a: list, n: int) -> list:
    """
    Simple count sort algorithm
    :param array_a: list
    :param n: int
    :return: int
    """
    m = 10
    array_b = [0 for _ in range(m+1)]
    array_sorted = [0 for _ in range(n + 1)]

    for j in range(n):
        array_b[array_a[j]] += 1

    for i in range(1, m + 1):
        array_b[i] = array_b[i] + array_b[i - 1]

    for j in range(n - 1, -1, -1):
        array_sorted[array_b[array_a[j]]] = array_a[j]
        array_b[array_a[j]] -= 1

    return array_sorted


def test_random(n: int = 10000, n_trials=10) -> None:
    for _ in range(n_trials):
        input_list = [random.randint(1, 10) for _ in range(n)]
        count_sort(input_list, n)


def main():
    reader = [map(int, line.split()) for line in sys.stdin]
    n = next(reader[0])
    digits = [next(reader[1]) for _ in range(n)]
    sorted_digits = count_sort(digits, n)
    sorted_digits = [i for i in sorted_digits if 0 < i <= 1e4]
    [print(i, end=" ") for i in sorted_digits]


if __name__ == '__main__':
    main()
    #cProfile.run('test_random()')
