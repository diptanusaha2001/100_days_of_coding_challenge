class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0 or n<1:
            return []

        dp=[[] for _ in range(n+1)]
        dp[1]=[TreeNode(0)]

        for i in range(3,n+1):
            for j in range(1,i):
                leftTree=dp[j]
                rightTree=dp[i-1-j]

                for leftSubtree in leftTree:
                    for rightSubtree in rightTree:
                        root=TreeNode(0)
                        root.left=leftSubtree
                        root.right=rightSubtree
                        dp[i].append(root)

        return dp[n]                    
