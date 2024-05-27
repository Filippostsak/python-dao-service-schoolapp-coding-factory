import mysql.connector
from dao.abc_student_dao import ABCStudentDAO

class StudentDAOImpl(ABCStudentDAO):

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_student(self, student):
        sql = "INSERT INTO STUDENTS (FIRSTNAME, LASTNAME) VALUES (%s, %s)"
        self.cursor.execute(sql, (student['firstname'], student['lastname']))
        self.connection.commit()

    def get_student(self, student_id):
        sql = "SELECT * FROM STUDENTS WHERE ID = %s"
        self.cursor.execute(sql, (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student_id, student):
        sql = "UPDATE STUDENTS SET FIRSTNAME = %s, LASTNAME = %s WHERE ID = %s"
        self.cursor.execute(sql, (student['firstname'], student['lastname'], student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        sql = "DELETE FROM STUDENTS WHERE ID = %s"
        self.cursor.execute(sql, (student_id,))
        self.connection.commit()

    def list_students(self):
        sql = "SELECT * FROM STUDENTS"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
