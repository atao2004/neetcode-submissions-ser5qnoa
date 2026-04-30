class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * (len(nums) + 1)

        def dfs(i):
            if i >=n:
                return memo[n]
            elif memo[i] != 0:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)
            
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i+1), nums[i] + dfs(i + 2))
        # return dfs(0)
        