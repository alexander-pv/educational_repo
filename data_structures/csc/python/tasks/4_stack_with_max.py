"""
Стек — абстрактная структура данных, поддерживающая операции push и pop.
Несложно реализовать стек так, чтобы обе эти операции работали за константное время.
В данной задаче ваша цель — расширить интерфейс стека так, чтобы он дополнительно поддерживал операцию max
и при этом чтобы время работы всех операций по-прежнему было константным.

Формат входа.
Первая строка содержит число запросов q.
Каждая из последующих q строк задаёт запрос в одном из следующих форматов: push v, pop, or max.

Формат выхода.
Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.

Ограничения.
1 ≤ q ≤ 400 000, 0 ≤ v ≤ 100 000.
"""


class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_idx = []
        self.size = 0

    def update_max_idx(self):
        if self.size == 1:
            self.max_idx.append(0)
        else:
            if self.stack[-1] > self.stack[self.max_idx[-1]]:
                self.max_idx.append(self.size - 1)
            else:
                self.max_idx.append(self.max_idx[-1])

    def get_max(self):
        return self.stack[self.max_idx[-1]]

    def push(self, x):
        self.stack.append(x)
        self.size += 1
        self.update_max_idx()

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.size -= 1
        value = self.stack.pop()
        self.max_idx.pop()
        return value

    def is_empty(self):
        return self.size == 0


def parse_stack_command(stack: MaxStack, string: str):
    if "push" in string:
        cmnd, value = string.split(" ")
        stack.push(int(value))
    else:
        if string == "pop":
            output = stack.pop()
        elif string == "max":
            output = stack.get_max()
        else:
            raise ValueError(f"Unexpected command: `{string}` to parse!")
        return output


def test() -> None:
    test_values = (
        {"n": 5,
         "commands": ("push 2", "push 1", "max", "pop", "max"),
         "expected": (-1, -1, 2, -1, 2)
         },
        {"n": 10,
         "commands": ("push 2", "push 3", "push 9", "push 7",
                      "push 2", "max", "max", "max", "pop", "max"),
         "expected": (-1, -1, -1, -1, -1, 9, 9, 9, -1, 9)

         },
        {"n": 5,
         "commands": ("push 1", "push 2", "max", "pop", "max"),
         "expected": (-1, -1, 2, -1, 1)

         }
    )
    for example in test_values:
        stack = MaxStack()
        for string, expected in zip(example["commands"], example["expected"]):
            result = parse_stack_command(stack, string)
            if string == "max":
                assert result == expected, f"Result: [{result}] Expected: [{expected}]"


def run_task() -> None:
    stack = MaxStack()
    n = int(input())
    for i in range(n):
        string = input()
        result = parse_stack_command(stack, string)
        if string == "max":
            print(result)


if __name__ == "__main__":
    test()
    # run_task()
