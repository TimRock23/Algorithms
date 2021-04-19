def f(number):
    if number == 0:
        return print(0)
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


if __name__ == '__main__':
    number = int(input())
    print(f(number))
