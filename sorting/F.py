def f(count, arr):
    even = []
    uneven = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            uneven.append(i)
    for i in range(count):
        if i % 2 == 0:
            arr[i] = even[int(i/2)]
        else:
            arr[i] = uneven[int(i//2)]
    return arr


if __name__ == '__main__':
    count = int(input())
    if count != 0:
        arr = list(map(int, input().split(' ')))
        print(*f(count, arr))
