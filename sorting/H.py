def h(count, flowerbeds):
    flowerbeds = sorted(flowerbeds, key=lambda i: [i[0], -i[1]])
    result = []
    for i in range(count-1):
        if (flowerbeds[i][1] >= flowerbeds[i+1][0]) and (
                flowerbeds[i+1][0] <= flowerbeds[i][1]):
            flowerbeds[i+1][0] = min(flowerbeds[i][0], flowerbeds[i+1][0])
            flowerbeds[i+1][1] = max(flowerbeds[i][1], flowerbeds[i+1][1])
        else:
            result.append(flowerbeds[i])
    result.append(flowerbeds[-1])
    for i in result:
        print(*i)


h()
if __name__ == '__main__':
    count = int(input())
    flowerbeds = []
    for i in range(count):
        flowerbed = list(map(int, input().split(' ')))
        flowerbeds.append(flowerbed)
    h(count, flowerbeds)
