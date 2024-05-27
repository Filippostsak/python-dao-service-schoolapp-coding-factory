import mysql.connector
from dao.abc_teacher_dao import ABCTeacherDAO

class TeacherDAOImpl(ABCTeacherDAO):

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_teacher(self, teacher):
        sql = "INSERT INTO TEACHERS (FIRSTNAME, LASTNAME) VALUES (%s, %s)"
        self.cursor.execute(sql, (teacher['firstname'], teacher['lastname']))
        self.connection.commit()

    def get_teacher(self, teacher_id):
        sql = "SELECT * FROM TEACHERS WHERE ID = %s"
        self.cursor.execute(sql, (teacher_id,))
        return self.cursor.fetchone()

    def update_teacher(self, teacher_id, teacher):
        sql = "UPDATE TEACHERS SET FIRSTNAME = %s, LASTNAME = %s WHERE ID = %s"
        self.cursor.execute(sql, (teacher['firstname'], teacher['lastname'], teacher_id))
        self.connection.commit()

    def delete_teacher(self, teacher_id):
        sql = "DELETE FROM TEACHERS WHERE ID = %s"
        self.cursor.execute(sql, (teacher_id,))
        self.connection.commit()

    def list_teachers(self):
        sql = "SELECT * FROM TEACHERS"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
