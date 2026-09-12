class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if target > matrix[i][cols-1]:
                continue
            elif target == matrix[i][cols-1]:
                return True
            else:
                left = 0
                right = cols -1
                mid = cols//2
                while left <= right and mid < cols:
                    if target < matrix[i][mid] :
                        right = mid - 1
                    elif target > matrix[i][mid]:
                        left = mid + 1
                    else:
                        return True
                    mid = left + (right-left//2)
        return False




