class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.targetSum, self.ans = targetSum, []           
        self.get_path_sum(root, 0, [])                      
        return self.ans                                     
        
    def get_path_sum(self, root, psum, path):
        if not root: return None                           
        if not root.left and not root.right:                
            if root.val + psum == self.targetSum:           
                path.append(root.val)                       
                self.ans.append([e for e in path])          
                path.pop(-1)                                
                return;                                     
        path.append(root.val)                               
        self.get_path_sum(root.left, psum + root.val, path) 
        self.get_path_sum(root.right, psum + root.val, path)
        path.pop(-1)                                        
