def i(count, budget, prices):
    to_buy = 0
    for i in range(count):
        if prices[i] <= budget:
            budget -= prices[i]
            to_buy += 1
        else:
            break
    return to_buy


if __name__ == '__main__':
    count_budget = list(map(int, input().split(' ')))
    count = count_budget[0]
    budget = count_budget[1]
    prices = sorted(list(map(int, input().split(' '))))
    print(i(count, budget, prices))
