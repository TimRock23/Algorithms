class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if not self.max_items:
            self.max_items.append(item)
        elif item > self.max_items[-1]:
            self.max_items.append(item)
        else:
            self.max_items.append(self.max_items[-1])

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max_items.pop()
        return self.items.pop()

    def get_max(self):
        if not self.max_items:
            return None
        return self.max_items[-1]


def max_size(commands):
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            if stack.pop() == 'error':
                print('error')
        elif command[0] == 'get_max':
            print(stack.get_max())


max_size()
if __name__ == '__main__':
    stack = StackMaxEffective()
    count = int(input())
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    j(commands)
