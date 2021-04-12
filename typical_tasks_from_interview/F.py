def f(num_list):
    k = 1
    for i in num_list:
        for num in num_list[k:]:
            if i == num:
                print(num)
                break
        k += 1


if __name__ == '__main__':
    count = int(input())
    num_list = input().split(' ')
    print(f(num_list))
