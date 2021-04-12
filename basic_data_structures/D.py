def d(str_num, column_num, matrix, target_str, target_col):
    nums = []
    if 0 < target_str < str_num - 1:
        nums.append(matrix[target_str-1][target_col])
        nums.append(matrix[target_str+1][target_col])
    elif target_str == str_num - 1 and str_num > 1:
        nums.append(matrix[target_str - 1][target_col])
    elif target_str == 0 and str_num > 1:
        nums.append(matrix[target_str + 1][target_col])

    if 0 < target_col < column_num - 1:
        nums.append(matrix[target_str][target_col-1])
        nums.append(matrix[target_str][target_col+1])
    elif target_col == column_num - 1 and column_num > 1:
        nums.append(matrix[target_str][target_col-1])
    elif target_col == 0 and column_num > 1:
        nums.append(matrix[target_str][target_col+1])

    return ' '.join(sorted(nums, key=int))


if __name__ == '__main__':
    str_num = int(input())
    column_num = int(input())
    matrix = []
    for i in range(str_num):
        matrix.append([j for j in input().split(' ')])
    target_str = int(input())
    target_col = int(input())
    print(d(str_num, column_num, matrix, target_str, target_col))
