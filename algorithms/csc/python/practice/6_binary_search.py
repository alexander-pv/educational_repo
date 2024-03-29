import sys
from bisect import bisect_left


def find_pos(xs, query):
    """
    Тривиальный пример для проверки найденных индексов
    :param xs:
    :param query:
    :return: int
    """
    try:
        return xs.index(query) + 1
    except ValueError:
        return -1


def binary_pos(xs, query):
    # Invariant: lo <= pos < hi
    lo, hi = 0, len(xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:
            hi = mid      # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1  # [mid + 1, hi)
        else:
            return mid + 1
    return -1


def binary_pos2(xs, query):

    lo = bisect_left(xs, query)
    # i < lo: xs[i] < query
    # i > lo: xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1
    else:
        return -1


def test_binary_pos():
    """
    Рассматриваем краевые случаи
    :return: None
    """
    assert binary_pos([], 42) == -1
    assert binary_pos([42], 42) == 1
    assert binary_pos([42], 1) == -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")


if __name__ == '__main__':
    test_binary_pos()
