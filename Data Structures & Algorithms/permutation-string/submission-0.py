class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_length = len(s1)
        if len(s2) < len(s1):
            return False
        r = window_length 
        l = 0

        s1_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] +=1
        while(r <= len (s2)):
            # compare dicts
            s2_dict = defaultdict(int)
            substring = s2[l:r]
            for c in substring:
                s2_dict[c] +=1
            
            if s1_dict == s2_dict:
                return True

            l += 1
            r += 1
        return False

        