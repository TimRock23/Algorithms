def g(first_word, second_word):
    first_list = sorted(list(first_word))
    second_list = sorted(list(second_word))
    return first_list == second_list


if __name__ == '__main__':
    first_word = input()
    second_word = input()
    print(g(first_word, second_word))
