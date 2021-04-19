def i(x, y):
    x = x % y
    if x == 0:
        return y
    return i(y, x)


if __name__ == '__main__':
    width = int(input())
    length = int(input())
    print(i(width, length))
