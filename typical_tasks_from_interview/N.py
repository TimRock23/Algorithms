def n(num):
    max_num = 0
    max_degree = 0
    while max_num < 10000:
        max_num = 4**(max_degree + 1)
        max_degree += 1
    four_degree = [4**i for i in range(0, max_degree-1)]
    return num in four_degree


if __name__ == '__main__':
    num = int(input())
    print(n(num))
