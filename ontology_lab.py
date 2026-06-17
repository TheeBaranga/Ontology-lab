# ------------------------------------------
# PART A: Define Ontology Classes
# ------------------------------------------
class Student:
    def __init__(self, student_id, name, programme, year):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.year = year

class Lecturer:
    def __init__(self, lecturer_id, name, department):
        self.lecturer_id = lecturer_id
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_code, title, credits):
        self.course_code = course_code
        self.title = title
        self.credits = credits

class Department:
    def __init__(self, dept_code, name):
        self.dept_code = dept_code
        self.name = name

class Classroom:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity


# ------------------------------------------
# PART B: Create Ontology Objects
# ------------------------------------------
# Students
student1 = Student("S001", "Mary", "Applied Computer Technology", 2)
student2 = Student("S002", "Brian", "Software Engineering", 2)
student3 = Student("S003", "Linda", "Information Systems Technology", 3)
student4 = Student("S004", "Kalvin", "Applied Computer Technology", 3)
student5 = Student("S005", "Ryan", "Software Engineering", 2)

# Lecturers
lecturer1 = Lecturer("L01", "Dr. Otieno", "Computer Science")
lecturer2 = Lecturer("L02", "Prof. Simwa", "Applied Sciences")
lecturer3 = Lecturer("L03", "Dr. Jane", "Information Systems")

# Courses
course1 = Course("APT3020", "Knowledge Based Systems", 3)
course2 = Course("IST4040", "Systems Analysis", 3)
course3 = Course("APT4040", "Advanced Artificial Intelligence", 3)
course4 = Course("CMS3700", "Community Service", 3)
course5 = Course("MTH1010", "Calculus I", 3)

# Departments
dept1 = Department("D01", "Computer Science")
dept2 = Department("D02", "Applied Sciences")
dept3 = Department("D03", "Software Engineering")
dept4 = Department("D04", "Information Systems Technology")
# Classrooms
room1 = Classroom("Science 101", 40)
room2 = Classroom("Science 102", 50)
room3 = Classroom("Auditorium", 150)


# ------------------------------------------
# PART C: Create Relationships (Knowledge Base)
# ------------------------------------------
# Relationship: A student is enrolled in a course (Current Semester)
enrollments = {
    "Mary": ["APT3020", "IST4040"],
    "Brian": ["APT3020", "MTH1010"],
    "Linda": ["APT3020", "CMS3700"],
    "Kalvin": ["APT3020", "CMS3700"],
    "Ryan": ["IST4040"]
}

# Relationship: Completed courses (Used for prerequisite reasoning)
completed_courses = {
    "Mary": ["IST2020"], 
    "Brian": ["APT3020"],
    "Kalvin": ["APT3020"]
}

# Relationship: A lecturer teaches a course
teaching_assignments = {
    "APT3020": "Dr. Otieno",
    "IST4040": "Prof. Simwa",
    "APT4040": "Dr. Otieno",
    "CMS3700": "Dr. Jane"
}

# Relationship: A course belongs to a department
department_courses = {
    "Software Engineering": ["APT3020", "IST4040", "APT4040", "CMS3700"],
    "Applied Sciences": ["MTH1010"]
}

# Relationship: A course has a prerequisite
prerequisites = {
    "APT4040": "APT3020",
    "IST4040": None,
    "APT3020": None
}

# Relationship: A course is taught in a classroom
course_classrooms = {
    "APT3020": "Science 101",
    "IST4040": "Science 102",
    "CMS3700": "Auditorium"
}


# ------------------------------------------
# PART D: Add Reasoning Functions
# ------------------------------------------
def get_student_courses(student_name):
    return enrollments.get(student_name, [])

def get_course_lecturer(course_code):
    return teaching_assignments.get(course_code, "Unassigned")

def get_department_courses(dept_name):
    return department_courses.get(dept_name, [])

def get_students_in_course(course_code):
    students = []
    for student, courses in enrollments.items():
        if course_code in courses:
            students.append(student)
    return students

def can_take_course(student_name, course_code):
    prereq = prerequisites.get(course_code)
    
    # If there is no prerequisite, they can take it
    if not prereq:
        return True, None
    
    # Check if the student has completed the prerequisite
    student_completed = completed_courses.get(student_name, [])
    if prereq in student_completed:
        return True, None
    else:
        return False, prereq


# ------------------------------------------
# 6. Minimum Expected Output Execution
# ------------------------------------------
if __name__ == "__main__":
    print("Courses taken by Mary:")
    for course in get_student_courses("Mary"):
        print(f"- {course}")
    print()

    print("Lecturer teaching APT3020:")
    print(f"- {get_course_lecturer('APT3020')}")
    print()

    print("Courses in Software Engineering Department:")
    for course in get_department_courses("Software Engineering"):
        print(f"- {course}")
    print()

    print("Students taking APT3020:")
    for student in get_students_in_course("APT3020"):
        print(f"- {student}")
    print()

    print("Can Mary take APT4040?")
    can_take, missing_prereq = can_take_course("Mary", "APT4040")
    if can_take:
        print("Yes.")
    else:
        print(f"No. Missing prerequisite: {missing_prereq}")