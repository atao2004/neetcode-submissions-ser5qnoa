class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return True
            # left side sorted
            if nums[l] == nums[m]:
                l += 1
            elif nums[l] < nums[m]:
                # in range
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # not in range
                else:
                    l = m + 1
            # right side sorted
            else:
                # in range
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # not in range
                else:
                    r = m - 1
        return False