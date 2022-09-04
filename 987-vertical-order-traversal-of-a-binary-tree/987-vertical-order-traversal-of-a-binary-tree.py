class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = {}
        def traverse(node, row, col):
            if col not in columns: columns[col] = {}
            if row not in columns[col]: columns[col][row] = []
            columns[col][row].append(node.val)
            if node.left: traverse(node.left, row + 1, col - 1)
            if node.right: traverse(node.right, row + 1, col + 1)
        traverse(root, 0, 0)
        
        sorted_columns = sorted(list(columns.keys()))
        output = []
        for column in sorted_columns:
            nodes = []
            sorted_row = sorted(list(columns[column].keys()))
            for row in sorted_row:
                columns[column][row].sort()
                nodes.extend(columns[column][row])
            output.append(nodes)
        return output