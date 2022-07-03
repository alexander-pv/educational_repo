import sys
from typing import Tuple

"""
Даны число 1≤n≤10^2 ступенек лестницы и целые числа −10^4≤a1,…,an≤10^4, которыми помечены ступеньки.
Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки),
каждый раз поднимаясь на одну или две ступеньки.
"""


def best_step_recursive(steps_list: list, sum_list: list, n: int, k: int = 0) -> int:
    """
    Recursive algorithm for ladder task
    Note, we do not need to store all sums in s_list. We need only the last 2 of them.
    :param steps_list:    list of step weights
    :param sum_list:      list, the sum of weights for steps being taken
    :param n:             int,  number of weights in steps_list
    :param k:             int,  current recursion call
    :return: int
    """
    if k == n:
        return sum_list[-1]
    else:
        if k <= 1:
            sum_list.append(steps_list[k])
        else:
            print(f'max({sum_list[-2]},{sum_list[-1]}) + {steps_list[k]}')
            print(sum_list, steps_list, k)
            next_val = max(sum_list[-2], sum_list[-1]) + steps_list[k]
            sum_list.append(next_val)
        k += 1
        return best_step_recursive(steps_list=steps_list, sum_list=sum_list[-2:], n=n, k=k)


def best_step_iterative(steps_list: list, n: int) -> int:
    """
    Iterative algorithm for ladder task
    :param steps_list:  list of ints, weight per each step
    :param n:           int, number of weights in steps_list
    :return: int
    """
    sum_list = [0, 0]
    for i in range(n):
        if i <= 1:
            sum_list[i] = steps_list[i]
        else:
            next_val = max(sum_list) + steps_list[i]
            sum_list[0] = sum_list[1]
            sum_list[1] = next_val
    return sum_list[-1]


def read_input() -> Tuple[int, list]:
    """
    Read input for a task
    :return: int, list of ints
    """
    lines = ([line for line in sys.stdin])
    n = int(lines[0])
    weigths = [int(x) for x in lines[1].split(' ')]
    return n, weigths


def main() -> None:
    n, w = read_input()
    result = best_step_iterative(steps_list=[0, *w], n=n + 1)
    print(result)


if __name__ == '__main__':
    main()
