# 1. Python List Transformation
# Objective:
# The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement:
# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.
grades.sort(reverse=True)
print(grades)
average = 0
for grade in grades:
    average += grade

average /= len(grades)

print(average)

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

print(grades)


# Task 2: Calculate the average grade and display it.

# Task 3: Replace any grade below 80 with the value Failed.

# 2. Advanced List Methods and Identity Operators
# Objective:
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
sub_and_att = list(set(submitted) & set(attended))
# Find out which students both submitted their assignments and attended the class.

print(sub_and_att)

identical_list = set(submitted) == set(attended)
print(submitted in attended)
# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

# 3. Advanced Slicing Techniques
# Objective:
# The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement:
# You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures for the second week (7 days) of the month.

second_week = temperatures[7:14]
print(second_week)

# Task 2: Extract all the temperatures above 100.

above_hundred = temperatures[(temperatures.index(100) + 1):]
print(above_hundred)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
reverse_list = temperatures
days_5to10 = reverse_list[4:10]
print(days_5to10)

# 4. List Comprehensions and Membership Operators
# Objective:
# The aim of this assignment is to practice using list comprehensions and membership operators in Python.

# Problem Statement:
# You have a list of numbers, and you'd like to generate a new list based on certain conditions.

# Task 1: Given the list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a list comprehension to create a new list containing only even numbers.

even_numbers_list = [number for number in numbers if number % 2 == 0]
print(even_numbers_list)

# Task 2: Use a list comprehension to create a new list containing numbers greater than 5.

numbers_greater_than_5 = numbers[numbers.index(5) + 1:]
print(numbers_greater_than_5)

# Task 3: Check if the number 7 is in the original numbers list.

number7_in_list = 7 in numbers
print(number7_in_list)

# 5. Deep Dive into Python Lists
# Objective:
# The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Create a new list where each element is a dictionary with keys name, grade, and activity and the corresponding values from the provided lists.

min_length = min(len(students), len(grades), len(activities))
student_info = [{"name": students[i], "grade": grades[i], "activity": activities[i]} 
                for i in range(min_length)]
print(student_info)

# Task 2: Filter out students who have grades below 80.

filtered_student_list =[{"name": students[i], "grade": grades[i], "activity": activities[i]}
                        for i in range(len(students)) if grades[i] >= 80]
print(filtered_student_list)

# Task 3: For the remaining students, add a new key-value pair in their dictionary: "status": "Passed".

passed_student_list = [{"name": students[i], "grade": grades[i], "activity": activities[i], "status":"passed"}
                       for i in range(len(student_info))]
print(passed_student_list)
