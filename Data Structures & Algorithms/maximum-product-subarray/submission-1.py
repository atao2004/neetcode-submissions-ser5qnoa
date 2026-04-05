class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max= cur_min= res = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)

            res = max(res, cur_max)
        return res
        # cursum, curmin, maxsum = nums[0]
        # # maxsum = nums[0]
        # for num in nums[1:]:
        #     if cursum * num < cursum:
        #         cursum = 1
        #     cursum = max(cursum * num, cursum)
        #     maxsum = max(cursum, maxsum)
        # return maxsum