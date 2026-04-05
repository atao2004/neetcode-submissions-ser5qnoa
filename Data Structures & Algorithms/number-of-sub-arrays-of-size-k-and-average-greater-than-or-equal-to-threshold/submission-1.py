class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        curSum =0
        count =0
        target = threshold * k
        for r in range(len(arr)):
            curSum += arr[r]
            # if r - l + 1 < k:
            #     curSum += arr[r]
            if r - l + 1 > k:
                curSum -= arr[l]
                l += 1
            if curSum >= target and r - l + 1 == k:
                count += 1
        return count