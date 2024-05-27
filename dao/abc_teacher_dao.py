from abc import ABC, abstractmethod

class ABCTeacherDAO(ABC):

    @abstractmethod
    def create_teacher(self, teacher):
        pass

    @abstractmethod
    def get_teacher(self, teacher_id):
        pass

    @abstractmethod
    def update_teacher(self, teacher_id, teacher):
        pass

    @abstractmethod
    def delete_teacher(self, teacher_id):
        pass

    @abstractmethod
    def list_teachers(self):
        pass
