class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0,1
        n = len(nums)
        for i in range(n):
            j = i+1
            while abs(i-j) <= k and j < n:
                if nums[i] == nums[j]:
                    return True
                j+=1
        return False