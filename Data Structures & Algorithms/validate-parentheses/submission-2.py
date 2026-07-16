class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            
            if i == '[':
                temp.append('[')
            if i == '{':
                temp.append('{')
            if i == '(':
                temp.append('(')
            if i == '}':
                if not temp: 
                    return False
                if temp[-1] != '{':
                    return False
                else:
                    temp.pop(-1)
            if i == ']':
                if not temp: 
                    return False
                if temp[-1] != '[':
                    return False
                else:
                    temp.pop(-1)
            if i == ')':
                if not temp: 
                    return False
                if temp[-1] != '(':
                    return False
                else:
                    temp.pop(-1)
        if len(temp) ==0:
            return True
        return False
            
