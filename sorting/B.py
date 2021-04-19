def b(arr_length, arr):
    for i in range(arr_length):
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = x

    return arr


if __name__ == '__main__':
    arr_length = int(input())
    arr = list(map(int, input().split(' ')))
    print(*b(arr_length, arr))
