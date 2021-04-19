def c(s, t):
    lst = []
    num = 0
    for i in t:
        if lst == s:
            return True
        if i == s[num]:
            num += 1
            lst.append(i)
        if lst == s:
            return True
    return False


if __name__ == '__main__':
    s = list(input())
    t = list(input())
    print(c(s, t))
