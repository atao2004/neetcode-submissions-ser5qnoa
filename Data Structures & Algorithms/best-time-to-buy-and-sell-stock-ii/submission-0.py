class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff_arr = [0] * (len(prices) - 1)
        for i in range(len(prices) - 1, 0, -1):
            diff = prices[i] - prices[i-1]
            diff_arr[i-1] = diff
        max_profit = 0
        for num in diff_arr:
            if num > 0:
                max_profit += num
        return max_profit