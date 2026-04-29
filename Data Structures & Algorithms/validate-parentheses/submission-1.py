class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == ")" or c== "]" or c=="}") and not stack:
                return False
            if (c == ")" or c== "]" or c=="}") and stack:
                open_bracket = stack.pop()
                if c == ")" and open_bracket != "(":
                    return False
                elif c == "]" and open_bracket != "[":
                    return False
                elif c == "}" and open_bracket != "{":
                    return False
                else:
                    continue
            stack.append(c)
        if stack:
            return False
        return True
        