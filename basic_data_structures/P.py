class Queue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.head = 0
        self.tail = 0
        self.queue_size = 0
        self.max_size = n

    def get(self):
        if self.queue_size == 0:
            return 'error'
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            return x

    def put(self, x):
        if self.queue_size < self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1
        else:
            return 'error'

    def size(self):
        return self.queue_size


def queue_node(commands):
    for command in commands:
        if command[0] == 'put':
            queue.put(int(command[1]))
        elif command[0] == 'get':
            print(queue.get())
        elif command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':
    queue = Queue(1000)
    count = int(input())
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    queue_node(commands)
