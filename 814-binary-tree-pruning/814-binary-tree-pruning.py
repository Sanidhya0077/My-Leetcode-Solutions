class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        root.left = left
        root.right = right
        
        if not root.left and not root.right:
            if root.val == 1:
                return root
            if root.val == 0:
                return None
        
        return root