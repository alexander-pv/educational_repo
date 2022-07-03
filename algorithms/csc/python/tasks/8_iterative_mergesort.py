"""
Алгоритм сортировки MergeSort с применением кучи.
"""

import heapq


def merge(array_a: list, array_b: list) -> list:
    """
    Merge function of two lists for MergeSort algorithm
    :param array_a: list
    :param array_b: list
    :return: list
    """
    merged_list = []
    len_array_a = len(array_a)
    len_array_b = len(array_b)

    while min(len_array_a, len_array_b) > 0:

        if array_a[0] < array_b[0]:
            merged_list.append(array_a[0])
            array_a = array_a[1:]
            len_array_a -= 1
        else:
            merged_list.append(array_b[0])
            array_b = array_b[1:]
            len_array_b -= 1

    if array_a:
        merged_list.extend(array_a)
    else:
        merged_list.extend(array_b)

    return merged_list


def iterative_mergesort(array: list) -> list:
    """
    Iterative MergeSort algorithm
    :param array: list of unsorted ints
    :return: list
    """
    heap = []
    for i in range(len(array)):
        heapq.heappush(heap, [array[i]])

    while len(heap) > 1:
        heapq.heappush(heap, merge(array_a=heapq.heappop(heap),
                                   array_b=heapq.heappop(heap)
                                   )
                       )
    return heapq.heappop(heap)


if __name__ == '__main__':
    print('Sorted: ', iterative_mergesort(array=[int(i) for i in input().split()]))
