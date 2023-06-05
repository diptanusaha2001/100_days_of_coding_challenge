class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(l):
                res.append(path[:]) 
                return

            for i, letter in enumerate(l):
                if used[i]:
                    continue
    
                path.append(letter)
                used[i] = True
                dfs(path, used, res)
                path.pop()
                used[i] = False
            
        res = []
        dfs([], [False] * len(l), res)
        return res
