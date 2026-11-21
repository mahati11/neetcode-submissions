class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0 
        l = 1
        r = x
        mid = (r+l)//2
        temp = 1
        while l < r :
            temp = mid*mid
            if temp == x :
                return mid
            if temp > x:
                r = mid - 1
            if temp < x:
                if (mid+1)*(mid+1) > x:
                    return mid
                l = mid +1

            mid = (r+l)//2

        return mid