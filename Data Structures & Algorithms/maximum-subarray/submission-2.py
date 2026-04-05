class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        curSum = 0
        for num in nums:
            if num + curSum >= num:
                curSum = num + curSum
                curMax = max(curSum, curMax)

            else:# less than
                curSum = num
                curMax = max(curSum, curMax)

        return curMax

        