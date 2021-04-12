def is_correct_bracket_seq(input_string):
    if len(input_string) == 0:
        return True
    elif len(input_string) % 2 == 1:
        return False
    for i in range(len(input_string)//2):
        x = input_string.replace('()', '')
        x = x.replace('[]', '')
        x = x.replace('{}', '')
        input_string = x
    if len(input_string) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    input_string = input()
    print(is_correct_bracket_seq(input_string))
