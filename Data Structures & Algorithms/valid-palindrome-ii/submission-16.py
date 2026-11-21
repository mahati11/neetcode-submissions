class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0 
        r = n  - 1
        
        def check(s):
            if s == s[::-1]:
                return True
            else:
                return False
        
        
        if not check(s):
            while l < r:
                if s[l] != s[r]:
                    if check(s[l+1:r+1]) == True:
                        return True
                    if check(s[l:r])  == True:
                        return True
                    return False
                l+=1
                r-=1
        else:
            return True

        


