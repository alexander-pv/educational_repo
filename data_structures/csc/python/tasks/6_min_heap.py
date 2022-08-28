"""
Переставить элементы заданного массива чисел так, чтобы он удовлетворял свойству мин-кучи.

Вход. Массив чисел A[0 . . . n − 1].
Выход. Переставить элементы массива так, чтобы выполнялись неравенства A[i] ≤ A[2i + 1] и A[i] ≤ A[2i + 2] для всех i.

"""


class MinHeap:

    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.heap_size = 0
        self.answer = []

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def sift_up(self, i: int):
        while i > 0 and self.array[self.parent(i)] > self.array[i]:
            self.array[self.parent(i)], self.array[i] = self.array[i], self.array[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i: int):
        min_idx = i
        l, r = self.left_child(i), self.right_child(i)
        if l < self.heap_size and self.array[l] < self.array[min_idx]:
            min_idx = l
        if r < self.heap_size and self.array[r] < self.array[min_idx]:
            min_idx = r
        if i != min_idx:
            self.answer.append((i, min_idx))
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.sift_down(min_idx)

    def insert(self, x: int):
        if self.capacity == self.heap_size:
            raise ValueError('Limit of Heap capacity')
        else:
            self.heap_size += 1
            self.array.insert(self.heap_size - 1, x)
            self.sift_up(self.heap_size - 1)

    def extract_min(self) -> int:
        out = self.array.pop(0)
        self.heap_size -= 1
        if self.heap_size > 0:
            last = self.array.pop(self.heap_size - 1)
            self.array.insert(0, last)
            self.sift_down(0)
        return out

    def build_heap(self, arr: list):
        n = len(arr)
        self.array = arr
        self.heap_size = n
        for i in range(n // 2, -1, -1):
            self.sift_down(i)


def test():
    data = ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    for arr in data:
        min_heap = MinHeap(100)
        min_heap.build_heap(arr)


def run_task():
    n = int(input())
    data = [int(x) for x in input().split(' ')]
    min_heap = MinHeap(n + 1)
    min_heap.build_heap(data)

    swaps = len(min_heap.answer)
    print(swaps)
    if swaps > 0:
        for i, j in min_heap.answer:
            print(i, j)


if __name__ == '__main__':
    test()
    # run_task()
