def j(numbers):
    result = {}
    for num in numbers:
        if num not in result:
            result[num] = 0
        result[num] += 1
    res = sorted(result, key=result.get)[0]
    return res


if __name__ == '__main__':
    count = input()
    numbers = input().split(' ')
    print(j(numbers))
