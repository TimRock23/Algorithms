def d(arr1, arr2):

    arr_dict = {}
    for i in arr2:
        if i not in arr_dict:
            arr_dict[i] = 1
    for i in arr1:
        if i in arr_dict:
            if arr_dict[i] == 1:
                print(i, end=' ')
                arr_dict[i] = 2


if __name__ == '__main__':
    arr1_len = int(input())
    arr2_len = int(input())
    if arr1_len != 0 and arr2_len != 0:
        arr1 = list(map(int, input().split(' ')))
        arr2 = list(map(int, input().split(' ')))
        d(arr1, arr2)
