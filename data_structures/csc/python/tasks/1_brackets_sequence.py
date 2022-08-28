"""
Вы разрабатываете текстовый редактор для программистов и хотите реализовать проверку
корректности расстановки скобок. В коде могут встречаться скобки []{}(). Из них скобки [,{ и (
считаются открывающими, а соответствующими им закрывающими скобками являются ],} и ).
В случае, если скобки расставлены неправильно, редактор должен также сообщить пользователю первое место ошибки.

1)В первую очередь необходимо найти закрывающую скобку, для кото-
рой либо нет соответствующей открывающей (например, скобка ] в
строке “]()”), либо же она закрывает не соответствующую ей откры-
вающую скобку (пример: “()[}”).
2)Если таких ошибок нет, необходимо найти первую открывающую скобку, для которой нет соответствующей закрывающей
(пример: скобка ( в строке “{}([]”).
3)Помимо скобок, исходный код может содержать символы латинского алфавита, цифры и знаки препинания.

"""


class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.size -= 1
        return self.stack.pop()

    def is_empty(self):
        return self.size == 0


def is_balanced(txt: str):
    opening, closing = ('(', '[', '{'), (')', ']', '}')
    brackets_stack = Stack()
    opening_stack = Stack()

    for i, s in enumerate(txt, start=1):
        if s not in [*opening, *closing]:
            continue
        if s in opening:
            brackets_stack.push(s)
            opening_stack.push(i)
        else:
            if brackets_stack.is_empty():
                return i
            top = brackets_stack.pop()
            open_idx = opening.index(top)
            close_idx = closing.index(s)
            if open_idx != close_idx:
                return i
            else:
                opening_stack.pop()

    output = 'Success' if brackets_stack.is_empty() else opening_stack.top()
    return output


def test():
    right = ('[]', '{}[]', '[()]', '(())', '{[]}()', 'foo(bar)')
    wrong = ('{', ']', '[)', '{[}', 'foo(bar[i);', '[]([];', '{{{[][][]', '{{{{{{{((()))}',
             '{()}{', '}()', '()}()', '{[()]}}()', 'dasdsadsadas]]]'
             )
    wrong_ids = (1, 1, 2, 3, 10, 3, 3, 6,
                 5, 1, 3, 7, 13
                 )
    for r in right:
        print(is_balanced(txt=r), is_balanced(txt=r) == 'Success')
        assert is_balanced(txt=r) == 'Success'
    print('\n')
    for w, w_ans in zip(wrong, wrong_ids):
        print(is_balanced(txt=w), w_ans, w_ans == is_balanced(txt=w))


if __name__ == '__main__':
    test()
    # print(is_balanced(txt=input()))

