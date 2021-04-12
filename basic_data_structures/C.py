def c(input_str):
    max_len = 1
    for i in range(len(input_str)-1):
        count = 0
        chars = []
        for j in range(i, len(input_str)):
            char = input_str[j]
            if char in chars:
                break
            chars.append(char)
            count += 1

        if max_len < count:
            max_len = count
    return max_len


if __name__ == '__main__':
    input_str = input()
    print(c(input_str))
