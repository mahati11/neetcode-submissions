class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = multiple = False

        n = len(nums)
        res = [0]*n
        for i in nums:
            if i != 0 :
                product *= i
        if 0 in nums:
            zero = True
            c = nums.count(0)
            if c > 1:
                multiple = True
        if zero == True and multiple ==True:
            return res
        elif zero == True and multiple == False:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = product
        else:
            for i in range(n):
                res[i] = product // nums[i]
        return res

                
