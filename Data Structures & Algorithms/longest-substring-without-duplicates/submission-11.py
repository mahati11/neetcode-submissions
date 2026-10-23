class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n ==0 :
            return 0
        if n==1:
            return 1
        temp = set()
        l = 0
        ans = 0
        for r in range(n):
            while s[r] in temp:
                temp.remove(s[l])
                l +=1
            temp.add(s[r])
            ans = max(ans, r-l +1)
        return ans

           