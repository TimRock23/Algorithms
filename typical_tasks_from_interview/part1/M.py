def m(str_in):
    letter_dict = {}
    for letter in str_in:
        if letter not in letter_dict:
            letter_dict[letter] = 0
        letter_dict[letter] += 1

    sorted_dict = sorted(
        letter_dict.items(), key=lambda item: (-item[1], item[0]))
    sorted_list = [i[0]*i[1] for i in sorted_dict]
    return ''.join(sorted_list)


if __name__ == '__main__':
    str_in = input()
    print(m(str_in))
