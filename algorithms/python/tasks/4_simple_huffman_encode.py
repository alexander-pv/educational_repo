"""
#########################
Алгоритм кодирования Хаффмана.
Очередь с приоритетами на базе массива (Время работы с простейшей реализации на массиве - O(n^2))
#########################
По данной непустой строке sдлины не более 10^4 , состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k встречающихся в строке,
и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
"""


class PriorityQueue:
    def __init__(self):
        self.queue_nodes = []
        self.queue_priorities = []
        self.tree_levels = 0
        self.init_nodes = int()
        self.codes = {}
        self.frequencies = dict()

    def _insert(self, node):
        node_pos = self.find_new_position(node.value)
        self.queue_nodes.insert(node_pos, node)
        self.queue_priorities.insert(node_pos, node.value)

    def _init_nodes(self):
        self.init_nodes = len(self.frequencies.keys())
        for k, v in self.frequencies.items():
            self._insert(node=Node(key=k, value=v))

    def _get_chars_frequencies(self, s):
        chars_list = [i for i in s]
        for char in chars_list:
            if char not in self.frequencies.keys():
                self.frequencies.update({char: 1})
            else:
                self.frequencies[char] += 1
        return self.frequencies

    def find_new_position(self, p):
        pos = 0
        if len(self.queue_priorities) > 0:
            for q_p in self.queue_priorities:
                if q_p < p:
                    pos += 1
                else:
                    break
        return pos

    def extract_min(self):
        node = self.queue_nodes.pop(0)
        self.queue_priorities.pop(0)
        return node

    def split_leaves(self, leaves, char_code):

        if isinstance(leaves, str):
            if char_code == '':
                char_code = '0'
            char = leaves
            self.codes.update({char: char_code})
        else:
            left, right = leaves[0], leaves[1]
            if isinstance(right, str) & isinstance(left, str):
                self.codes.update({left: char_code + '0'})
                self.codes.update({right: char_code + '1'})
            elif isinstance(left, str):
                self.codes.update({left: char_code + '0'})
                self.split_leaves(right, char_code + '1')
            else:
                self.split_leaves(right, char_code + '1')
                self.split_leaves(left, char_code + '0')
        return self.codes

    def generate_tree(self):
        n = len(self.queue_nodes)
        while n != 1:
            node_0 = self.extract_min()
            node_1 = self.extract_min()
            new_node = Node(key=f'{node_0.key}_{node_1.key}',
                            value=node_0.value + node_1.value,
                            children=[node_0, node_1],
                            )
            self._insert(node=new_node)
            self.tree_levels += 1
            n = len(self.queue_nodes)
        return self.queue_nodes[0]

    def get_huffman_codes(self, s):

        self._get_chars_frequencies(s)
        self._init_nodes()
        tree = self.generate_tree()
        leaves = tree.get_leaves()
        codes = self.split_leaves(leaves, char_code='')
        return codes


class Node:
    def __init__(self, key, value, children=None):
        self.children = []
        self.n_children = 0
        if children:
            self.children.extend(children)
            self.n_children = len(self.children)
        self.key = key
        self.value = value

    def update_value(self):
        self.value = self[0].value + self[1].value

    def get_leaves(self):
        if self.n_children > 0:
            return self[0].get_leaves(), self[1].get_leaves()
        else:
            return self.key

    def __getitem__(self, idx):
        return self.children[idx]


if __name__ == '__main__':

    s = 'accepted'
    p_queue = PriorityQueue()
    codes = p_queue.get_huffman_codes(s)
    encoded_s = ''.join(codes[x] for x in s)
    print(len(codes.keys()), len(encoded_s))
    for k, v in codes.items():
        print(f'{k}: {v}')
    print(encoded_s)

