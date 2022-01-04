"""
Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9.
Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины k,
в которой каждый элемент делится на предыдущий.
В задании последовательность - неубывающая.
"""

import sys
from typing import Tuple


def lis_bottom_up(a: list, n: int) -> int:
    """
    LIS BottomUp algorithm
    :param a: list of int numbers,
    :param n: length of list a,
    :return: int, length of the longest increasing subsequence
    """
    d = [0 for _ in range(n)]

    for i in range(n):
        d[i] = 1
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])
    return ans


def conditional_lis_bottom_up(a: list, n: int) -> int:
    """
    LIS BottomUp algorithm for a task
    :param a: list of int numbers,
    :param n: length of list a,
    :return: int, length of the longest increasing subsequence
    """
    d = [0 for _ in range(n)]

    for i in range(n):
        d[i] = 1
        for j in range(i):
            if a[j] <= a[i] and d[j] + 1 > d[i] and (a[i] % a[j] == 0):
                d[i] = d[j] + 1
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])
    return ans


def read_input() -> Tuple[int, list]:
    """
    Read input for a task
    :return: int, list of ints
    """
    reader = [map(int, line.split()) for line in sys.stdin]
    n = next(reader[0])
    digits = [next(reader[1]) for _ in range(n)]
    return n, digits


if __name__ == '__main__':
    n, digits = read_input()
    ans = conditional_lis_bottom_up(a=digits, n=n)
    print(ans)
