class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = list()
        res = 0
        
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                temp.append(int(i))
            else:
              
                a = temp.pop(-2)
                b = temp.pop(-1)
                if i == '+':
                    temp.append(a+b)
                if i == '*':
                    temp.append(a*b)
                if i == '-':
                    temp.append(a-b)
                if i == '/':
                    if a !=0:
                        temp.append(int(a/b))
                    else:
                        temp.append(0)
        return temp[0]




