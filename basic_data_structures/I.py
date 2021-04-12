class StackMax:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.items.pop()

    def get_max(self):
        if self.is_empty():
            return None
        max_num = self.items[0]
        for i in self.items:
            if i > max_num:
                max_num = i
        return max_num


def max_size(commands):

    for command in commands:
        if command[0] == 'get_max':
            print(stack.get_max())
        elif command[0] == 'pop':
            if stack.pop() == 'error':
                print(stack.pop())
        elif command[0] == 'push':
            stack.push(int(command[1]))


if __name__ == '__main__':
    stack = StackMax()
    count = int(input())
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    max_size(commands)
