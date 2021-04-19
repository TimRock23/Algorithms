def c(count):
    nums = {0: 1, 1: 1}

    def fibonacci(num):
        if num in nums:
            return nums[num]

        nums[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return nums[num]

    return fibonacci(count)


if __name__ == '__main__':
    count = int(input())
    print(c(count))
