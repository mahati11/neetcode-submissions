class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        o=z=t=0
        for i in nums:
            if i == 0:
                z +=1
            elif i == 1:
                o+=1
            else:
                t+=1
        
        for i in range(0,z):
            
            nums[i] = 0
        for i in range(z,o+z):
            nums[i] = 1
        for i in range(o+z, n):
            nums[i] = 2
        