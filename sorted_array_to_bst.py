from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


# Convert tree to LeetCode-style list output
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing nulls
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array: ").split()))

    sol = Solution()
    root = sol.sortedArrayToBST(nums)

    output = tree_to_list(root)
    print("Output:", output)


"""
to run file: python sorted_array_to_bst.py
enter numbers


"""