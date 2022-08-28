"""
Ваша цель в данной задаче — реализовать такую схему, используя таблицу с m ячейками
и полиномиальной хеш-функцией на строках.

p = 1 000 000 007 — простое число, а x = 263.
add string: добавить строку string в таблицу. Если такая строка уже есть, проигнорировать запрос;
del string: удалить строку string из таблицы. Если такой строки нет, проигнорировать запрос;
find string: вывести «yes» или «no» в зависимости от того, есть в таблице строка string или нет;
check i: вывести i-й список (используя пробел в качестве разделителя); если i-й список пуст, вывести пустую строку.

При добавлении строки в цепочку, строка должна добавляться в начало цепочки.

Формат входа:
Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n.
Каждая из последующих n строк содержит запрос одного из перечисленных выше четырёх типов.

Формат выхода:
Для каждого из запросов типа find и check выведите результат в отдельной строке.

Ограничения:
 1 ≤ n ≤ 10 5 ; n/5 ≤ m ≤ n. Все строки имеют длину от одного до пятнадцати и содержат только буквы латинского алфавита.
"""


def hash_function(s: str, table_size: int, p: int = int(1e9 + 7), x: int = 263):
    result = (sum(ord(char) * (x ** i % p) for i, char in enumerate(s)) % p) % table_size
    return result


class HashTable:

    def __init__(self, table_size: int):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]

    def add_string(self, s: str) -> None:
        idx = hash_function(s, table_size=self.table_size)
        if s not in self.table[idx]:
            self.table[idx].append(s)

    def del_string(self, s: str) -> None:
        idx = hash_function(s, table_size=self.table_size)
        try:
            self.table[idx].remove(s)
        except ValueError:
            pass

    def find_string(self, s: str) -> str:
        idx = hash_function(s, table_size=self.table_size)
        out = "yes" if s in self.table[idx] else "no"
        return out

    def check(self, i: int) -> str:
        out = "\n"
        if len(self.table[i]) > 0:
            out = " ".join(self.table[i][::-1])
        return out


def run_task() -> None:
    m = int(input())
    n = int(input())
    htable = HashTable(table_size=m)
    htable_commands = {"add": htable.add_string,
                       "check": htable.check,
                       "find": htable.find_string,
                       "del": htable.del_string
                       }
    for _ in range(n):
        req = input()
        command, value = req.split(" ")
        if command == "check":
            value = int(value)
        output = htable_commands[command](value)
        if output:
            print(output)


def test() -> None:
    m = 5
    requests = ("add world",
                "add HellO",
                "check 4",
                "find World",
                "find world",
                "del world",
                "check 4",
                "del HellO",
                "add luck",
                "add GooD",
                "check 2",
                "del good")
    htable = HashTable(table_size=m)
    htable_commands = {"add": htable.add_string,
                       "check": htable.check,
                       "find": htable.find_string,
                       "del": htable.del_string
                       }
    for req in requests:
        command, value = req.split(" ")
        if command == "check":
            value = int(value)
        output = htable_commands[command](value)
        if output:
            print(output)


if __name__ == "__main__":
    test()
    # run_task()
