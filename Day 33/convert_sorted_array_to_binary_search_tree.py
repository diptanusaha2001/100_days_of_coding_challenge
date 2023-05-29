class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recur(0, len(nums)-1, nums)

    def recur(self, s, e, nums: List[int]) -> TreeNode:
        if(s > e):
            return None
        mid = int(s + (e-s)/2)
        root = TreeNode(nums[mid])
        root.left = self.recur(s, mid - 1, nums)
        root.right = self.recur(mid + 1, e, nums)
        return root
