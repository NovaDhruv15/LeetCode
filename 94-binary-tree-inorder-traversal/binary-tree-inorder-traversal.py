
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def solve(node):
            if node is None:
                return

            solve(node.left)
            ans.append(node.val)
            solve(node.right)

        solve(root)
        return ans
