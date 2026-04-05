class Solution:
    def findMin(self, nums: List[int]) -> int:
        # pivot point of nums[mid+1] < nums[mid] for soem arbitrary mid
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            # if nums[m+1] < nums[m]:
            #     return nums[m+1]
            if nums[m] < nums[r]:
                r = m
            if nums[m] > nums[r]:
                l = m + 1
        return nums[r]