from abc import ABC, abstractmethod

class ABCStudentDAO(ABC):

    @abstractmethod
    def create_student(self, student):
        pass

    @abstractmethod
    def get_student(self, student_id):
        pass

    @abstractmethod
    def update_student(self, student_id, student):
        pass

    @abstractmethod
    def delete_student(self, student_id):
        pass

    @abstractmethod
    def list_students(self):
        pass
