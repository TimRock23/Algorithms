def b(priceperday):
    stonks = 0
    for i in range(count):
        if i == 0:
            pass
        elif priceperday[i] > priceperday[i-1]:
            stonks += priceperday[i] - priceperday[i-1]
    return stonks


if __name__ == '__main__':
    count = int(input())
    priceperday = list(map(int, input().split(' ')))
    print(b(priceperday))
