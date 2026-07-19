class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        n = len(heights)
        right = n - 1
        res  = 0 
        # while left <  n:
        #     right = n - 1
        while left <  right:
            b = right - left 
            l = min(heights[left], heights[right])
            res = max(res, l*b)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
                
        return res

