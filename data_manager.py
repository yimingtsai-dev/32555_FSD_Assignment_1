import os
from student import Student
from subject import Subject


class DataManager:
    def __init__(self, fileName="student.data"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.fileName = os.path.join(base_dir, fileName)
        self.createFile()

    def createFile(self):
        if not os.path.exists(self.fileName):
            with open(self.fileName, "w", encoding="utf-8") as file:
                pass

    def generateStudentId(self):
        students = self.loadAllStudentsList()
        new_id = len(students) + 1
        return str(new_id).zfill(6)

    def studentToLine(self, student):
        subject_parts = []
        for subject in student.subjects:
            subject_parts.append(f"{subject.subjectId}:{subject.mark}")

        subjects_str = "|".join(subject_parts)
        return f"{student.id},{student.name},{student.email},{student.password},{subjects_str}\n"

    def lineToStudent(self, line):
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

    def loadAllStudentsList(self):
        students = []
        self.createFile()

        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file:
                student = self.lineToStudent(line)
                if student is not None:
                    students.append(student)

        return students

    def loadAllStudentsDict(self):
        students_dict = {}
        students = self.loadAllStudentsList()

        for student in students:
            students_dict[student.email] = student

        return students_dict

    def saveAllStudents(self, students):
        with open(self.fileName, "w", encoding="utf-8") as file:
            for student in students:
                file.write(self.studentToLine(student))

    def addStudent(self, student):
        with open(self.fileName, "a", encoding="utf-8") as file:
            file.write(self.studentToLine(student))

    def updateStudent(self, updated_student):
        students = self.loadAllStudentsList()

        for i in range(len(students)):
            if students[i].id == updated_student.id:
                students[i] = updated_student
                self.saveAllStudents(students)
                return True

        return False

    def deleteStudent(self, student_id):
        students = self.loadAllStudentsList()
        new_students = []
        deleted = False

        for student in students:
            if student.id == student_id:
                deleted = True
            else:
                new_students.append(student)

        if deleted:
            self.saveAllStudents(new_students)

        return deleted

    def emailExists(self, email):
        students_dict = self.loadAllStudentsDict()
        return email in students_dict

    def findStudentByLogin(self, email, password):
        students_dict = self.loadAllStudentsDict()

        if email in students_dict:
            student = students_dict[email]
            if student.password == password:
                return student

        return None

    def getStudentCount(self):
        return len(self.loadAllStudentsList())

    def getStudentNames(self):
        students = self.loadAllStudentsList()
        names = []

        for student in students:
            names.append(student.name)

        return names