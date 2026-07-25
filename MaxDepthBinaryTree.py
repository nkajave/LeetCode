# MaxDepthBinaryTree.py

"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2 

Constraints:
1. The number of nodes in the tree is in the range [0, 104].
2. -100 <= Node.val <= 100

"""
from collections import deque


# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):

        # Base case
        if root is None:
            return 0

        # Find depth of left subtree
        leftDepth = self.maxDepth(root.left)

        # Find depth of right subtree
        rightDepth = self.maxDepth(root.right)

        # Return current node depth
        return 1 + max(leftDepth, rightDepth)


# Function to build tree from level-order input
def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] != "null":
            current.left = TreeNode(int(values[i]))
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != "null":
            current.right = TreeNode(int(values[i]))
            queue.append(current.right)
        i += 1

    return root


# User Input
values = input("Enter tree in level order (use 'null' for empty nodes): ").split()

root = buildTree(values)

solution = Solution()
print("Maximum Depth:", solution.maxDepth(root))