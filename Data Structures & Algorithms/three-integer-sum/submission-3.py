class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[i] + nums[r] == 0:
                    res.append((nums[l], nums[i], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1] and l < r:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return res

