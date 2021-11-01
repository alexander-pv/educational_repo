"""
Первая строка содержит число n, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j] A[i.
(Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве,
упорядоченном по убыванию, инверсию образуют каждые два элемента.)


"""
import bisect
import cProfile
import random
from typing import Tuple


def merge(array_a: list, array_b: list) -> Tuple[list, int]:
    """
    Merge function of two lists for MergeSort algorithm
    :param array_a: list
    :param array_b: list
    :return: list, int
    """
    merged_list = []
    len_array_a = len(array_a)
    len_array_b = len(array_b)
    inversions = 0
    merged_id, a_id, b_id = 0, 0, 0

    while (len_array_a if len_array_a < len_array_b else len_array_b) > 0:

        if array_a[a_id] > array_b[b_id]:
            merged_list[merged_id:] = [array_b[b_id]]
            b_id += 1
            len_array_b -= 1
            merged_id += 1
            inversions += len_array_a

        else:
            merged_list[merged_id:] = [array_a[a_id]]
            a_id += 1
            len_array_a -= 1
            merged_id += 1

    if len_array_a:
        merged_list[merged_id:] = array_a[a_id:]
    else:
        merged_list[merged_id:] = array_b[b_id:]

    return merged_list, inversions


def iterative_mergesort(array: list) -> Tuple[list, int]:
    """
    Iterative MergeSort algorithm customized for the inversions counting task
    :param array: list of unsorted ints
    :return: list, int
    """
    total_inversions = 0
    len_array = len(array)

    while len_array > 1:
        for i in range(len_array - 1, 0, -2):
            a, b = array[i - 1], array[i]
            del array[i]
            array[i - 1], merge_inversions = merge(array_a=a, array_b=b)
            total_inversions += merge_inversions
            len_array -= 1
    return array, total_inversions


def test_task():
    data_tuple = (
        ((2, 3, 9, 2, 9), 2),
        ((7, 6, 5, 4, 3, 2, 1), 21),
        ((1, 2, 3, 5, 4), 1),
        ((10, 8, 6, 2, 4, 5), 12),
        ((1, 9, 8, 1, 4, 1), 8),
        ((6, 2, 3, 7, 5, 8), 4),
        ((6, 4, 5, 0, 0, 2), 11),
        ((8, 9, 10, 7, 4, 0), 12),
        ((1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 3), 15),
        ((42, 42, 70, 79, 29, 85, 47, 81, 96, 3, 25, 52, 49, 84, 95, 17, 49, 7, 9, 76, 77, 79, 32,
          45, 52, 30, 92, 85, 17, 32, 92, 2, 14, 85, 85, 21, 30, 86, 89, 79, 39, 49, 47, 17), 466)
    )
    for data in data_tuple:
        input_data, ans = data
        input_data = [[i] for i in input_data]
        _, total_inv = iterative_mergesort(array=input_data)
        assert ans == total_inv
        print(f"OK: {data}")


def test_time():
    N = 100000
    data = [[random.randint(-1000, 1000)] for _ in range(N)]
    iterative_mergesort(array=data)


if __name__ == '__main__':
    test_task()
    cProfile.run('test_time()')
