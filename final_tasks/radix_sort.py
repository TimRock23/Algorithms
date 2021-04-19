def counting_sort(array, exp):
    n = len(array)
    output = [0] * n
    digits_counter = [0] * 10

    for elem in array:
        digit = int(elem / exp % 10)
        digits_counter[digit] += 1

    for i in range(1, 10):
        digits_counter[i] += digits_counter[i - 1]

    for i in range(n - 1, -1, -1):
        digit = int(array[i] / exp % 10)
        digit_value = digits_counter[digit] - 1
        output[digit_value] = array[i]
        digits_counter[digit] -= 1

    return output


def radix_sort(array):
    max1 = max(array)

    exp = 1
    while max1 // exp > 0:
        array = counting_sort(array, exp)
        exp *= 10

    return array


if __name__ == '__main__':
    input()
    arr = [int(num) for num in input().split()]
    print(*radix_sort(arr))
