import random
from functools import lru_cache


def edit_distance_recursive(s1: str, s2: str) -> int:
    @lru_cache(maxsize=None)
    def d(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        else:
            return min(d(i, j - 1) + 1,
                       d(i - 1, j) + 1,
                       d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]))

    return d(len(s1), len(s2))


def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    if m < n:
        return edit_distance(s2, s1)
    prev = list(range(n + 1))
    for i, ch1 in enumerate(s1, 1):
        curr = [i]  # O(min(m, n)) memory
        for j, ch2 in enumerate(s2, 1):
            curr.append(min(curr[-1] + 1,
                            prev[j] + 1,
                            prev[j - 1] + (ch1 != ch2)))
        prev = curr
    return prev[n]


def test(n_iter: int = 100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = "".join(random.choice("01") for _ in range(length))

        assert edit_distance(s, "") == edit_distance("", s) == len(s)
        assert edit_distance(s, s) == 0

    assert edit_distance("ab", "ab") == 0
    assert edit_distance("short", "ports") == 3


def main() -> None:
    s1, s2 = input(), input()
    print(edit_distance(s1, s2))


if __name__ == '__main__':
    # sys.setrecursionlimit(int(1e4))
    # main()
    test()
