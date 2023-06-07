class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return None
        res = []
        path = collections.deque() 
        
        def dfs(node, s):
            path.append(node.val)
            s += node.val
            if  not node.left and not node.right and s == targetSum:
                res.append(list(path))
			if node.left:
                dfs(node.left, s)
            if  node.right:
                dfs(node.right, s)
            s -= node.val
            path.pop()
		dfs(root, 0)
        return res
