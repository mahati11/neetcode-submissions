class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        count = n
        temp = dict()
        diff= 0
        for i in range(n):
            temp[position[i]] = speed[i]
        arrange = sorted(position)[::-1]
        for i in range(n):
            dist = target - arrange[i] 
            time = dist / temp[arrange[i]]
            if time > diff:
                diff = time
            else:
                count -=1
        
        
        return count

