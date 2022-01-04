"""
Первая строка входа содержит целые числа 1≤W≤104 и 1≤n≤300 — вместимость рюкзака и число золотых слитков.
Следующая строка содержит n целых чисел 0≤w1,…,wn≤105, w_n ≤ 10^5 , задающих веса слитков.
Найдите максимальный вес золота, который можно унести в рюкзаке.
"""

import sys
from typing import Tuple


def read_input() -> Tuple[int, int, list]:
    """
    Read input for a task
    :return: int, list of ints
    """
    lines = ([line for line in sys.stdin])
    w, n = [int(x) for x in lines[0].split(' ')]
    costs = [int(x) for x in lines[1].split(' ')]
    return w, n, costs


def knapsack_without_reps(w: int, n: int, costs: list) -> int:
    """
    Knapsack without repetitions. Bottom-Up dynamic programming algorithm.
    Cost matrix building example:
            Input: 20 4
                   5 7 12 18
            knapsack_mat:
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
                        [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5,  5,  5,  5,  5,  5,  5,  5,  5,  5]
                        [0, 0, 0, 0, 0, 5, 5, 7, 7, 7, 7, 7, 12, 12, 12, 12, 12, 12, 12, 12, 12]
                        [0, 0, 0, 0, 0, 5, 5, 7, 7, 7, 7, 7, 12, 12, 12, 12, 12, 17, 17, 19, 19]
                        [0, 0, 0, 0, 0, 5, 5, 7, 7, 7, 7, 7, 12, 12, 12, 12, 12, 17, 18, 19, 19]
            Output: 19
    :param w:     int, maximum cost value, maximum knapsack capacity
    :param n:     int, number of possible items
    :param costs: list of ints, items costs
    :return: int
    """
    # First, we build a table to solve subtasks
    # Rows - the number of possible items to choose from 0 to n, n_0,...n_n
    # Columns - the number of knapsack volumes from 0 to w, w_0,..,w_w
    # Note, costs[n_i - 1] is necessary because of indexation
    knapsack_mat = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for n_i in range(n + 1):
        for w_i in range(w + 1):
            # Skip zero item or zero capacity states
            if n_i == 0 or w_i == 0:
                continue
            if costs[n_i - 1] > w_i:
                # If current item cost is higher than knapsack capacity, choose solution with previous item
                knapsack_mat[n_i][w_i] = knapsack_mat[n_i - 1][w_i]
            else:
                prev_solution = knapsack_mat[n_i - 1][w_i]
                # The cost of current item + the cost of the space left in the knapsack
                suggest_solution = costs[n_i - 1] + knapsack_mat[n_i - 1][w_i - costs[n_i - 1]]
                # Choose the best option
                knapsack_mat[n_i][w_i] = max(prev_solution, suggest_solution)
    return knapsack_mat[n][w]


if __name__ == '__main__':
    w, n, costs = read_input()
    res = knapsack_without_reps(w=w, n=n, costs=costs)
    print(res)
