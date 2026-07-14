class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = j = 0 
        n = len(nums)
        while i < n:
            temp = target - nums[i]
            j = i+1
            while j < n:
                if nums[j] == temp:
                    return [i, j]
                j+=1
            i+=1


