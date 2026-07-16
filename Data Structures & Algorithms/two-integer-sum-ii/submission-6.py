class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left  = 0 
        right = 1
      
        while right < n:
            temp = target - numbers[left]
            
            while  right< n and numbers[right] <= temp :
                if numbers[right] == temp:
                    return [left+1, right+1]
                right +=1
               
            left +=1 
            right = left+1