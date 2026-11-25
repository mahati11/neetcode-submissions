class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n >= k:
            diff = n-k
        elif n < k:
            diff = n - (k%n)
            # diff = (n-diff) 
        

        temp = nums[diff:]
        for j in temp:
            nums.remove(j)
        for i in temp[::-1]:
            nums.insert(0, i)

       