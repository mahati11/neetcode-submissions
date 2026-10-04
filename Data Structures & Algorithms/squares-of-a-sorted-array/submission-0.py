class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        neg_a = []
        pos_a = []
        if nums[0] >=0 :
            neg = False
        else:
            neg = True
        
        if neg == False:
            for i in range(n):
                nums[i] = nums[i]**2
            return nums

        for i in range(n):
            if nums[i] < 0:
                neg_a.append(nums[i])
            else:
                pos_a.append(nums[i])
        l = len(neg_a)
        m = len(pos_a)
        for i in range(l):
            neg_a[i] = neg_a[i]**2
        for i in range(m):
            pos_a[i] = pos_a[i]**2
        res = []
        left = right =  0
        neg_a = neg_a[::-1]
        while left < l and right < m:
            if neg_a[left] <= pos_a[right]:
                res.append(neg_a[left])
                left+=1
            else:
                res.append(pos_a[right])
                right+=1
        if n != len(res):
            if left == l:
                temp =pos_a[right:]
                for i in temp:
                    res.append(i)
            elif right == m:
                temp = neg_a[left:]
                for i in temp:
                    res.append(i)
                
        return res




        
        


        
