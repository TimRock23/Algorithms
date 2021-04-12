def o(first_server, second_users, second_server):
    for i in range(-second_users, 0):
       first_server[i] = second_server[i]
    result = sorted(first_server, key=int)
    return ' '.join(result)


if __name__ == '__main__':
    first_server = input().split(' ')
    first_users = int(input())
    second_users = int(input())
    second_server = input().split(' ')
    print(o(first_server, second_users, second_server))
