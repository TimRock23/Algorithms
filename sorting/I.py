def i(colors):
    colors_dict = {'0': 0, '1': 0, '2': 0}
    for i in colors:
        colors_dict[i] += 1
    for key, value in colors_dict.items():
        while value > 0:
            print(key, end=' ')
            value -= 1


if __name__ == '__main__':
    count = int(input())
    if count != 0:
        colors = input().split(' ')
        i(colors)
