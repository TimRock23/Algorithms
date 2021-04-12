def b(str_count, column_count, matrix):
    right_matrix = []

    for i in range(column_count):
        right_matrix.append(list())
        for j in range(str_count):
            right_matrix[i].append(0)

    for i in range(str_count):
        for j in range(column_count):
            right_matrix[j][i] = matrix[i][j]

    [print(' '.join(line)) for line in right_matrix]


if __name__ == '__main__':
    str_count = int(input())
    column_count = int(input())
    matrix = [input().split() for i in range(str_count)]
    b(str_count, column_count, matrix)
