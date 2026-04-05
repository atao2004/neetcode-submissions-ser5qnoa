class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def backtrack():
            if len(stack)== len(nums):
                res.append(stack.copy())
                return
            for cur in nums:
                if cur not in stack:
                    stack.append(cur)
                    backtrack()
                    stack.pop()

        backtrack()
        return res
        
             