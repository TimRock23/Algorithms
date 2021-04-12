def b(nums, k):
    result = {}
    for num in nums:
        if num not in result:
            result[num] = 1
        if num in result:
            result[num] += 1
    final = sorted(result, key=result.get, reverse=True)[:k]
    return ' '.join(final)


if __name__ == '__main__':
    total_students = input()
    nums = input().split(' ')
    k = int(input())
    print(b(nums, k))
