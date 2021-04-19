def d(num):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(num + 1)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    result = str(v2)[-1]
    return result


if __name__ == '__main__':
    num = int(input())
    print(d(num))
