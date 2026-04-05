class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        r = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
                # r += 1
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                visited.add(s[r])
                # r += 1
            max_len = max(max_len, len(visited))
        return max_len

