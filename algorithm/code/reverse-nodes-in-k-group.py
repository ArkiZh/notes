"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k <= 1:
            return head
        # start
        pre = self
        pre.next = head
        # loop
        while True:
            start = pre.next
            end = start
            # check k group
            for i in range(k-1):
                if not end:
                    return self.next
                end = end.next
            if not end:
                return self.next

            # do reversion
            pre.next = end
            pre = start
            next_group = end.next

            a, b = start, start.next
            for i in range(k-1):
                temp = b.next
                b.next = a
                a = b
                b = temp

            pre.next = next_group

if __name__=="__main__":
    print("=========================")
    start = ListNode(1)
    cur = start
    for i in range(4):
        cur.next=ListNode(i+2)
        cur = cur.next
    print("Original list:")
    start.show()

    print("Result:")
    
    Solution().reverseKGroup(start,6).show()
    # Solution1().reverseList(start).show()
    # Solution2().reverseList(start).show()
    # Solution3().reverseList(start).show()
    # Solution4().reverseList(start).show()

        
