import unittest
from unittest.mock import MagicMock
from service.student_service import StudentService

class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.dao = MagicMock()
        self.service = StudentService(self.dao)

    def tearDown(self):
        del self.service

    def test_create_student(self):
        student = {
            'firstname': 'John',
            'lastname': 'Doe'
        }
        self.service.create_student(student)
        self.dao.create_student.assert_called_once_with(student)

    def test_get_student(self):
        student_id = 1
        self.dao.get_student.return_value = ('John', 'Doe')
        result = self.service.get_student(student_id)
        self.dao.get_student.assert_called_once_with(student_id)
        self.assertEqual(result, ('John', 'Doe'))

    def test_update_student(self):
        student_id = 1
        student = {
            'firstname': 'Jane',
            'lastname': 'Smith'
        }
        self.service.update_student(student_id, student)
        self.dao.update_student.assert_called_once_with(student_id, student)

    def test_delete_student(self):
        student_id = 1
        self.service.delete_student(student_id)
        self.dao.delete_student.assert_called_once_with(student_id)

    def test_list_students(self):
        self.dao.list_students.return_value = [('John', 'Doe'), ('Jane', 'Smith')]
        result = self.service.list_students()
        self.dao.list_students.assert_called_once()
        self.assertEqual(result, [('John', 'Doe'), ('Jane', 'Smith')])

if __name__ == '__main__':
    unittest.main()