"""
В первой строке даны целое число n  и массив A[1…n] из различных натуральных чисел, не превышающих 10^9 ,
в порядке возрастания, во второй — целое число k и k  натуральных чисел b1,…,bk b_1, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс j , для которого A[j]=b_i, или −1, если такого j нет.

"""


def binary_search(array_a: list, k: int) -> int:
    """
    Simple binary search algorithm
    :param array_a: list, A[1…n]
    :param k:       int,
    :return:        int
    """
    start, end = 0, len(array_a) - 1
    while start <= end:
        m = int(start + (end - start) // 2)

        if array_a[m] == k:
            return m + 1
        elif array_a[m] > k:
            end = m - 1
        else:
            start = m + 1
    return -1


def main() -> None:
    array_a = [int(i) for i in input().split(' ')][1:]
    array_b = [int(i) for i in input().split(' ')][1:]
    assert array_a == sorted(array_a)

    for k in array_b:
        idx = binary_search(array_a, k)
        print(idx, end=' ')


def test(n_iters=1000, max_len=50, max_val=100):
    import random

    for _ in range(n_iters):
        array_length = random.randint(0, max_len)
        array_a = sorted([random.randint(0, max_val) for i in range(array_length)])
        array_b = [random.randint(0, max_val) for i in range(array_length)]

        print(f'\narray_a: {array_a}\narray_b: {array_b}')
        for k in array_b:
            idx = binary_search(array_a, k)
            print(idx, end=' ')
        print('\n')


if __name__ == '__main__':
    test()
