#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printNextLevel(self, result, level, node, fromLeft):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        if len(result) - 1 < level:
            result.append([])
        if node.left is not None:
            if fromLeft:
                result[level].append(node.left.val)
            else:
                result[level].insert(0, node.left.val)
        if node.right is not None:
            if fromLeft:
                result[level].append(node.right.val)
            else:
                result[level].insert(0, node.right.val)

        self.printNextLevel(result, level + 1, node.left, not fromLeft)
        self.printNextLevel(result, level + 1, node.right, not fromLeft)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        result = [[root.val]]
        self.printNextLevel(result, 1, root, False)
        return result
# @lc code=end
