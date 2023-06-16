class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        mp = {}
        def comb(n, k):
            if n == 1 and k == 1:
                mp[(1, 1)] = [[1]]  
                return [[1]]
            if (n, k) in mp:
                return mp[(n, k)]  
            ans = []
            if k == 1:
                ans = [[x] for x in range(1, n + 1)]  
            elif n == k:
                ans = [list(range(1, n + 1))]  
            else:
                ans = comb(n - 1, k)  
                c_wo_n = comb(n - 1, k - 1)  
                for v in c_wo_n:
                    v_w_n = v + [n]  
                    ans.append(v_w_n)  
            mp[(n, k)] = ans  
            return ans
        return comb(n, k)
