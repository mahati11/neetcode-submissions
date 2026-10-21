class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
       
        
        n = len(nums)
        if n == 0:
            return 0
        if n ==1:
            return 1
        l = res = 0
        r = 1
        ans = 1
        while l<r and r<n:
            if nums[l] + 1 == nums[r]:
                ans+=1
            elif nums[l] == nums[r]:
                l+=1
                r+=1
                continue
            else:
                res = max(res,ans)
                ans =  1
            l +=1
            r +=1

        return max(res, ans)






