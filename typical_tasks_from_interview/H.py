punctuation = [' ', '.', ',', '!', '?', ':', ';']


def h(word):
    word_low = word.lower()
    new_word = ''.join(sign for sign in word_low if sign not in punctuation)
    return new_word == new_word[::-1]


if __name__ == '__main__':
    word = input()
    print(h(word))
