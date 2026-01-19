class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result


# ---------- Helper functions ----------

def build_tree(values):
    """
    Build binary tree from level-order list.
    Example: [1, None, 2, 3]
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    raw = input("Enter tree in level order (use null for empty): ")

    values = []
    for x in raw.split():
        if x.lower() == "null":
            values.append(None)
        else:
            values.append(int(x))

    root = build_tree(values)

    sol = Solution()
    result = sol.inorderTraversal(root)

    print("Inorder Traversal Output:", result)



"""
to run: python BinaryTreeInorderTraversal.py
git status
git add BinaryTreeInorderTraversal.py
git commit -m "Binary Tree Inorder Traversal"
git push

"""
