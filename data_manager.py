import os
from student import Student
from subject import Subject


class DataManager:
    def __init__(self, file_name="student.data"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(base_dir, file_name)
        self.create_file()

    def create_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="utf-8") as file:
                pass

    def generate_student_id(self):
        students = self.load_all_students_list()
        new_id = len(students) + 1
        return str(new_id).zfill(6)

    def student_to_line(self, student):
        subject_parts = []
        for subject in student.subjects:
            subject_parts.append(f"{subject.subjectId}:{subject.mark}")

        subjects_str = "|".join(subject_parts)
        return f"{student.id},{student.name},{student.email},{student.password},{subjects_str}\n"

    def line_to_student(self, line):
        line = line.strip()
        if line == "":
            return None

        parts = line.split(",", 4)
        if len(parts) < 5:
            return None

        student_id = parts[0]
        name = parts[1]
        email = parts[2]
        password = parts[3]
        subjects_str = parts[4]

        student = Student(student_id, name, email, password)

        if subjects_str != "":
            subject_items = subjects_str.split("|")
            for item in subject_items:
                if item == "":
                    continue

                subject_parts = item.split(":")
                if len(subject_parts) != 2:
                    continue

                subject_id = subject_parts[0]
                mark = int(subject_parts[1])
                subject = Subject(subject_id, mark)
                student.subjects.append(subject)

        return student

    def load_all_students_list(self):
        students = []
        self.create_file()

        with open(self.file_name, "r", encoding="utf-8") as file:
            for line in file:
                student = self.line_to_student(line)
                if student is not None:
                    students.append(student)

        return students

    def load_all_students_dict(self):
        students_dict = {}
        students = self.load_all_students_list()

        for student in students:
            students_dict[student.email] = student

        return students_dict

    def save_all_students(self, students):
        with open(self.file_name, "w", encoding="utf-8") as file:
            for student in students:
                file.write(self.student_to_line(student))

    def add_student(self, student):
        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(self.student_to_line(student))

    def update_student(self, updated_student):
        students = self.load_all_students_list()

        for i in range(len(students)):
            if students[i].id == updated_student.id:
                students[i] = updated_student
                self.save_all_students(students)
                return True

        return False

    def delete_student(self, student_id):
        students = self.load_all_students_list()
        new_students = []
        deleted = False

        for student in students:
            if student.id == student_id:
                deleted = True
            else:
                new_students.append(student)

        if deleted:
            self.save_all_students(new_students)

        return deleted

    def email_exists(self, email):
        students_dict = self.load_all_students_dict()
        return email in students_dict

    def find_student_by_login(self, email, password):
        students_dict = self.load_all_students_dict()

        if email in students_dict:
            student = students_dict[email]
            if student.password == password:
                return student

        return None

    def get_student_count(self):
        return len(self.load_all_students_list())

    def get_student_names(self):
        students = self.load_all_students_list()
        names = []

        for student in students:
            names.append(student.name)

        return names