class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(nums,temp):
            if len(nums) == 0:
                ans.append(temp)
                return
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:],temp+[nums[i]]) 
        helper(nums,[])
        return set(tuple(ele) for ele in ans) 
        
