class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return not self.__items

    def push(self, item):
        return self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.__items.pop()


OPERANDS = {
    '+': (lambda x, y: x+y),
    '-': (lambda x, y: x-y),
    '*': (lambda x, y: x*y),
    '/': (lambda x, y: x//y)
}


def calculator(formula):
    stack = Stack()
    for symbol in formula:

        if symbol in OPERANDS:
            second_value, first_value = int(stack.pop()), int(stack.pop())
            func = OPERANDS[symbol]
            result = func(first_value, second_value)
            stack.push(result)
        else:
            stack.push(symbol)

    return stack.pop()


if __name__ == '__main__':
    formula_arr = input().split()
    print(calculator(formula_arr))
