from dao.student_dao_impl import StudentDAOImpl

class StudentService:

    def __init__(self, dao):
        self.dao = dao

    def create_student(self, student):
        self.dao.create_student(student)

    def get_student(self, student_id):
        return self.dao.get_student(student_id)

    def update_student(self, student_id, student):
        self.dao.update_student(student_id, student)

    def delete_student(self, student_id):
        self.dao.delete_student(student_id)

    def list_students(self):
        return self.dao.list_students()
