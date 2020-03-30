
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
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
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        self.recursive(head)
        return self.new_head


    
    def recursive(self, current: ListNode) -> ListNode:
        if current.next is None:
            self.new_head = ListNode(current.val)
            return self.new_head
        temp = self.recursive(current.next)
        next=ListNode(current.val)
        temp.next=next
        # print("Return",end=" ")
        # temp.show()
        return next
    


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        self.old_head=head
        self.recursive(head)
        
        return self.new_head

    def recursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            self.new_head=head
            self.old_head.next=None
            return head
        cur = self.recursive(head.next)
        cur.next=head
        return head


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return cur


class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head=None
        while head is not None:
            temp=head.next
            head.next=new_head
            new_head=head
            head=temp

        return new_head


class Solution4:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,prev=head,None
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        return prev
    
        
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
    
    # Solution().reverseList(start).show()
    # Solution1().reverseList(start).show()
    # Solution2().reverseList(start).show()
    # Solution3().reverseList(start).show()
    Solution4().reverseList(start).show()

        
