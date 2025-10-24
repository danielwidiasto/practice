def maxProfit(self, prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    total_profit = 0

    for i in range(1, len(prices)):

        # Greedy decision: If today's price higher than yesterday
        # make transaction, to gain max profit

        if prices[i] > prices [i-1]:
            # The profit from this specific price rise is the difference
            daily_profit = prices[i] - prices[i-1]
            # Count profit
            total_profit += daily_profit

    return total_profit
