"""
Реализовать структуру данных, эффективно обрабатывающую запросы вида:
    - add number name,
    - del number,
    - find number.

• add number name: добавить запись с именем name и телефонным номером number.
Если запись с таким телефонным номером уже есть, нужно заменить в ней имя на name.

• del number: удалить запись с соответствующим телефонным номером.
Если такой записи нет, ничего не делать.

• find number: найти имя записи с телефонным номером number.
Если запись с таким номером есть, вывести имя. В противном случае вывести «not found» (без кавычек).

Вход:
    Последовательность запросов вида add number, name, del number и find number,
    где number — телефонный номер, содержащий не более семи знаков, а name — короткая строка.
Выход:
    Для каждого запроса find number выведите соответствующее имя или сообщите, что такой записи нет.


1 ≤ n ≤ 10 5 . Телефонные номера содержат не более
семи цифр и не содержат ведущих нулей. Имена содержат только
буквы латинского алфавита, не являются пустыми строками и
имеют длину не больше 15. Гарантируется, что среди имён не
встречается строка «not found»
"""

import copy


def hash_func(x: int, size: int) -> int:
    return x % size


class Node:
    number: int = -1
    name: str = None
    next: object = None

    def add_next(self) -> None:
        self.next = copy.deepcopy(Node())

    def has_next(self) -> bool:
        return self.next is not None

    def __repr__(self):
        return dict(number=self.number, name=self.name, next=self.next).__repr__()


class LinkedList:

    def __init__(self, head: Node = Node()):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"[{node.number}, {node.name}]")
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class PhoneBook:

    def __init__(self, size: int):
        self.size = size
        self.table = [copy.deepcopy(LinkedList()) for i in range(self.size)]

    def _add_number(self, node: Node, number: int, name: str):

        if node.number == -1:
            node.number, node.name = number, name
        elif node.number == number:
            node.name = name
        else:
            node.add_next()
            self._add_number(node=node.next, number=number, name=name)

    def _del_number(self, node: Node, number: int):
        if node is not None:
            if node.number == number:
                node.number, node.name = -1, None
            else:
                self._del_number(node=node.next, number=number)

    def _find_number(self, node: Node, number: int) -> str:

        result = "not found"
        if node is not None:
            if node.number == number:
                result = node.name
            else:
                result = self._find_number(node=node.next, number=number)
        return result

    def add_number(self, number: int, name: str) -> None:
        idx = hash_func(number, self.size)
        self._add_number(node=self.table[idx].head, number=number, name=name)

    def del_number(self, number: int):
        idx = hash_func(number, self.size)
        self._del_number(node=self.table[idx].head, number=number)

    def find_number(self, number: int) -> str:

        idx = hash_func(number, self.size)
        result = self._find_number(node=self.table[idx].head, number=number)
        return result


def run_task() -> None:
    n = int(input())
    book = PhoneBook(size=n)
    for i in range(n):
        string = input().split(' ')
        number = int(string[1])
        if string[0] == 'add':
            book.add_number(number=number, name=string[2])
        elif string[0] == 'find':
            res = book.find_number(number=number)
            print(res)
        elif string[0] == 'del':
            book.del_number(number=number)


def test() -> None:
    pass


if __name__ == "__main__":
    test()
    # run_task()
