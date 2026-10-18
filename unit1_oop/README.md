# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

Implementation documentation:

First I have the parent class where I made a class varible called category where it tells whether this object will be a parent or a child. I also have two instance varibles which represent the name and age. Constructor will initialize and the display_info() will output the general information of the object.

Second I have the child class where I added the category variable and two new instance variable which represent a kids grade and favorite colors. I call the parent class constructor for the name and age using the super() function. I also have two methods where we display different information about the child object.

In the namespace demonstration I created three objects. It accesses the class variable through the class and an object. I also aded a new attribute for the first child and displayed the instance namespaces using _dict_. I also added a extra child, the 3rd one is going to serve as a test if we left the colors blank to see how the program would react to this change. The output simply gave us the information for this child and left the colors blank.

In the copy demonstration, we have a original dictionary with a nested list and modified by adding an extra score (100). I then display the original then both copies made to show how the shallow copy can share nested mutable data with the original while the deep copy will show its own separate nested data.

Last, in the main() function it will create the objects of ParentClass and of ChildClass. Where it calls their methods to show inheritance and method overriding. I also called the namespace and copying demonstration functions to print those out as well. 

Overall, object-oriented programming can help by keeping all information organized and seperating where you want general common information and where you would like more specialized features such as my child class. Namespaces allows you to keep track of different attributes for different objects and when using shallow and deep copying,  you can duplicate data while choosing if you would like to share nested objects as well. 