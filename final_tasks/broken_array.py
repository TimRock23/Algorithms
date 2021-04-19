def search_index(array, search_elem, left_index, right_index):
    mid_index = (right_index + left_index) // 2
    mid_elem = array[mid_index]

    if search_elem == mid_elem:
        return mid_index

    if right_index < left_index:
        return -1

    if array[left_index] <= mid_elem:

        if array[left_index] <= search_elem <= mid_elem:
            return search_index(array, search_elem, left_index, mid_index-1)
        else:
            return search_index(array, search_elem, mid_index+1, right_index)

    else:

        if mid_elem <= search_elem <= array[right_index]:
            return search_index(array, search_elem, mid_index+1, right_index)
        else:
            return search_index(array, search_elem, left_index, mid_index+1)


if __name__ == '__main__':
    arr_length = int(input())
    element = int(input())
    arr = [int(num) for num in input().split()]
    medium_index = arr_length // 2
    print(search_index(arr, element, 0, arr_length-1))
