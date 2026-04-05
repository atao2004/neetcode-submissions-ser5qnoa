class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i, remaining):
            if remaining < 0 or i >= len(nums):
                if sum(path) == target:
                    res.append(path.copy())
                return
            # include nums[i] many times
            path.append(nums[i])
            backtrack(i, remaining - nums[i])
            path.pop()

            # # include nums[i] once 
            # path.append(nums[i])
            # backtrack(i + 1)
            # path.pop()

            #dont include nums[i]
            backtrack(i+1, remaining)


        backtrack(0, target)
        return res