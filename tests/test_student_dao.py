import unittest
from unittest.mock import MagicMock
from dao.student_dao_impl import StudentDAOImpl

class TestStudentDAOImpl(unittest.TestCase):

    def setUp(self):
        self.host = "localhost"
        self.user = "schoolapp"
        self.password = "schoolapp12345"
        self.database = "schoolapp"
        self.dao = StudentDAOImpl(self.host, self.user, self.password, self.database)

    def tearDown(self):
        del self.dao

    def test_create_student(self):
        student = {
            'firstname': 'John',
            'lastname': 'Doe'
        }
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.create_student(student)
        self.dao.cursor.execute.assert_called_once_with(
            "INSERT INTO STUDENTS (FIRSTNAME, LASTNAME) VALUES (%s, %s)",
            ('John', 'Doe')
        )
        self.dao.connection.commit.assert_called_once()

    def test_get_student(self):
        student_id = 1
        self.dao.cursor.execute = MagicMock()
        self.dao.cursor.fetchone = MagicMock(return_value=('John', 'Doe'))
        result = self.dao.get_student(student_id)
        self.dao.cursor.execute.assert_called_once_with(
            "SELECT * FROM STUDENTS WHERE ID = %s",
            (student_id,)
        )
        self.assertEqual(result, ('John', 'Doe'))

    def test_update_student(self):
        student_id = 1
        student = {
            'firstname': 'Jane',
            'lastname': 'Smith'
        }
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.update_student(student_id, student)
        self.dao.cursor.execute.assert_called_once_with(
            "UPDATE STUDENTS SET FIRSTNAME = %s, LASTNAME = %s WHERE ID = %s",
            ('Jane', 'Smith', student_id)
        )
        self.dao.connection.commit.assert_called_once()

    def test_delete_student(self):
        student_id = 1
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.delete_student(student_id)
        self.dao.cursor.execute.assert_called_once_with(
            "DELETE FROM STUDENTS WHERE ID = %s",
            (student_id,)
        )
        self.dao.connection.commit.assert_called_once()

    def test_list_students(self):
        self.dao.cursor.execute = MagicMock()
        self.dao.cursor.fetchall = MagicMock(return_value=[('John', 'Doe'), ('Jane', 'Smith')])
        result = self.dao.list_students()
        self.dao.cursor.execute.assert_called_once_with("SELECT * FROM STUDENTS")
        self.assertEqual(result, [('John', 'Doe'), ('Jane', 'Smith')])

if __name__ == '__main__':
    unittest.main()
