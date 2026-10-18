"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # one variable
    category = "Parent"
    #constructor with two instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    category = "Child"

    def __init__(self, name, age, colors, grade):
        super().__init__(name, age)

        self.colors = colors
        self.grade = grade
    #method
    def display_colors(self):
        return f"Hobbies: {self.colors}"

    #override method
    def display_info(self):
        return (f"Name: {self.name}, Age: {self.age}, Favorite colors: {self.colors}, Grade: {self.grade}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # two objects
    child1 = ChildClass("DJ", 16, ["Pink", "Blue"], "A")
    child2 = ChildClass("San", 15, ["Yellow", "Purple", "Red"], "C")
    child3 = ChildClass("Laye", 10, [], "B")

    #Class varible
    print("Category: ", ChildClass.category)
    # access same variable through object
    print("Child 1 category: ", child1.category)
    # add new attribute
    child1.height = "5'5"
    #display
    print()
    print("Child1 namespace: ")
    print(child1.__dict__)

    print()
    print("Child2 namespace: ")
    print(child2.__dict__)

#test
    print()
    print("Child3 namespace: ")
    print(child3.__dict__)

    print()
    print("ChildClass namespace: ")
    print(ChildClass.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    #object with nested mutable data
    original = {"name": "DJ", "scores": [95, 90, 98]}

    #shallow copy
    shallow_copy = copy(original)

    #deep copy
    deep_copy = deepcopy(original)

    #modify original
    original["scores"].append(100)

    #display all
    print("\nOriginal: ", original)
    print("\nShallow copy: ", shallow_copy)
    print("\nDeep copy: ", deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print()
    print("Parent:")
    parent = ParentClass("Lucy", 40)
    print(parent.display_info())
    print("Category:", parent.category)

    print("\nChild:")
    child = ChildClass ("Psylocke", 17, ["Pink", "Mauve"], "A")
    print(child.display_info())
    print(child.display_colors())
    print("Category: ", child.category)


    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()