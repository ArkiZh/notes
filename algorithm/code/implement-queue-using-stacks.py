"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        self.transfer()
        return self.stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        self.transfer()
        return self.stack_out[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_in) + len(self.stack_out) == 0
        

    def transfer(self):
        """
        Move elements of stack_in to stack_out.
        """
        if self.stack_out:
            return
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
for i in range(10):
    obj.push(i)
while(not obj.empty()):
    print(obj.pop())
print(obj.peek())
