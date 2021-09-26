"""
Куча на массиве

Первая строка входа содержит число операций. Каждая из последующих n строк задают операцию одного
из следующих двух типов: Insert x, ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
"""


class MaxHeap:
    def __init__(self):
        self.array = []
        self.last_pos = 0
        self.heap_size = 0

    def insert(self, p):
        self.array.append(p)
        self.last_pos = len(self.array) - 1
        self.heap_size += 1
        self.sift_up(self.last_pos)

    def sift_up(self, idx):
        parent_idx = (idx - 1)//2
        if idx > 0:
            node_p = self.array[idx]
            node_parent_p = self.array[parent_idx]
            if node_p > node_parent_p:
                self.array[idx] = node_parent_p
                self.array[parent_idx] = node_p
            self.sift_up(parent_idx)

    def sift_down(self, idx):

        node_p = self.array[idx]

        child0_idx = int(2 * idx + 1)
        child1_idx = int(2 * idx + 2)

        if (child0_idx < self.heap_size) & (child1_idx < self.heap_size):

            node_child0_p = self.array[child0_idx]
            node_child1_p = self.array[child1_idx]

            if node_child0_p > node_child1_p:
                chosen_child = node_child0_p
                child_idx = child0_idx
            else:
                chosen_child = node_child1_p
                child_idx = child1_idx

            if chosen_child > node_p:
                self.array[child_idx] = node_p
                self.array[idx] = chosen_child

            self.sift_down(child_idx)

        elif (child0_idx < self.heap_size) & (child1_idx > self.heap_size):

            chosen_child = self.array[child0_idx]
            child_idx = child0_idx
            if chosen_child > node_p:
                self.array[child_idx] = node_p
                self.array[idx] = chosen_child

            self.sift_down(child_idx)

    def extract_max(self):
        max_val = self.array.pop(0)
        self.heap_size -= 1
        self.last_pos = len(self.array) - 1
        if self.heap_size > 1:
            self.sift_down(0)
            self.sift_up(self.last_pos)
        return max_val


if __name__ == '__main__':

    n = int(input())
    heap = MaxHeap()
    for _ in range(n):
        op = input()
        if op == 'ExtractMax':
            print(heap.extract_max())
        else:
            val = int(op.split(' ')[-1])
            heap.insert(val)
