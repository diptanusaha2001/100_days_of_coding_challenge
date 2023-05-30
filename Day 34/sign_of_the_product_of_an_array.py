class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for n in nums:
            if not n:
                return n
            if n < 0:
                result = -result
        return result
