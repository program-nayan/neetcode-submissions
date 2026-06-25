from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = (ROWS * COLS) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // COLS][mid % COLS]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False