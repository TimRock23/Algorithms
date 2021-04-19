def biggest_num(numbers):
    result = sorted(numbers, key=CMP, reverse=True)
    return ''.join(result)


def my_cmp(x, y):
    return (x + y) < (y + x)


class CMP:
    def __init__(self, obj, *args):
        self.obj = obj

    def __lt__(self, other):
        return my_cmp(self.obj, other.obj)


if __name__ == '__main__':
    count = int(input())
    if count != 0:
        nums = input().split()
        print(biggest_num(nums))
