def c(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return c(less) + [pivot] + c(greater)


if __name__ == '__main__':
    arr_length = int(input())
    arr = list(map(int, input().split(' ')))
    print(*c(arr))