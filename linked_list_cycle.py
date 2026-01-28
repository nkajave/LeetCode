class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        first = head
        second = head

        while second and second.next:
            first = first.next
            second = second.next.next

            if first == second:
                return True

        return False


# ---------- Helper functions ----------

def build_linked_list(values, pos):
    """
    values: list of node values
    pos: index where tail connects (-1 for no cycle)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    nums = list(map(int, input("Enter linked list values: ").split()))
    pos = int(input("Enter cycle position (-1 for no cycle): "))

    head = build_linked_list(nums, pos)

    sol = Solution()
    result = sol.hasCycle(head)

    print(result)


"""
to run: python linked_list_cycle.py

git status
git add linked_list_cycle.py
git commit -m 'Linked List Cycle'
git push
"""