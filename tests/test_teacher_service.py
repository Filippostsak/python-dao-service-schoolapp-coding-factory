import unittest
from unittest.mock import MagicMock
from service.teacher_service import TeacherService

class TestTeacherService(unittest.TestCase):

    def setUp(self):
        self.dao = MagicMock()
        self.service = TeacherService(self.dao)

    def tearDown(self):
        del self.service

    def test_create_teacher(self):
        teacher = {
            'firstname': 'John',
            'lastname': 'Doe'
        }
        self.service.create_teacher(teacher)
        self.dao.create_teacher.assert_called_once_with(teacher)

    def test_get_teacher(self):
        teacher_id = 1
        self.service.get_teacher(teacher_id)
        self.dao.get_teacher.assert_called_once_with(teacher_id)

    def test_update_teacher(self):
        teacher_id = 1
        teacher = {
            'firstname': 'Jane',
            'lastname': 'Smith'
        }
        self.service.update_teacher(teacher_id, teacher)
        self.dao.update_teacher.assert_called_once_with(teacher_id, teacher)

    def test_delete_teacher(self):
        teacher_id = 1
        self.service.delete_teacher(teacher_id)
        self.dao.delete_teacher.assert_called_once_with(teacher_id)

    def test_list_teachers(self):
        self.service.list_teachers()
        self.dao.list_teachers.assert_called_once()

if __name__ == '__main__':
    unittest.main()