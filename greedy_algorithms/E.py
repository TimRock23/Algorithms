def e(cookie_size, kids_count, greed_factor):
    count = 0
    for size in cookie_size:
        if count >= kids_count:
            break
        if size >= greed_factor[count]:
            count += 1
    return count


if __name__ == '__main__':
    kids_count = int(input())
    greed_factor = sorted(list(map(int, input().split(' '))))
    cookie_count = int(input())
    cookie_size = sorted(list(map(int, input().split(' '))))
    print(e(cookie_size, kids_count, greed_factor))
