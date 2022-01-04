"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000  — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8  по модулю.

Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Для данной задачи необходимо использовать алгоритм быстрой сортировки QuickSort.
"""
import bisect
import cProfile
import random
import sys
from typing import Tuple


def partition3split(a: list, l: int, r: int) -> Tuple[int, int]:
    """
    Partition function for QuickSort algorithm with 3-way split
    :param a: list of ints
    :param l:     int
    :param r:     int
    :return: int
    """

    x = a[l]
    le = l  # elements that are less than x
    ge = r  # elements that are greater than x

    i = le
    while i <= ge:
        if a[i] < x:
            a[le], a[i] = a[i], a[le]
            le += 1
        elif a[i] > x:
            a[ge], a[i] = a[i], a[ge]
            ge -= 1
            i -= 1
        i += 1
    return le, ge


def quick_sort(a: list, n: int,  l: int, r: int) -> None:
    """
    QuickSort with 3-way split for average performance speedup
    :param a: list
    :param n: int
    :param l: int
    :param r: int
    :return: None
    """
    if l >= r:
        return
    else:
        c = (a[0] + a[n//2] + a[n-1])//3
        a[l], a[c] = a[c], a[l]
        m1, m2 = partition3split(a, l, r)
        quick_sort(a, n, l, m1 - 1)
        quick_sort(a, n, m2 + 1, r)


def random_quick_sort(a: list, l: int, r: int) -> None:
    """
    QuickSort with randomization for average performance speedup
    :param a: list
    :param l: int
    :param r: int
    :return: None
    """
    if l >= r:
        return
    else:
        c = random.randint(l, r)
        a[l], a[c] = a[c], a[l]
        m1, m2 = partition3split(a, l, r)
        random_quick_sort(a, l, m1 - 1)
        random_quick_sort(a, m2 + 1, r)


def dots_bin_search(borders, dot, b_type):
    """

    :param borders: list of ints
    :param dot: int
    :param b_type:
    :return: "left", "right"
    """
    if b_type == "left":
        m = bisect.bisect_right(borders, dot)
    elif b_type == "right":
        m = bisect.bisect_left(borders, dot)
    return m


def count_segments_simple(starts: list, ends: list, value: int) -> int:
    """
    Count segments which covers a passed value
    :param starts: list
    :param ends:   list
    :param value:  value
    :return: int
    """

    acc = 0

    for left, right in zip(starts, ends):

        if left <= value and right < value:
            pass
        elif left <= value <= right:
            acc += 1
        else:
            break
    return acc


def count_segments(starts: list, ends: list, value: int) -> int:
    """
    Count segments which covers a passed value
    :param starts: list
    :param ends:   list
    :param value:  value
    :return: int
    """

    l_count = dots_bin_search(borders=starts, dot=value, b_type="left")
    r_count = dots_bin_search(borders=ends, dot=value, b_type="right")
    return l_count - r_count


def main() -> None:
    reader = (map(int, line.split()) for line in sys.stdin)
    n, m = next(reader)
    segments = [list(next(reader)) for _ in range(n)]
    points = [p for p in next(reader)]
    starts_list, ends_list = [s[0] for s in segments], [s[1] for s in segments]

    random_quick_sort(a=starts_list, l=0, r=len(starts_list) - 1)
    random_quick_sort(a=ends_list, l=0, r=len(ends_list) - 1)

    result = [count_segments(starts=starts_list, ends=ends_list, value=v) for v in points]
    for r in result:
        print(r, end=" ")


def test_random(n=50000, n_points=10000):
    starts_list = [random.randint(-100, 100) for _ in range(n)]
    ends_list = [x + random.randint(1, 100) for x in starts_list]
    points = [random.randint(-1000, 1000) for p in range(n_points)]

    random_quick_sort(a=starts_list, l=0, r=len(starts_list) - 1)
    random_quick_sort(a=ends_list, l=0, r=len(ends_list) - 1)
    # quick_sort(a=starts_list, n=n, l=0, r=len(starts_list) - 1)
    # quick_sort(a=ends_list, n=n, l=0, r=len(ends_list) - 1)

    result = [count_segments(starts=starts_list, ends=ends_list, value=v) for v in points]
    for r in result:
        print(r, end=" ")


if __name__ == '__main__':
    main()
    #cProfile.run('test_random()')
