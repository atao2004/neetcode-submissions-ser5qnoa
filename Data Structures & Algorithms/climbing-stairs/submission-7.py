class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 3 => (n=2)+(n=1)+(n=0)
        # memo arr which stores index:num steps
        # memo = [0] * (n+1)
        # memo[0] = 0
        # memo[1] = 1
        # if n >= 2:
        #     memo[2] = 2
        #     for i in range(3, n+1):
        #         memo[i] = memo[i-1] + memo[i-2]
        # return memo[n]
        a, b = 1, 2
        if n <= 2:
            return n
        for i in range(3, n+1):
            a, b = b, a+b
        return b
        # def dp(i):
        #     if i == 1:
        #         return 1
        #     elif i == 2:
        #         return 2
        #     elif memo[i] != 0:
        #         return memo[i]
        #     memo[i] = dp(i-1) + dp(i-2)
        #     return memo[i]
        # return dp(n)

