import unittest
from unittest.mock import MagicMock
from dao.teacher_dao_impl import TeacherDAOImpl

class TestTeacherDAOImpl(unittest.TestCase):

    def setUp(self):
        self.host = "localhost"
        self.user = "schoolapp"
        self.password = "schoolapp12345"
        self.database = "schoolapp"
        self.dao = TeacherDAOImpl(self.host, self.user, self.password, self.database)

    def tearDown(self):
        del self.dao

    def test_create_teacher(self):
        teacher = {
            'firstname': 'John',
            'lastname': 'Doe'
        }
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.create_teacher(teacher)
        self.dao.cursor.execute.assert_called_once_with(
            "INSERT INTO TEACHERS (FIRSTNAME, LASTNAME) VALUES (%s, %s)",
            ('John', 'Doe')
        )
        self.dao.connection.commit.assert_called_once()

    def test_get_teacher(self):
        teacher_id = 1
        self.dao.cursor.execute = MagicMock()
        self.dao.cursor.fetchone = MagicMock(return_value=('John', 'Doe'))
        result = self.dao.get_teacher(teacher_id)
        self.dao.cursor.execute.assert_called_once_with(
            "SELECT * FROM TEACHERS WHERE ID = %s",
            (teacher_id,)
        )
        self.assertEqual(result, ('John', 'Doe'))

    def test_update_teacher(self):
        teacher_id = 1
        teacher = {
            'firstname': 'Jane',
            'lastname': 'Smith'
        }
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.update_teacher(teacher_id, teacher)
        self.dao.cursor.execute.assert_called_once_with(
            "UPDATE TEACHERS SET FIRSTNAME = %s, LASTNAME = %s WHERE ID = %s",
            ('Jane', 'Smith', teacher_id)
        )
        self.dao.connection.commit.assert_called_once()

    def test_delete_teacher(self):
        teacher_id = 1
        self.dao.cursor.execute = MagicMock()
        self.dao.connection.commit = MagicMock()
        self.dao.delete_teacher(teacher_id)
        self.dao.cursor.execute.assert_called_once_with(
            "DELETE FROM TEACHERS WHERE ID = %s",
            (teacher_id,)
        )
        self.dao.connection.commit.assert_called_once()

    def test_list_teachers(self):
        self.dao.cursor.execute = MagicMock()
        self.dao.cursor.fetchall = MagicMock(return_value=[('John', 'Doe'), ('Jane', 'Smith')])
        result = self.dao.list_teachers()
        self.dao.cursor.execute.assert_called_once_with("SELECT * FROM TEACHERS")
        self.assertEqual(result, [('John', 'Doe'), ('Jane', 'Smith')])

if __name__ == '__main__':
    unittest.main()