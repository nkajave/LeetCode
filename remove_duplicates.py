class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# Helper functions
def build_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted numbers: ").split()))
    
    head = build_list(nums)

    sol = Solution()
    new_head = sol.deleteDuplicates(head)

    print("After removing duplicates:")
    print_list(new_head)


"""
to run: python remove_duplicates.py

git status
git add remove_duplicates.py
git commit -m "Remove Duplicates from Sorted List"
git push

"""
