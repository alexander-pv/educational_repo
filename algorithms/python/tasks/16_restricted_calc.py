"""
У вас есть примитивный калькулятор, который умеет выполнять 
всего три операции с текущим числом x: заменить x на 2x, 3x или x+1. 
По данному целому числу 1≤n≤10^5  определите минимальное число операций k , необходимое, чтобы получить n из 1. 
Выведите k и последовательность промежуточных чисел.
"""

from typing import Tuple


def step_paths(values: list, inv_ops: tuple) -> list:
    """
    :param values:  list of ints, values to be transformed
    :param inv_ops: tuple of callable, possible calculator operations
    :return: list, the smallest values for each operation and the number of input values
    """
    paths = []
    for op in inv_ops:
        v_list = (int(x) if not x % 1 else float('inf') for x in (op(v) for v in values))
        paths.append(min(v_list))
    return paths


def restore_solution(seq_len: int, tab: list, ops: tuple) -> list:
    """
    :param seq_len: int, sequence length
    :param tab:     list, solutions table
    :param ops:     tuple of callable, possible calculator operations
    :return: list,  restored from tab the shortest sequence
    """
    sequence = [1 for _ in range(seq_len + 1)]
    val, seq_id = 1, 1
    for i in range(seq_len, 0, -1):
        op_id = tab[i].index(val)
        val = ops[op_id](val)
        sequence[seq_id] = val
        seq_id += 1
    return sequence


def top_down_restricted_calculator(n: int, ops: tuple, inv_ops: tuple) -> Tuple[int, list]:
    """
    Solution with TopDown method
    :param n:        int, target value
    :param ops:      tuple of callable, possible calculator operations
    :param inv_ops:  tuple of callable, inverted calculator operations
    :return: int, sequence length, list, the sequence
    """
    solution_tab = [[n for _ in range(len(ops))]]
    while 1 not in solution_tab[-1]:
        paths_list = step_paths(solution_tab[-1], inv_ops=inv_ops)
        solution_tab.append(paths_list)
    seq_len = len(solution_tab) - 1
    sequence = restore_solution(seq_len=seq_len, tab=solution_tab, ops=ops)
    return seq_len, sequence


def main() -> None:
    ops = (lambda x: x + 1, lambda x: 2 * x, lambda x: 3 * x)
    inv_ops = (lambda x: x - 1, lambda x: x / 2, lambda x: x / 3)
    n = int(input())
    seq_len, sequence = top_down_restricted_calculator(n=n, ops=ops, inv_ops=inv_ops)
    print(seq_len)
    print(*sequence)


if __name__ == '__main__':
    main()
