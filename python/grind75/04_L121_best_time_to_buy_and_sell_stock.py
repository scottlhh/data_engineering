"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

def find_best_time(prices : list[int]) -> tupple[int, int, int]:
    curr_buy_idx = 0
    curr_sell_idx = 0
    max_profit = 0
    new_buy_idx = 0
    for i, price in enumerate(prices):
        # higer price found
        if price > prices[curr_sell_idx]:
            curr_sell_idx = i
            max_profit = price - prices[curr_buy_idx]
            # if previous new low found, update max profit
            if price - prices[new_buy_idx] > max_profit:
                max_profit = price - prices[new_buy_idx]
                curr_buy_idx = new_buy_idx
        # new low found
        elif price < prices[curr_buy_idx]:
            new_buy_idx = i
            if max_profit==0:
                curr_buy_idx = i
                curr_sell_idx = i
    return (curr_buy_idx, curr_sell_idx, max_profit)


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = find_best_time(prices)
    assert res == (1, 4, 5), '1, 4, 5'

    prices = [7,6,5,4,3,2]
    res = find_best_time(prices)
    assert res == (5, 5, 0), '5, 5, 0'

    prices = [1,1,5,7,8,4]
    res = find_best_time(prices)
    assert res == (0, 4, 7), '0, 4, 7'

    prices = [9,2,5,7,8,4,6, 4,7,1,2,3,2,1,9]
    res = find_best_time(prices)
    assert res == (13, 14, 8), '8, 13, 8'
