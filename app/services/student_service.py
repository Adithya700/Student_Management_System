students = [] 
 
def get_all_students(): 
    return students
 
def create_student(student): 
    students.append(student) 

def get_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None    

def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return True
    return False

def update_student(student_id, data):
    for student in students:
        if student["id"] == student_id:
            student["name"] = data["name"]
            student["age"] = data["age"]
            student["course"] = data["course"]
            return student

    return None