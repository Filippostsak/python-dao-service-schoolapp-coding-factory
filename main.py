from service.teacher_service import TeacherService
from service.student_service import StudentService
from dao.teacher_dao_impl import TeacherDAOImpl
from dao.student_dao_impl import StudentDAOImpl

def main():
    teacher_dao = TeacherDAOImpl(host="localhost", user="schoolapp", password="schoolapp12345", database="schoolapp")
    student_dao = StudentDAOImpl(host="localhost", user="schoolapp", password="schoolapp12345", database="schoolapp")
    teacher_service = TeacherService(teacher_dao)
    student_service = StudentService(student_dao)

    while True:
        print("\nSchool Management System")
        print("1. Add Teacher")
        print("2. Get Teacher")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. List Teachers")
        print("6. Add Student")
        print("7. Get Student")
        print("8. Update Student")
        print("9. Delete Student")
        print("10. List Students")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            teacher = {'firstname': firstname, 'lastname': lastname}
            teacher_service.create_teacher(teacher)
            print("Teacher added successfully!")

        elif choice == '2':
            teacher_id = int(input("Enter teacher ID: "))
            teacher = teacher_service.get_teacher(teacher_id)
            if teacher:
                print(f"ID: {teacher[0]}, First Name: {teacher[1]}, Last Name: {teacher[2]}")
            else:
                print("Teacher not found.")

        elif choice == '3':
            teacher_id = int(input("Enter teacher ID: "))
            firstname = input("Enter new first name: ")
            lastname = input("Enter new last name: ")
            teacher = {'firstname': firstname, 'lastname': lastname}
            teacher_service.update_teacher(teacher_id, teacher)
            print("Teacher updated successfully!")

        elif choice == '4':
            teacher_id = int(input("Enter teacher ID: "))
            teacher_service.delete_teacher(teacher_id)
            print("Teacher deleted successfully!")

        elif choice == '5':
            teachers = teacher_service.list_teachers()
            for teacher in teachers:
                print(f"ID: {teacher[0]}, First Name: {teacher[1]}, Last Name: {teacher[2]}")

        elif choice == '6':
            firstname = input("Enter first name: ")
            lastname = input("Enter last name: ")
            student = {'firstname': firstname, 'lastname': lastname}
            student_service.create_student(student)
            print("Student added successfully!")

        elif choice == '7':
            student_id = int(input("Enter student ID: "))
            student = student_service.get_student(student_id)
            if student:
                print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")
            else:
                print("Student not found.")

        elif choice == '8':
            student_id = int(input("Enter student ID: "))
            firstname = input("Enter new first name: ")
            lastname = input("Enter new last name: ")
            student = {'firstname': firstname, 'lastname': lastname}
            student_service.update_student(student_id, student)
            print("Student updated successfully!")

        elif choice == '9':
            student_id = int(input("Enter student ID: "))
            student_service.delete_student(student_id)
            print("Student deleted successfully!")

        elif choice == '10':
            students = student_service.list_students()
            for student in students:
                print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")

        elif choice == '11':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
