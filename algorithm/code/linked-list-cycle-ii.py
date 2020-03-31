"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def show(self):
        if self.next is not None:
            print(self.val,end="->")
            self.next.show()
        else:
            print(self.val,"NULL",sep="->")


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            # print(head.val)
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next and slow:
            # print(fast.val,slow.val)
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                # print("===")
                start = head
                while start:
                    if start is slow:  # This check should be done first, in case the cycle begins at position 0.
                        return start
                    start = start.next
                    slow = slow.next
        return None


if __name__ =="__main__":
    print("=========================")
    start = ListNode(1)
    cur = start
    for i in range(10):
        cur.next = ListNode(i+2)
        cur = cur.next
    cur.next = start.next.next

    # print(Solution().detectCycle(start).val)
    print(Solution1().detectCycle(start).val)
