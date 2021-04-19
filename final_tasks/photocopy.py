def photocopy(count_servers, server_sizes):
    server_sizes.sort()
    min_size_server = 0
    max_size_server = count_servers - 1
    count_photos = 0
    while min_size_server != max_size_server:
        if server_sizes[max_size_server] < server_sizes[max_size_server-1]:
            server_sizes.sort()
        if server_sizes[min_size_server] == 0:
            min_size_server += 1
        else:
            server_sizes[max_size_server] -= 1
            server_sizes[min_size_server] -= 1
            count_photos += 1

    return count_photos


if __name__ == '__main__':
    count = int(input())
    if count > 1:
        arr = [int(num) for num in input().split()]
        print(photocopy(count, arr))
    else:
        print(0)
