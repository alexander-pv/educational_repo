"""
Поиск образца в тексте. Реализуйте алгоритм Карпа–Рабина.

Найти все вхождения строки Pattern в строку Text.

Вход:
Строки Pattern и Text.

Выход:
Индексы вхождений строки Pattern в строку Text в возрастающем порядке, используя индексацию с нуля.
Text[i..i + |Pattern| − 1] = Pattern.

Ограничения:
1 ≤ |Pattern| ≤ |Text| ≤ 5 · 10^5 .
Суммарная длина всех вхождений образца в текста не превосходит 10^8 . Обе строки содержат буквы латинского алфавита.
"""
import random


class RollingHash:

    def __init__(self, template: str, p: int, x: int or None = None):
        """
        Rabin-Karp algorithm with rolling polynomial hash function
        :param p: large prime number
        :param x: constant for polynomial hash function
        :param template: string template
        """
        self.p = p
        self.template = template
        self.window = len(template)
        # # random integer 1<=x<=p
        self.x = x if x else random.randint(1, p)
        # x^(|P|-1) mod p, x^(|P|-2) mod p,...,x^0 mod p, where P - template length
        self.xs = [pow(self.x, i - 1) % self.p for i in range(self.window, 0, -1)]

    def hash(self, s: str) -> int:
        """
        Calculate polynomial hash value of a string 's' based on ASCII char codes:
        h_i = s_0 * x^(|P|-1) mod p + s_1 * x^(|P|-2) mod p + ... + x_
        :param s: string
        :return: hash integer value
        """
        return sum((ord(char) * self.xs[i]) for i, char in enumerate(s)) % self.p

    def match(self, text: str):
        """
        :param text:
        :return:
        """
        template_hash = self.hash(self.template)
        print(f'template_hash: {template_hash}')
        n_shifts = len(text) - self.window + 1
        for i in range(n_shifts):
            if i == 0:
                substr_hash = self.hash(text[:self.window])
            else:
                """
                h(window_i) = [h(window_(i-1)) - ASCII(text[i-1]) * x^(|P|-1) mod p ] * x (mod p) \
                              + ASCII(text[winsize-1 + i])
                """

                prev_char_code = ord(text[i - 1])
                next_char_code = ord(text[i + self.window - 1])
                substr_hash = (substr_hash - prev_char_code * self.xs[0]) * self.x % self.p + next_char_code % self.p

            if template_hash == substr_hash:
                substring = text[i:self.window + i]
                print(f'Matched hash: {substr_hash} for substring {substring}')
                if self.template == substring:
                    print(i, end=' ')


def run_task() -> None:
    template, text = input(), input()
    roll_hash = RollingHash(template=template, p=1000000007, x=1)
    roll_hash.match(text)


def test() -> None:
    examples = (
        ("Test", "testTesttesT"),
        ("aba", "abacaba"),
        ("aaaaa", "baaaaaaa")
    )
    for template, text in examples:
        roll_hash = RollingHash(template=template, p=1000000007, x=1)
        print(f"\ninput: {template}, {text}")
        roll_hash.match(text)


if __name__ == "__main__":
    test()
    # run_task()
