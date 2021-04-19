def h():
    root = 2 ** 0.5
    root = float('{:.5f}'.format(root))
    return root


if __name__ == '__main__':
    string = input().split(' ')
    print(h())
