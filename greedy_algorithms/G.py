def g(count, nums):
    result = []
    imd_result = 1
    for i in range(count-1):
        if nums[i] < nums[i+1]:
            imd_result += 1
        else:
            result.append(imd_result)
            imd_result = 1
    if not result:
        return imd_result
    else:
        return max(result)


if __name__ == '__main__':
    count = int(input())
    nums = list(map(int, input().split(' ')))
    print(g(count, nums))
