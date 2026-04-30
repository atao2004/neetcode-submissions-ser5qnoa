class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (len(nums) + 1)
        memo[0] = nums[0]
        if n > 1:
            memo[1] = max(nums[0], nums[1])
        for i in range(2, n):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2])
        return memo[n-1]


        # def dfs(i):
        #     if i >=n:
        #         return memo[n]
        #     elif memo[i] != 0:
        #         return memo[i]
        #     memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
        #     return memo[i]
        # return dfs(0)
            
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i+1), nums[i] + dfs(i + 2))
        # return dfs(0)
        