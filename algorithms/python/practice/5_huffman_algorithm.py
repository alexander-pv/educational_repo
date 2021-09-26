import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, cntr1, left = heapq.heappop(h)
        freq2, cntr2, right = heapq.heappop(h)
        heapq.heappush(h,  (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _cnt, root)] = h
        root.walk(code, "")
    return code


class HuffmanDecoder:
    """
    HuffmanDecoder без построения дерева
    """

    def __init__(self, codes):
        self.inv_codes = {v: k for k, v in codes.items()}
        self.decoded_chars = []
        self.substring = ''
        self.suggestions = self.inv_codes

    def update_suggestions(self, s):
        self.substring += s
        self.suggestions = dict([(k, v) for k, v in self.inv_codes.items() if k.startswith(self.substring)])
        if len(self.suggestions.keys()) == 1:
            self.decoded_chars.extend(list(self.suggestions.values()))
            self.suggestions = self.inv_codes
            self.substring = ''

    def decode_string(self, string):
        for s in string:
            self.update_suggestions(s)
        return ''.join(self.decoded_chars)


def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


def test(n_iter=100, interval=50):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, interval)
        s = "".join(random.choice(string.ascii_letters)for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)

        decoder = HuffmanDecoder(code)
        assert decoder.decode_string(encoded) == s
        print(f'Accepted:\t{s}')


if __name__ == '__main__':
    test()
