class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical slice across all strings
        # n = len(strs[0])
        longest = ""
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]):
                    return longest
                if strs[0][j] != strs[i][j]:
                    return longest
            longest += (strs[0][j])
        return longest


