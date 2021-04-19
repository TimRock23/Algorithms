def g(arr):
    arr = sorted(arr, reverse=True)
    for i in range(len(arr)-2):
        first = arr[i]
        second = arr[i+1]
        third = arr[i+2]
        if first < second + third:
            return first+second+third


if __name__ == '__main__':
    count = int(input())
    arr = list(map(int, input().split(' ')))
    print(g(arr))
