def c(count, input_list, plus):
    result = 0
    for num in input_list:
        count -= 1
        result += int(num)*(10**count)
    final_num = result + plus
    result_list = ' '.join(list(str(final_num)))
    return result_list


if __name__ == '__main__':
    count = int(input())
    input_list = input().split(' ')
    plus = int(input())
    print(c(count, input_list, plus))
