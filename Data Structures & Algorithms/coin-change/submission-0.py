class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain):
            if remain < 0:
                return 1e9
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            memo[remain] = 1 + min(dfs(remain - coin) for coin in coins)
            return memo[remain]
        
        res= dfs(amount)
        return res if res <= 1e9 else -1