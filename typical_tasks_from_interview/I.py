def i(first_num, second_num):
    if len(first_num) >= len(second_num):
        max_len = len(first_num)
        list(first_num).append(0)
        max_num = list(first_num)
        max_num.reverse()
        min_num = list(second_num)
        min_num.reverse()
    else:
        max_len = len(second_num)
        list(second_num).append(0)
        max_num = list(second_num)
        max_num.reverse()
        min_num = list(first_num)
        min_num.reverse()

    while len(min_num) < len(max_num):
        min_num.append(0)

    new_list = [0 for j in range(max_len+1)]
    x = 0
    for j in max_num:
        summ = int(j) + int(min_num[x]) + new_list[x]
        if summ in (0, 1):
            new_list[x] = summ
        elif summ == 2:
            new_list[x] = 0
            new_list[x+1] = 1
        elif summ == 3:
            new_list[x] = 1
            new_list[x+1] = 1
        x += 1
    result = ''.join(str(j) for j in new_list[::-1])
    return result


if __name__ == '__main__':
    first_num = input()
    second_num = input()
    print(i(first_num, second_num))
