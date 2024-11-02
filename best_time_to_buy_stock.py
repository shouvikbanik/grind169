def max_profit(prices):
    buy = 0
    sell = buy + 1
    maximum_profit = 0
    while sell < len(prices):
        if prices[buy] > prices[sell]:
            buy = sell
        else:
            maximum_profit = max(maximum_profit, (prices[sell] - prices[buy]))
        sell += 1
    return maximum_profit
