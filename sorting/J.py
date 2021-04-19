def j():
    n = int(input())
    if n == 0:
        return
    n_arr = list(map(int, input().split(' ')))
    m = int(input())
    if m == 0:
        n_arr.sort()
        return print(*n_arr)
    m_arr = list(map(int, input().split(' ')))
    other = []
    res_dict = {}
    for i in m_arr:
        res_dict[i] = 0
    for i in n_arr:
        if i in res_dict:
            res_dict[i] += 1
        else:
            other.append(i)
    other.sort()
    for key, value in res_dict.items():
        while value > 0:
            print(key, end=' ')
            value -= 1
    print(*other)


j()
