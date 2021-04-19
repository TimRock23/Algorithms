def h(string):
    word = string[-1]
    return len(word)


if __name__ == '__main__':
    string = input().split(' ')
    print(h(string))
