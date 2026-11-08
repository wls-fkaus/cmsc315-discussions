"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # if empty position then create new
        if node is None:
            return Node(value)

        # smaller values would go left because the BST usually keeps them on the left.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values will go on the right because BSt usally keeps them ont he right side
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        #duplicates ignore
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST seach is more efficient because it's faster and can eliminate parts of the tree after checking every node
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if node.value == value:
            return True

        # Search left if ID is smaller, if not search right
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            #visit left subtree
            self._inorder_recursive(node.left, values)

            #visit current node
            values.append(node.value)

            #visit right subtree
            self._inorder_recursive(node.right, values)

            #this produces sorted output because the smaller IDs are on the left and the larger ones are on the right



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.
    print("Cat Adoption Center System")

    cat_tree = BST()

    cat_ids = [50, 30, 70, 20, 40, 60, 80]

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    for cat_id in cat_ids:
        cat_tree.insert(cat_id)
        print("Inserted cat adoption ID:", cat_id)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.


    #This will reorganize the list from smallest to largest

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    print("Cat adoption IDs in order")
    print(cat_tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.


    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    print("Searching for ID 30:", cat_tree.search(30))
    print("Searching for ID 80:", cat_tree.search(80))

    # search for IDs that don't exist
    print("Searching for ID 25:", cat_tree.search(25))
    print("Searching for ID 78:", cat_tree.search(78))

    #The BST should follow the correct branch based on the ID

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    #Traverse an empty tree
    test = BST()
    print("Empty tree put in order:")
    print(test.inorder())
    #test searching empty tree
    print("Searching an empty tree:", test.search(10))

    #Test inserting a duplicate ID
    cat_tree.insert(50)
    print("After inserting duplicate ID 50:")
    print(cat_tree.inorder())

    #duplicate is ignored, so the tree doesn't have two nodes with the same ID



if __name__ == "__main__":
    main()