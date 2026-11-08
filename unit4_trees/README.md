# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

First I initialized a Binary Search Tree (BST). I put in seven different IDs using insert() while also inserting the values into the correct nodes depending if the value was larger than the last. Then I used the in-order traversal to display the adoption IDs it organizes from smallest to largest. It’ll visit the left subtree then to the current and lastly to the right subtree according to the value.

I tested the search method using IDs that exist and IDs that don’t exist to make sure they correctly output True and False depending if the value could be found in the BST. I used the search() method using the if loop to check and compare which direction to search and if the values match.

For edge tests I tested in-order transversal on an empty tree which returned the empty list as is. Searching also returned False. I also tried adding a duplicate ID in the cat adoption IDs and the program ignored the duplicate returning the adoption ID as it was before.
