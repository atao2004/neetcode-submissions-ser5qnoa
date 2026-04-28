class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        n = len(chars)
        written = 0
        for r in range(n):
            # repeat
                #do nothing
            # not repeat
            if r == n-1 or chars[r+1] != chars[l]:
                chars.append(chars[l])
                if r-l + 1 > 1:
                    # count > 1
                    for c in str(r-l+1):
                        chars.append(c)
                l=r+1

        del chars[:n]
        return len(chars)
                
                

