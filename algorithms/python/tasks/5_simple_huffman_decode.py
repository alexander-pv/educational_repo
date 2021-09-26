"""
#########################
Декодирование кода Хаффмана
#########################

В первой строке входного файла заданы два целых числа k, l через пробел — количество различных букв,
встречающихся в строке, и размер получившейся закодированной строки, соответственно.
В следующих k строках записаны коды букв в формате "letter: code".

Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке.
В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке
хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты.
Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит 10^4 символов.
"""


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


if __name__ == '__main__':

    k, l = input().split(' ')
    k, l = int(k), int(l)
    codes = dict()
    for _ in range(k):
        k, v = input().split(': ')
        codes.update({k: v})

    encoded_s = input()

    decoder = HuffmanDecoder(codes)
    decoded_s = decoder.decode_string(encoded_s)
    print(decoded_s)
