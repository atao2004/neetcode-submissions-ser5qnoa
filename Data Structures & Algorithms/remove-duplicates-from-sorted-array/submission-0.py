class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == nums[l]:
                del nums[r]
                continue
            r += 1
            l += 1
        return len(nums)