class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        j = 1
        if n ==1:
            return 1
        while i < j and j < n:
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i +=1   
            j+=1
        return i+1
            

