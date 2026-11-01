# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

Implmentation document:
First I used the built-in Python insert() method to add a value to a specific index for the insert_at() function. 

In the delete_at() function, I put a if loop to with the condition that is the index given for the list is less than 0 OR the index given is more than or equal to the length of the list it would return “None” meaning it would return “None if the index given for this function was invalid. If the index is valid then I saved the value removed in a “removed_value” variable to return after.

In the search_value() function I used a for loop to search for the value given in each index in the list given and if the value matched the value in the index the loop was on, then it would return that index. If the value could not be found then we would just return “-1”

In the main() function I called from the insert_at() function to try inserting a random value from the beginning, middle, and end. After each insert I printed the list everytime to show the list being updated everytime. 
Then I deleted a value from the start of the list and then the middle and lastly the end of the list while also showing the list after each delete to show the list being updated again using the detele_at() function.

Then I used the search_value() function to search for a value in the list and a value that does not exist in the list. I used an if loop to check if the value given was a negative number or not as well. If the value could not be found or was invalid then it returned the sentence “was not found” instead.

For the edge cases I tried to remove a invalid index using delete_at()function which gave back “None”
I searched for a value that wasn’t in the list using search_value() function which gave back “-1”
I inserted a random value into an empty list using insert_at() function into a newly created empty list. This gave back the list with the newly inserted value.
I deleted a random value from a another newly made empty list using delete_at() function which just gave back “None”
