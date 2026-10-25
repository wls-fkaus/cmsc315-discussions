# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

First, in the Stack class I created the constructor for an empty list to store values. The push() method uses the append function to add values. The pop method uses pop() function to remove and return the most recently added value. The peek() method uses a if function to check if the list is already empty to return None or the list top value without removing. The is_empty() method will just check if the list is empty or not by checking if the length of the list is zero or not.

In the Queue class, I used the deque from the collections module to store values. In the enqueue() method I used the append function to add new values into the queue. In the dequeue() method I used the if function to make sure if the queue was empty or not using the is_empty() method and return None or the value in the front. There's also a front() method where it allows you to view the first value without removing. Last there's the is_empty() method where it checks if the queue is empty or not. 

In the main class I demonstrated a stack by creating a object using the Stack class. I added four values and displayed the top value using the peek() method. I then removed the values where you can also see how the last value added is also the first value to be removed as well. I tested the pop() and pook() methods on a empty stack as well which returned None for both. Lastly I created a stack with only one value and removed it, then checked if the is_empty() method would return true or false.

Next I demonstrated a queue by creating a Queue object and added four values. I then used the front() method to show the front value and the removed the values to show how the first value added is the first one removed as well. I also tested what would happen if I tried the dequeu() and front() methods on a empty queue. The results I got was "None" and then I tried to test a single-item queue next. I added only one value to one queue and then removed it and checked if the is_empty would come back true or false after. 