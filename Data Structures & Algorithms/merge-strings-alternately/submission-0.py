class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        
        res = ''
        t = min(m,n)
        for i in zip(word1, word2):
            res += i[0] + i[1]

        if t == n and m>n:
            res += word2[n:]
        if t == m and n>m:
            res+= word1[m:]
        
        return res

