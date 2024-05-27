from dao.teacher_dao_impl import TeacherDAOImpl

class TeacherService:

    def __init__(self, dao):
        self.dao = dao

    def create_teacher(self, teacher):
        self.dao.create_teacher(teacher)

    def get_teacher(self, teacher_id):
        return self.dao.get_teacher(teacher_id)

    def update_teacher(self, teacher_id, teacher):
        self.dao.update_teacher(teacher_id, teacher)

    def delete_teacher(self, teacher_id):
        self.dao.delete_teacher(teacher_id)

    def list_teachers(self):
        return self.dao.list_teachers()
