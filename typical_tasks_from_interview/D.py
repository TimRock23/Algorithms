def d(input_list):
    result_list = [i for i in input_list if int(i) != 0]
    return ' '.join(result_list)


if __name__ == '__main__':
    count = int(input())
    input_list = input().split()
    print(d(input_list))
