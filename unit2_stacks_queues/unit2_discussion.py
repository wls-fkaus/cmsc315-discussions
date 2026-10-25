"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        
        # When you add to the top it means that the newest value is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        
        # If the stack is empty then we want to return None
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        
        # Peek will return the top value without removing it
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        
        # Add to the back so the oldest value is removed
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        
        # If queue is empty then return None
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        
        # Return front value without removing
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")

stack = Stack()
print("Adding 4 values to stack: ")
for value in [10, 20, 30, 40]:
    stack.push(value)
    print("Pushed:", value)

print("Top value using peek(): ", stack.peek())
print("\nRemoving values to show an example of LIFO:")

while not stack.is_empty():
    print("Popped: ", stack.pop())

print("True or False, is the stack empty? ", stack.is_empty())

print("      test popping from an empty stack, (removing values)")
print("      ", stack.pop())

print("      test peeking at an empty stack, (show top value)")
print("      ", stack.peek())

print("      and verify a single-item stack becomes empty after removal.")

stack_single = Stack()
stack_single.push(100)
print("\nSingle-item stack was created with:", stack_single.peek())
print("Removed the single item:", stack_single.pop())
print("True or False, is the single-item stack empty?", stack_single.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
# TODO: Create a Queue object, demonstrate FIFO behavior

queue = Queue()

print("Add four values to queue:")
for value in [10, 20, 30 , 40]:
    queue.enqueue(value)
    print("Enqueued:", value)

print("Front value using front():", queue.front())
print("\nRemove values to demonstrate FIFO behavior")
while not queue.is_empty():
    print("Dequeued:", queue.dequeue())

print("True or False, is the queue empty?", queue.is_empty)

print("      test dequeuing from an empty queue, ()")
print("      ", queue.dequeue())

print("      test viewing the front of an empty queue, ()")
print("      ", queue.front())

print("      and verify a single-item queue becomes empty after removal.")

queue_single = Queue()
queue_single.enqueue(100)
print("\nSingle-item queue has the single value with:", queue_single.front())
print("Removed the single item:", queue_single.dequeue())
print("True or False, is the single-item queue empty?", queue_single.is_empty())

if __name__ == "__main__":
    main()
