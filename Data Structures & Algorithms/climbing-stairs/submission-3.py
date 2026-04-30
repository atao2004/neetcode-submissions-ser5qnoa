class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 3 => (n=2)+(n=1)+(n=0)
        # memo arr which stores index:num steps
        memo = [0] * (n+1)
        def dp(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2
            elif memo[i] != 0:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)

