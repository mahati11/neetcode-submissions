class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n//2
        left = 0
        right = n-1
        
        while left <=  right:
            if  target < nums[mid]:
                right = mid -1
            if target > nums[mid]:
                left = mid +1
            if target == nums[mid]:
                return mid
            mid = (right - left)//2 + left
            
        return -1

