
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

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
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False


class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and slow and fast.next:
            fast, slow = head.next.next, slow.next
            if fast is slow:
                return True
        return False


if __name__=="__main__":
    print("=========================")
    start = ListNode(1)
    cur = start
    for i in range(10):
        cur.next = ListNode(i+2)
        cur = cur.next
    cur.next=start.next.next

    print(Solution().hasCycle(start))
    print(Solution1().hasCycle(start))
    
