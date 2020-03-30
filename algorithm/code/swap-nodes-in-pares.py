"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            print("==========HEAD")
            head.show()
            print("NEW")
            if new_head:
                new_head.show()
            
            if head.next:
                if not new_head:
                    new_head=head.next
                # head_next=head.next.next
                # head.next.next=head
                # head.next=head_next.next if head_next and head_next.next else head_next
                # head=head_next
                head.next.next,head.next,head=head,head.next.next.next if head.next.next and head.next.next.next else head.next.next ,head.next.next
            else:
                if not new_head:
                    new_head=head
                head=None
        return new_head

    
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        p_a,p_a.next=self,head
        while p_a.next and p_a.next.next:
            p_b=p_a.next
            p_c=p_b.next
            # p_d=p_c.next
            # p_a.next=p_c
            # p_c.next=p_b
            # p_b.next=p_d
            # p_a=p_b

            p_a.next,p_c.next,p_b.next,p_a=p_c,p_b,p_c.next,p_b


            
        return self.next
            
            
    
if __name__=="__main__":
    print("=========================")
    start = ListNode(1)
    cur = start
    for i in range(10):
        cur.next=ListNode(i+2)
        cur = cur.next
    print("Original:")
    start.show()
    print("Result:")
    # Solution().swapPairs(start).show()
    Solution1().swapPairs(start).show()
