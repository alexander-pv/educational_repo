"""
Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
Найдите наибольшую невозрастающую подпоследовательность в A.
В первой строке выведите её длину k, во второй — её индексы.

Дорешать.
"""

import sys
from typing import Tuple


def lnis_bottom_up(a: list, n: int) -> Tuple[int, list]:
    """
    LNIS BottomUp algorithm
    :param a: list of int numbers,
    :param n: length of list a,
    :return: int, tuple of ints
    """
    d = [0 for _ in range(n)]

    for i in range(n):
        d[i] = 1
        for j in range(i):
            if a[j] >= a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    for i in range(n):
        ans = max(ans, d[i])

    print(d)

    last_idx = d.index(ans)
    prev_idx = last_idx
    k = ans
    lnis_idx = [d[last_idx]]

    for i in range(last_idx, -1, -1):

        if d[i] < k and a[i] >= a[prev_idx]:
            lnis_idx.insert(0, i + 1)
            k -= 1
            prev_idx = i

    return ans, lnis_idx


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
    if n > 1:
        ans, lnis_idx = lnis_bottom_up(a=digits, n=n)
    else:
        ans = 1
        lnis_idx = [1]
    print(ans)
    [print(s, end=' ') for s in lnis_idx]
