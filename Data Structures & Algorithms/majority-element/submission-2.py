class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        c = {}
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                if nums[i] not in c:
                    c[nums[i]]  = 2
                else:
                    c[nums[i]] +=1
            else:
                if nums[i] not in c:
                    c[nums[i]]  = 1
                
        print(c)        
        m  = c[nums[0]]
        res = nums[0]
        for k,v in c.items():
            if v > m:
                m = v
                res = k
        return res
        