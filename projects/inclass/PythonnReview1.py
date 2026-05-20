#Carlos Salgado
# Student ID:5001363
# date: 5/18/2026
# Description: This program allows the user to input the names and grades of a number of students, calculates the average grade for each student, and determines the corresponding letter grade based on a standard grading scale. The program also includes reflection questions to evaluate the development process.

#Function to calculate the average of list of grades
def calculate_avg(grades):
    return sum(grades) / len(grades)

#Function to determin the letter grade for the average
def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    elif avg >= 50:
        return 'F'
    
    #Dictionary to store the letter grades and their corresponding grade points
    grade_points = {}
    
#ask user for number of students
num_students = int(input("Enter the number of students: ")) 
students = {}

#Loop to get the name and grades for each student
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i+1))
    grades = []
    
    #Loop to get the 3 grades for each student
    for j in range(3):
        grade = float(input("Enter grade: "))
        grades.append(grade)
    students[name] = grades

#print the average and letter grade for each student
print("Student Grades:")

#Loop through the students dictionary and calculate the average and letter grade for each student
for name, grades in students.items():
    avg = calculate_avg(grades)
    letter_grade = get_letter_grade(avg)
    print(f"{name}: Average = {avg:.2f}, Letter Grade = {letter_grade}")

#Reflection Questions (answer as comments at the bottom of your program):

#1. Which part of your program was the easiest to write, and why?    
"""The easiest part of the program to write was the function to calculate the average of the grades. This is because it is a simple mathematical operation that can be easily implemented using the built-in sum() and len() functions in Python."""

#2. Which part was the most challenging, and how did you solve it?
"""The most challenging part of the program was the 2 for loops to get the name and grades for each student. This is because I had to make sure that the input was correctly stored in the students dictionary and that the average and letter grade were correctly calculated for each student. 
    I solved this by carefully planning out the structure of the program and testing it with different inputs to ensure that it worked correctly."""

#3. Why did you choose a list to store grades?
"""I chose a list to store the grades because its a flexible data structure that allows easy storageand retrieval of multiple grades for each student."""

#4. What is one improvement you would make if you had more time?
"""One improvement I would make if I had more time is to add error handling to the program to ensure that the user inputs valid data. 
    For example, I could add a try-except block to catch any ValueError exceptions that may occur when the user inputs a non-numeric value for the grades."""

#5. One thing the AI solution did differently than mine was:
"""The AI broke everything into separate functions like calculate_avg(),
    get_letter_grade(), get_grade(), collect_student(), summarize(), and
    print_report(). My version only had two functions and put most of the
    logic directly in the main code."""

#6. One part of my original code that I understand better now is:
"""The two nested for loops. After comparing both versions I can see that
    my loops are actually doing the same job, just without the extra safety checks.
    It helped me see that the structure I wrote was correct, just missing error handling."""

#7. One part of the AI code that I do NOT fully understand is:
"""The way it uses separate functions like collect_student() and summarize()
    to break everything into smaller pieces. I understand what each one does,
    but I'm still not fully comfortable with why you would split it up that way
    instead of just writing it all in one block like I did."""

#8. If you were debugging this program, where would you start and why?
"""I would start with the get_letter_grade() function because there is a bug
    in my version. The grade_points dictionary is indented inside the function
    but it never actually gets used or returned, so it does nothing. I would
    also check that the elif for avg >= 50 returns 'F' correctly since any
    grade below 60 should already be an F."""

#9. After comparing both solutions, which approach would you keep and why?
"""I would keep a mix of both. I would keep my simpler structure since it is
    easier to read and follow, but I would add the input validation from the
    AI version. My version breaks if the user types something wrong, and that
    is a real problem. Everything else my version does just fine."""