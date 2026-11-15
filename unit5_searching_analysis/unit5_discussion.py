"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #Linear search has O(n) time complexity because it has to check every element in the list 
    # the more there is in the list the more it has to comapre.

    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    #To search a sorted list you repeatedly divide the search space in half
    #Binary search has O(log n) time complexity  since each iteration half of the elements are eliminated.

    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # target = right half
            low = mid - 1
        else:
            #target in the left half
            high = mid -1
    return -1



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.
    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    small_books = [101, 203, 402, 504, 601,]

    #existing number
    target = 203
    print("Library Book IDs:", small_books)
    print("Searching for Book ID:", target)
    print("Linear Search Result:", linear_search(small_books, target))
    print("Binary Search Result:", binary_search(small_books, target))


    #Both should return the same results but binary will eliminate half the elements with each iteration
    #binary search checks the middle book first while linear checks one by one

    #Number does not exist
    target = 800
    print("\nSearching for Book ID:", target)
    print("Linear Search Result:", linear_search(small_books, target))
    print("Binary Search Result:", binary_search(small_books, target))

    #Should return -1

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    large_books = list(range(1001, 11001))

    # Search for the near end
    target = 10999

    print("Total Books in Library:", len(large_books))
    print("Searching for Book ID:", target)
    print("Linear Search Result:", linear_search(large_books, target))
    print("Binary Search Result:", binary_search(large_books, target))

    #Linear seach will check almost every element, 
    #Binary search eliminates half


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_library = []
    print("\nEmpty Library Test:")
    print("Linear Search:", linear_search(empty_library, 101))
    print("Binary Searc:", binary_search(empty_library, 101))

    #should return -1 for both since theres nothing 

    one_book = [250]

    print("\nLibrary with One Book Test:")
    print("Searching for Book ID 250")
    print("Linear Search:", linear_search(one_book, 250))
    print("Binary Search:", binary_search(one_book, 250))

    #both should return index 0 because there is only one book and it's the book we are searching for

    print("\nBook Not Available Test:")
    print("Searching for Book ID 999 in:", small_books)
    print("Linear Search:", linear_search(small_books, 999))
    print("Binary Search:", binary_search(small_books, 999))

    #both should return -1 since this is not a number in any list




if __name__ == "__main__":
    main()