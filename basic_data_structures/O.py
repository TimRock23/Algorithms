def o(have, search):
    variants_have = []
    count = 0
    for i in range(len(have)):
        variant = sorted(have[i:i+len(search)])
        variants_have.append(''.join(variant))
    search = ''.join(sorted(search))
    for variant in variants_have:
        if variant == search:
            count += 1
    return count


if __name__ == '__main__':
    have = input()
    search = input()
    print(o(have, search))
