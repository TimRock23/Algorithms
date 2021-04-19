from copy import deepcopy


def a(arr_length, arr):
    arr_res = []
    for i in range(arr_length-1):
        for j in range(arr_length-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

        if i == 0:
            print(*arr)
            arr_res.append(deepcopy(arr))

        if arr != arr_res[-1]:
            print(*arr)
        arr_res.append(deepcopy(arr))
    return arr_res


if __name__ == '__main__':
    arr_length = int(input())
    arr = list(map(int, input().split(' ')))
    a(arr_length, arr)
