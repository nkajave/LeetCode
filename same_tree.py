class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ---------- Helper function to build tree ----------

def build_tree(values):
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
    raw1 = input("Enter Tree 1 (level order, use null): ")
    raw2 = input("Enter Tree 2 (level order, use null): ")

    vals1 = [None if x.lower() == "null" else int(x) for x in raw1.split()]
    vals2 = [None if x.lower() == "null" else int(x) for x in raw2.split()]

    tree1 = build_tree(vals1)
    tree2 = build_tree(vals2)

    sol = Solution()
    result = sol.isSameTree(tree1, tree2)

    print("Result:", result)

"""
to run : python same_tree.py
git status
git add same_tree.py
git commit -m "checking if tree are same or not"
git push
"""