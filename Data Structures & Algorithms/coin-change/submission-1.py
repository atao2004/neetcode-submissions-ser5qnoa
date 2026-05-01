class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def change(amount):
        #     if amount == 0:
        #         return coins
        #     if amount < 0:
        #         return 1000000
        #     return 1 + min(change(amount - coin) for coin in coins)
        # return change(amount)
        n = len(coins)
        memo = {} # AMOUNT:num coins
        def change(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            memo[amount] =1+ min(change(amount - coin)for coin in coins)
            return memo[amount]
        return change(amount) if change(amount) != float('inf') else -1
            