# Student Record Manager Project
# This creates a dictionary and the function to add student data
student_records = {}
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")

# This adds the grades to the student in the dictionary record
def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

# This adds a function to check what courses the student is enrolled in. 
def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False

# This adds a function to calculate the grade averages of the students. 
def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        if student_records[name]["grades"] == None:
            return 0 
        else:
            result1 = 0
            result2 = 0
            result3 = 0
            for each_course in student_records[name]["grades"]:
                result1 += 1
            for each_grade in student_records[name]["grades"]:
                result2 += each_grade
            result3 = result2 / result1
            return result3  


# This is the example and test dataset.
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])

add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)

print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again
