class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        post_max = [0]*len(prices)
        curr_max = 0
        max_profit = 0
        for i in range(len(prices)-2,-1,-1):
            curr_max = max(prices[i+1], curr_max)
            post_max[i] = curr_max
        for i in range(len(prices)):
            max_profit = max(max_profit, post_max[i]-prices[i])
        return max_profit
