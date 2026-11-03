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

# This function will list the students by course
def list_students_by_course(course):
    student_name_list = []
    for names_of_students in student_records:
        if "courses" in student_records[names_of_students]:
            if course in student_records[names_of_students]["courses"]:
                student_name_list.append(names_of_students)
    return student_name_list    

# This is the example and test dataset.
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])

print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
