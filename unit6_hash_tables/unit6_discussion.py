"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    student_courses = {}
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.



    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    #Python uses hashing to know where keys are stored which helps values to be retrieved correctly
    student_courses["1001"] = "Computer Science"
    student_courses["1002"] = "Cybersecurity"
    student_courses["1003"] = "Mathematics"
    student_courses["1004"] = "Data Structures"
    student_courses["1005"] = "Programming"
    # 4. Display the contents of the dictionary.
    print("\nDictionary Contents:")
    print(student_courses)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    #Python hashes the key to locate the corresponding value
    print('Student 1001 is studying:', student_courses["1001"])
    print('Student 1004 is studying:', student_courses["1004"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before update:")
    print(student_courses)

    #Assign a new value to existing key replacing old value
    student_courses["1002"] = "Network Security"
    print("After update:")
    print(student_courses)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Before deleting:")
    print(student_courses)

    #Del statement remove only the selected key and value
    del student_courses["1003"]
    print("After deleting:")
    print(student_courses)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    #1: Look for a nonexisitng value
    missing_course = student_courses.get("1006")
    print("Looking up student 1006:", missing_course)

    #2: Deleting a key that doesn't exist
    removed_course = student_courses.pop("1007", "Student not found")
    print("Deleting student 1007:", removed_course)


if __name__ == "__main__":
    main()