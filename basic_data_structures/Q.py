class Deck:
    def __init__(self, max_size):
        self.items = [None for _ in range(max_size)]
        self.max_size = max_size
        self.size = 0
        self.head = 1
        self.tail = 0

    def push_back(self, value):
        if self.size == self.max_size:
            return print('error')
        self.items[self.tail] = value
        self.tail = (self.tail - 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            return print('error')
        self.items[self.head] = value
        self.head = (self.head + 1) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return print('error')
        self.head = (self.head - 1) % self.max_size
        x = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        return x

    def pop_back(self):
        if self.size == 0:
            return print('error')
        self.tail = (self.tail + 1) % self.max_size
        x = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1

        return x


def deck_q(commands):
    for command in commands:
        if command[0] == 'push_back':
            deck.push_back(int(command[1]))
        elif command[0] == 'push_front':
            deck.push_front(int(command[1]))
        elif command[0] == 'pop_front':
            print(deck.pop_front())
        elif command[0] == 'pop_back':
            print(deck.pop_back())


if __name__ == '__main__':
    count = int(input())
    max_size = int(input())
    deck = Deck(max_size)
    commands = []
    for i in range(count):
        command = input().split(' ')
        commands.append(command)
    deck_q(commands)
