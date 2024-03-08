prices = [7,1,5,3,6,4]
lowest = min(prices)
lowest_price = prices[0]
highest = max(prices)
highest_price = prices[0]
for price in prices:
    if price == lowest:
        lowest_price = price
    if price == highest:
        highest_price = price
    if prices.index(lowest) > prices.index(highest):
        index_lowest = prices.index(lowest)
        index_highest = prices.index(highest)

        print(index_lowest,index_highest, lowest_price, highest_price, highest_price-lowest_price)


    print(highest_price, lowest_price)

