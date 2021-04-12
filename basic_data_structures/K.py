class StackSet:
    def __init__(self):
        self.items_list = []
        self.items_set = set()

    def is_empty(self):
        return self.items_list == []

    def push(self, item):
        if item not in self.items_set:
            self.items_set.add(item)
            self.items_list.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        pop = self.items_list.pop()
        self.items_set.remove(pop)
        return pop

    def peek(self):
        if self.is_empty():
            return 'error'
        return self.items_list[-1]

    def size(self):
        return len(self.items_list)


def k(commands):
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'size':
            print(stack.size())
        elif command[0] == 'peek':
            print(stack.peek())
        elif command[0] == 'pop':
            if stack.pop() == 'error':
                print('error')


if __name__ == '__main__':
    stack = StackSet()
    count = int(input())
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    k(commands)
