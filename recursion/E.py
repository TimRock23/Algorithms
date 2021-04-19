def e(number):

    def factorial(num):
        if num <= 1:
            return 1
        return num * factorial(num - 1)

    factorial(number)


if __name__ == '__main__':
    number = int(input())
    print(e(number))
