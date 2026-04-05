class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        stack = []
        max_length = 0
        for num in nums:
            # skip dups
            if stack and stack[-1] == num:
                continue
            elif stack and num - stack[-1] > 1:
                stack.clear()
                stack.append(num)
            else:
                stack.append(num)
            max_length = max(max_length, len(stack))
        return max_length