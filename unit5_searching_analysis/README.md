# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

The Linear search method will search through a list checking each element one by one using the If loop from the beggining if it finds the ID it's looking for then the method will return it's index. If it cannot find the number then it returns -1 
The Binary search method will search through a sorted list by checking the middle element first. It uses a while loop and if the target ID is greater than the middle then it'll search the right half of it and if the number is smaller than it'll search the left half. It'll also return -1 if the element does not exist too

For the edge tests I decided to create one empty library and a library with one book and try testing to see what will happen if I searched for a book that does not exist as well. They all give the expected results and I simply just had to create different lists according to each test and call for each method (binary, linear search)