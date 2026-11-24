class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s= sorted(people)[::-1]
        l, r = 0, len(s) - 1
        count = 0 
        while l <= r :
            diff = limit - s[l]
            if s[r] <= diff:
                count+=1
                r-=1
            elif s[r] > diff:
                count+=1
            # elif s[r] < diff:
                # temp = r
                # while s[temp] < diff:
                #     temp-=1
                # if s[temp] == diff:
                #     s.pop(temp)
                #     count+=1
                #     r = len(s) - 1
            # elif diff == 0:
                # count+=1
            l+=1
        return count
            


                
