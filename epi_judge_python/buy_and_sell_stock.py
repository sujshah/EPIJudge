from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    maximum_value, maximum_profit = 0, 0
    for price in reversed(prices):
        maximum_profit = max(maximum_profit, maximum_value - price)
        maximum_value = max(maximum_value, price)
    return maximum_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
