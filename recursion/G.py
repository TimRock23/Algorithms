import string


def g():
    alphabet = [i for i in string.ascii_lowercase]
    letter = input()
    ind = 0

    def recursion(index):
        if alphabet[index] != letter:
            print(alphabet[index], end=' ')
            return recursion(index + 1)
        elif alphabet[index] == letter:
            print(alphabet[index])

    recursion(ind)


g()
