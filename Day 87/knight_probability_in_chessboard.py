class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        all_dir = [(-2, 1), (-1, 2), (1,2), (2,1) , (2,-1), (1,-2), (-1, -2), (-2,-1)]

        cache = {}
        
        def dp(x, y, remain):

            if (x, y, remain) in cache:
                return cache[(x, y, remain)]

            if not (0 <= x < n and 0 <= y < n):
                return 0

            
            if remain == 0:
                return 1
            
            wins = 0

            for dx, dy in all_dir:
                nx , ny = x + dx, y + dy
                wins += dp(nx, ny , remain-1)
                
            
            cache[(x, y, remain)] =  wins
            return cache[(x, y, remain)]
        
        tot_wins = dp(row, column, k)

        return tot_wins / (8**k)
