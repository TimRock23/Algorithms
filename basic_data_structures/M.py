class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.head = 0
        self.tail = 0
        self.queue_size = 0
        self.max_size = n

    def push(self, x):
        if self.queue_size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1

    def pop(self):
        if self.queue_size == 0:
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.queue_size


def queue(commands):
    for command in commands:
        if command[0] == 'pop':
            print(q.pop())
        elif command[0] == 'size':
            print(q.size())
        elif command[0] == 'peek':
            print(q.peek())
        elif command[0] == 'push':
            q.push(int(command[1]))


if __name__ == '__main__':
    q = MyQueue(1000)
    count = int(input())
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    queue(commands)
