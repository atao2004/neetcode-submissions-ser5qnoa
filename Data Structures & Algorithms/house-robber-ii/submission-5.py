class Solution:
    def rob(self, nums: List[int]) -> int:
        # we include the first house or we include the last house 0:n-2 or 1:n-1
        # otherwise similar to house robber 1

        # def dfs(i, n):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i+1, n), nums[i] + dfs(i+2, n))
        # return max(dfs(0, len(nums)-1), dfs(1, len(nums)))
       
        # def dfs(arr):
        #     n = len(arr)
        #     memo = [0] * (n+1)
        #     if n == 1:
        #         return arr[0]
        #     memo[0] = arr[0]
        #     memo[1] = max(arr[0], arr[1])
        #     for i in range(2, n):
        #         memo[i] = max(memo[i-1], arr[i] + memo[i-2])
        #     return memo[n-1]
        # if len(nums) == 1:
        #     return nums[0]
        # return max(dfs(nums[:-1]), dfs(nums[1:]))
        if len(nums) == 1:
            return nums[0]
        def dp(arr):
            if len(arr) == 1:
                return arr[0]
            a = arr[0]
            b = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                a, b = b, max(b, arr[i] + a)
            return b
        return max(dp(nums[:-1]), dp(nums[1:]))


