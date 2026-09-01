class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        if min(temperatures) == max(temperatures):
            return result
        for i in range(n):
            j = i + 1
            while  j < n and temperatures[j] <= temperatures[i] :
                j += 1
            if j == n:
                result[i] = 0 
                continue
            result[i] = j-i

        return result
            


            