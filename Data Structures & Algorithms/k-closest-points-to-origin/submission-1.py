class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def l2_dist(x1, y1, x2,  y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        # create a minheap 
        nums = []
        for pair in points:
            dist = l2_dist(pair[0], pair[1], 0, 0)
            print(dist)
            nums.append((dist, pair))
        heapq.heapify(nums)

        res =[]
        for i in range(k):
            res.append((heapq.heappop(nums)[1]))
        return res





        

