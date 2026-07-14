class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == len(set(nums)):
            return False
        return True