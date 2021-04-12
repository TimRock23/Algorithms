class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None for _ in range(max_size)]
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, x):
        if self.queue_size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1
        else:
            return 'error'

    def pop(self):
        if self.queue_size > 0:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            return x
        else:
            return None

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.queue_size


def n(commands):
    for command in commands:
        if command[0] == 'push':
            x = queue.push(command[1])
            if x == 'error':
                print(x)
        elif command[0] == 'pop':
            print(queue.pop())
        elif command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    count = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    n(commands)
