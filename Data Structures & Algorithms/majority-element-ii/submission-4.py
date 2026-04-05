class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # stack = []
        # threshold = (len(nums)) // 3
        # res = []
        # visited = set()
        # for num in nums:
        #     if stack and stack[-1] == num:
        #         stack.append(num)
        #     if stack and stack[-1] != num:
        #         stack.clear()
        #         stack.append(num)
        #     else: # stack not initialized
        #         stack.append(num)
        #     if len(stack) > threshold and stack[-1] not in visited:
        #         res.append(stack[-1])
        #         visited.add(stack[-1])
        # return res
        counts = Counter(nums)
        res = []
        for val, count in counts.items():
            if count > len(nums)//3:
                res.append(val)
        return res
