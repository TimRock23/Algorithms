def d(max_value, values):
    sorted_values = sorted(values, key=lambda item: (-item[0], item[1]))
    in_backpack = []
    for value in sorted_values:
        if value[1] <= max_value:
            max_value -= value[1]
            in_backpack.append(value[2])
    result = sorted(in_backpack)
    print(*result)


if __name__ == '__main__':
    max_value = int(input())
    count = int(input())
    values = []
    for i in range(count):
        value = input().split(' ')
        value.append(i)
        value = list(map(int, value))
        values.append(value)
    d(max_value, values)
