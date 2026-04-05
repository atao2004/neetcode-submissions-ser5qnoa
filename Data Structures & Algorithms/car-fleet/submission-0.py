class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []
        count = 0
        for pos, speed in zip(position, speed):
            pos_speed.append((pos, speed))
        pos_speed.sort(reverse=True)
        for p, s in pos_speed:
            time =(target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
                count += 1
        return count
            
