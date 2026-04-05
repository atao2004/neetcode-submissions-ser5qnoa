class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def checkCorrect(eatingRate):
            numHours = 0
            for pile in piles:
                if pile <= eatingRate:
                    numHours += 1
                else:
                    numHours += math.ceil(pile/eatingRate)
            return h>=numHours
        while l < r:
            m = (l+r) // 2
            if checkCorrect(m):
                r = m
            else:
                l = m+1
        return l





