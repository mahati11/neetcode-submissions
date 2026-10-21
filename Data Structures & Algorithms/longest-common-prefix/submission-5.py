class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if "" in strs:
            return ""

        mini = len(strs[0])
        ind = 0
        for i,v in enumerate(strs):
            n = len(v)
            if mini > n:
                mini = n
                ind = i 
        res = strs[ind]
        
        ans  =''
        for i in range(mini):
            temp = res[i]
            inc = True
            for j in strs:
                if temp != j[i]:
                    inc = False
                    break
            
            if inc == True:
                ans += temp
            else:
                return ans
        return ans       
                    