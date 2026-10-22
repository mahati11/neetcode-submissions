class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n < 4:
            return []
        if n == 4:
            if sum(nums) == target:
                return [nums]
            return []
        ans = []
        i = 0
        while i < n-3:
            j = i+1
            while j < n-2:
                l = j+1
                r = n-1
                a = target - (nums[i]+nums[j]) 
                while l < r and r < n:
                    if nums[l] + nums[r] == a:
                        t = [nums[i], nums[j], nums[l], nums[r]]
                        if t not in ans:
                            ans.append(t)
                        l+=1
                        r-=1
                    if nums[l] + nums[r] < a:
                        l+=1
                    if nums[l] + nums[r] > a:
                        r-=1
                j+=1
            i+=1
        
        return ans
                        









        
