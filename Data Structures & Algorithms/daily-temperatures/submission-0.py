class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force = double for loop to find the next element that has a higher temp
        # one pass O(n) monotonic stack of only decreasing values - once we find a value that is greater than top of stack
            # we can pop everything else out
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < curr_temp:
                past_index = stack.pop()
                num_days_after = i - past_index
                result[past_index] = (num_days_after)
            stack.append(i)
        # while stack:
        #     stack.pop()
        #     result.append(0)
        return result


