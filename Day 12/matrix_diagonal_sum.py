class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        # Sum of primary diagonal
        for i in range(n):
            total_sum += mat[i][i]
            
        # Sum of secondary diagonal (excluding elements on primary diagonal)
        for i in range(n):
            j = n - 1 - i
            if i != j:
                total_sum += mat[i][j]
                
        return total_sum
