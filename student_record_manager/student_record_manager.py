# Student Record Manager Project
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

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])

print(student_records)
