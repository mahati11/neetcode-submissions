class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        for i in s:
            if not i.isalpha():
                if not i.isnumeric():
                    s = s.replace(i, '')
        s = s.replace(' ','')
        right = len(s) -1

        while left < right:
                
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True