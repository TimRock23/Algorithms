def e(arr1, arr2):
    arr_dict = {}
    for i in arr2:
        if i not in arr_dict:
            arr_dict[i] = [0, 1]
        else:
            arr_dict[i][1] += 1
    for i in arr1:
        if i in arr_dict:
            arr_dict[i][0] += 1
            if arr_dict[i][0] <= arr_dict[i][1]:
                print(i, end=' ')


if __name__ == '__main__':
    arr1_len = int(input())
    arr2_len = int(input())
    if arr1_len != 0 or arr2_len != 0:
        arr1 = list(map(int, input().split(' ')))
        arr2 = list(map(int, input().split(' ')))
        e(arr1, arr2)
