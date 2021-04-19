def f(str_length, str_count, strings):
    count = 0
    for column in range(str_length):
        for string in range(str_count - 1):
            if strings[string][column] > strings[string + 1][column]:
                count += 1
                break
    return count


if __name__ == '__main__':
    str_count = int(input())
    str_length = int(input())
    strings = []
    for column in range(str_count):
        strings.append(input())
    print(f(str_length, str_count, strings))
