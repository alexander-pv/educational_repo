"""
Куча на массиве

Первая строка входа содержит число операций. Каждая из последующих n строк задают операцию одного
из следующих двух типов: Insert x, ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
"""


class MaxHeap:

    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.heap_size = 0

    def parent(self, i: int) -> int:
        out = (i - 1) // 2
        assert out >= 0
        return out

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def sift_up(self, i: int):
        while i > 0 and self.array[self.parent(i)] < self.array[i]:
            self.array[self.parent(i)], self.array[i] = self.array[i], self.array[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i: int):
        max_idx = i
        l, r = self.left_child(i), self.right_child(i)
        if l < self.heap_size and self.array[l] > self.array[max_idx]:
            max_idx = l
        if r < self.heap_size and self.array[r] > self.array[max_idx]:
            max_idx = r
        if i != max_idx:
            self.array[i], self.array[max_idx] = self.array[max_idx], self.array[i]
            self.sift_down(max_idx)

    def insert(self, x: int):
        if self.capacity == self.heap_size:
            raise ValueError('Limit of Heap capacity')
        else:
            self.heap_size += 1
            self.array.insert(self.heap_size - 1, x)
            self.sift_up(self.heap_size - 1)

    def extract_max(self) -> int:
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


if __name__ == '__main__':

    n = int(input())
    heap = MaxHeap(100)
    for _ in range(n):
        op = input()
        if op == 'ExtractMax':
            res = heap.extract_max()
            if res:
                print(res)
        else:
            val = int(op.split(' ')[-1])
            heap.insert(val)
