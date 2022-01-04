"""
##################
Непрерывный рюкзак
##################
Первая строка содержит количество предметов и вместимость рюкзака.
Каждая из следующих строк задаёт стоимость и объём предмета.
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.
"""


def knapsack(total_w: float, items: list) -> float:
    """
    Knapsack algorithm
    :param total_w: float, Total weight
    :param items:   list of tuples: [tuple(float, int),...]
    :return: float
    """
    ppu = [x[0] / x[1] for x in items]
    sort_idx = [ppu.index(i) for i in sorted(ppu, reverse=True)]
    total_c = 0.0
    left_w = total_w

    for idx in sort_idx:
        c, w = items[idx][0], items[idx][1]
        d = 1.0
        if left_w < w:
            d = left_w / w
        total_c += d * c
        left_w -= w

        if left_w <= 0:
            break
    return total_c


if __name__ == '__main__':
    n, total_w_inp = input().split(' ')
    n, total_w_inp = int(n), float(total_w_inp)
    items_list = []
    for _ in range(n):
        c_inp, w_inp = input().split(' ')
        items_list.append((float(c_inp), int(w_inp)))
    result = knapsack(total_w_inp, items_list)
    print('%.3f' % result)
