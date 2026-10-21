class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = {}
        a = []
        for i in nums:
            if i not in c:
                c[i] = 1    
            else:
                c[i] +=1
        
        for k,v in c.items():
            if v > n/3:
                a.append(k)
        return a
