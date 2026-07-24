# SymmetricTree.py

"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:
1. The number of nodes in the tree is in the range [1, 1000].
2. -100 <= Node.val <= 100

"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):

        def isMirror(left, right):
            # Both nodes are empty
            if left is None and right is None:
                return True

            # One node is empty
            if left is None or right is None:
                return False

            # Values are different
            if left.val != right.val:
                return False

            # Compare opposite children
            return (
                isMirror(left.left, right.right)
                and
                isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)


def buildTree(values):
    
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def main():
    print("Enter tree nodes in level-order.")
    print("Use 'null' for missing nodes.")
    print("Example: 1 2 2 3 4 4 3")

    user_input = input("Input: ").split()

    values = []
    for value in user_input:
        if value.lower() == "null":
            values.append(None)
        else:
            values.append(int(value))

    root = buildTree(values)

    solution = Solution()
    print("Output:", solution.isSymmetric(root))


if __name__ == "__main__":
    main()