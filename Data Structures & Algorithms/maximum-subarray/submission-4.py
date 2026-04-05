class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if curSum < 0 we staRT NEW
        cursum = nums[0]
        maxsum = nums[0]
        for num in nums[1:]:
            if cursum + num < num:
                cursum = num
            else:
                cursum += num
            if cursum > maxsum:
                maxsum = cursum
        return maxsum


        