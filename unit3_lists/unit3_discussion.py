"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # The insert method adds a new value at the specified index
    #  Inserting in the beginning will shift every existing value to the right
    # Insert in the middle will shift as well but starting fromt he middle
    # Insert at the end will shift no value

    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # index vsalidation will prevetn a index error whent he requested position doesn't exist
    # safe deletion is important to preent the program from crashing from invalid index

    if index < 0 or index >= len(lst):
        return None

    #removed value saved
    removed_value = lst.pop(index)

    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # linear seach checks one elemnt at a time  and the for loop will do that here
    # The loop will scan each value until it finds the value needed starting from the index given usually (0, the start)

    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return if not found
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.


    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    numbers = [1, 2, 3, 4, 5]

    print("Original:", numbers)

    #insert in the beginning
    numbers.insert(0, 6)
    print("After inserting in the beginning:", numbers)
    #insert in the middle
    numbers.insert(3, 10)
    print("After inserting in the middle:", numbers)
    #insert in the end
    numbers.insert(len(numbers), 100)
    print("After inserting in the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.  
    

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    
    #delete from beginning
    removed = delete_at(numbers, 0)
    print("Delete from beginning:", removed)
    print("Updated list:", numbers)
    #delete from middle
    removed = delete_at(numbers, 2)
    print("Delete from middle:", removed)
    print("Updated list:", numbers)
    #delete from end
    removed = delete_at(numbers, len(numbers) - 1)
    print("Delete from end:", removed)
    print("Updated list:", numbers)  

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    #search for exisitng value
    result = search_value(numbers, 3)

    if result != -1:
        print("Value 3 was found at the index:", result)
    else:
        print("Value 3 was not found")

    #search for nonexisting value
    result = search_value(numbers, 10)

    if result != -1:
            print("Value 10 was found at the index:", result)
    else:
            print("Value 10 was not found")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    #delete using an invalid index
    removed = delete_at(numbers, 100)
    print("Deleting invalid index:", removed)

    #Search for a missing value
    result = search_value(numbers, 109)
    print("Searching for a missing value:", result)

    #Insert into a empty list
    empty_list1 = []
    print("Empty list before modfying:", empty_list1)

    insert_at(empty_list1, 1, 67)
    print("Empty list after inserting in the beginning:", empty_list1)

    #Delete from empty list
    empty_list2 = []
    removed = delete_at(empty_list2, 0)
    print("Deleting from an empty list:", removed)





if __name__ == "__main__":
    main()