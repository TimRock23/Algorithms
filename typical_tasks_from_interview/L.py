def l(first_str, second_str):
    letter_dict = {}
    for letter in first_str:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    for letter in second_str:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    for item in letter_dict.items():
        if item[1] % 2 == 1:
            return item[0]


if __name__ == '__main__':
    first_str = input()
    second_str = input()
    print(l(first_str, second_str))
