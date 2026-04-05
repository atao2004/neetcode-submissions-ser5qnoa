class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        path = []

        def backtrack(i, remainder):
            if remainder == 0:
                res.append(path.copy()) 
                return
            if remainder < 0 or i >= len(candidates):
                return   
            # include candidates[i]
            path.append(candidates[i])
            backtrack(i + 1, remainder - candidates[i])
            path.pop()
            # dont include candidates[i] and skip dups
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1   
            backtrack(i+1, remainder)
        backtrack(0, target)
        return res
        