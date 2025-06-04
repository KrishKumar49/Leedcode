def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for p in prices:
        if p < min_price:
            min_price = p
            
        profit = p - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4])) 