"""
232. Implement Queue using Stacks

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
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
