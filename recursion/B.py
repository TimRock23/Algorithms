def b(numbers):
    count, degree = numbers[0], numbers[1]
    v1, v2, v3 = 1, 1, 0
    for rec in bin(count+1)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    result = v2 % 10 ** degree
    return result


if __name__ == '__main__':
    numbers = list(map(int, input().split(' ')))
    print(b(numbers))
