"""

Вычислить высоту данного дерева.

Вход:
Корневое дерево с вершинами {0, . . . , n−1}, заданное как последовательность
parent 0 , . . . , parent n−1 , где parent i — родитель i-й вершины.

Выход:
Высота дерева.

Ограничения: 1 ≤ n ≤ 10^5.
"""

import sys

RECURSION_LIMIT = 10000
sys.setrecursionlimit(RECURSION_LIMIT)


class Node:
    def __init__(self, idx: int, parent: object or None = None):
        self.idx = idx
        self.parent = parent
        self.children = []
        self.is_root = False

    def add_child(self, node) -> None:
        self.children.append(node)

    def get_root(self):
        if self.is_root:
            return self
        else:
            return self.parent.get_root()

    def __repr__(self):
        s = f'{self.idx}'
        if len(self.children) > 0:
            s += '->'
            s_temp = ','.join(child.__repr__() for child in self.children)
            s += f"({s_temp})"
        return s


def get_height(tree: Node) -> int:
    height = 1
    for child in tree.children:
        height = max(height, 1 + get_height(child))
    return height


def build_tree(parents: list or tuple) -> Node:
    nodes = [Node(idx=i) for i in range(len(parents))]
    for node_id, parent_id in enumerate(parents):
        if parent_id == -1:
            nodes[node_id].is_root = True
        else:
            nodes[node_id].parent = nodes[parent_id]
            nodes[parent_id].add_child(nodes[node_id])
    root = nodes[0].get_root()
    return root


def test() -> None:
    examples = (
        (4, -1, 4, 1, 1),
        (-1, 0, 4, 0, 3),
        (9, 7, 5, 5, 2, 9, 9, 9, 2, -1)
    )
    answers = (3, 4, 4)
    for parents, answer in zip(examples, answers):
        tree = build_tree(parents)
        print(tree)
        height = get_height(tree)
        print(height)
        assert height == answer


def run_task() -> None:
    n = int(input())
    parents = [int(x) for x in input().split(' ')]
    tree = build_tree(parents)
    print(get_height(tree))


if __name__ == "__main__":
    test()
    # run_task()
