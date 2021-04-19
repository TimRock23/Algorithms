def j(count, stairs):
    stair = stairs[0]
    index = 0
    for i in range(count):
        if index + stair >= count:
            return True
        jump_list = stairs[index+1:index+stair+1]
        if not jump_list:
            return False
        max_num = 0
        max_ind = 0
        for ind, elem in enumerate(jump_list):
            if elem >= max_num:
                max_num = elem
                max_ind = ind + 1
        stair = max_num
        index += max_ind
    return False


if __name__ == '__main__':
    count = int(input())
    stairs = list(map(int, input().split(' ')))
    print(j(count, stairs))
