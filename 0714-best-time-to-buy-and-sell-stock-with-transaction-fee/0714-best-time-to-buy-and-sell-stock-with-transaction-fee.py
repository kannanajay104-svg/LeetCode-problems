class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            old_cash = cash
            cash = max(cash, hold + price - fee)
            hold = max(hold, old_cash - price)

        return cash