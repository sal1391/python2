#Carlos Salgado
# Student ID:5001363
# date: 6/01/2026
# Description: This program defines a Student class to manage student information and status. It includes a function to change the status of a student object and demonstrates the creation of student objects, updating their statuses, and printing a summary of the students and the total count. The program also includes reflection questions to evaluate the development process.    

# changes the status of a student object
def change_status(student_obj,new_status):
    student_obj.status = new_status

# Defines the Student class with attributes and methods to manage student information and status
class Student:
    total_students = 0
    # Initializes a Student object with a name and status, and increments the total student count
    def __init__(self, name,status):
        self.name = name
        self.status = status
        Student.increment_count()
    # Updates the status of the student object to the new status provided
    def update_status(self,new_status):
        self.status = new_status
    # Class method to increment the total student count whenever a new student is created
    @classmethod
    def increment_count(cls):
        cls.total_students += 1
 
# Create student objects
s1 = Student("Alice","Active")
s2 =Student("Bob","Present")
s3 = Student("Charlie","Active")
s4 = Student("David","Present")

# change the status
change_status(s1,"Tardy")
change_status(s3,"Present")

#update the status of s1 to "Absent"
s1.update_status("Absent")
s4.update_status("Tardy")

# print the summary of students and total count
print("--------------Summary----------------")
print(f"Student: {s1.name}, Status: {s1.status}")
print(f"Student: {s2.name}, Status: {s2.status}")
print(f"Student: {s3.name}, Status: {s3.status}")
print(f"Student: {s4.name}, Status: {s4.status}")
print(f"Total students created: {Student.total_students}")


# --- Reflection ---

# 1. What does it mean that Python objects are mutable?
""" Python objects being mutable means that they can be changed after they have been created."""

# 2. Why is an instance method useful for updating one student's data?
""" An instance method is useful for updating one student's data because it allows us to modify the attributes of a specific student object directly. """

# 3. Why do class methods use cls instead of self?
""" Class methods use cls instead of self because they are designed to operate on the class itself rather than on individual instances of the class. The cls parameter refers to the class, allowing the method to access and modify class-level attributes, such as total_students in this case."""


# 4. What is the purpose of having a class variable like total_students?
""" The purpose of having a class variable like total_students is to keep track of the total number of student instances that have been created."""

#Generate AI code and compare without copying.

# 5. Difference from AI
""" AI's code had more functions for printing student information and counting students, while my code focused on the core functionality of managing student status and counting total students. AI's code also included more comments and a different structure for the Student class."""
# 6. AI strength
""" AI's strenght was that there was less lines of code and it was more concise. """
# 8. What you don’t understand?
""" I undestand the code just dont see how this storing this information on memory is diffrent then storying in a database"""
# 9. Which version is better?
"""The AI's easiesr to read"""