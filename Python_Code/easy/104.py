'''
104 二叉树最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


value1 = TreeNode(15)
value2 = TreeNode(7)
value3 = TreeNode(20)
value3.left = value1
value3.right = value2
value4 = TreeNode(9)
value5 = TreeNode(3)
value5.left = value4
value5.right = value3

print(Solution().maxDepth(value5))

print(Solution().maxDepth(TreeNode(2)))