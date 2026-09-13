class Solution:
    def calculate_hours(self, piles, speed):
        hours = 0
        for p in piles:
            # ceil(p / speed)
            hours += (p + speed - 1) // speed
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hours = self.calculate_hours(piles, mid)
            
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
