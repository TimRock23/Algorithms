def k(number):
    count_one = 0
    while number > 0:
        reminder = number % 2
        count_one += reminder
        number = number // 2
    return count_one


if __name__ == '__main__':
    num = int(input())
    print(k(num))
