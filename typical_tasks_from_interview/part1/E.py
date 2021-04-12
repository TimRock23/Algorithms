def e(num_ten):
    num_two = ''
    while num_ten > 0:
        reminder = str(num_ten % 2)
        num_two = reminder + num_two
        num_ten = num_ten // 2
    return num_two


if __name__ == '__main__':
    num_ten = int(input())
    print(e(num_ten))
