import re
import random
from data_manager import DataManager, Subject
from Model.student import Student
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class StudentSystem:
    def __init__(self):
        self.currentStudent = None
        self.dataManager = DataManager()

    def run(self):
        while True:
            ip = input("Student System (l/r/x): ").strip().lower()

            if ip == "r":
                self.registerStudent()
            elif ip == "l":
                self.loginStudent()
            elif ip == "x":
                break
            else:
                print("Invalid input! Please try again.")

    def registerStudent(self):
        print("Student Sign Up")
        while True:
            email = input("   Email: ")
            password = input("   Password: ")

            if not self._validateEmail(email) or not self._validatePassword(password):
                print("   Incorrect email or password format")
                continue

            print("   email and password formats acceptable")

            if self.dataManager.emailExists(email):
                print("   Student {0} already exists".format(self._emailToName(email)))
                return

            name = input("   Name: ")
            student_id = self.dataManager.generateStudentId()
            student = Student(student_id, name, email, password)
            self.dataManager.addStudent(student)

            print("   Enrolling Student {0}".format(name))
            print("   Registration successful. Your student ID is {0}".format(student_id))

            self.currentStudent = student
            self.menu()
            return

    def loginStudent(self):
        print("Student Sign In")
        while True:
            email = input("   Email: ")
            password = input("   Password: ")

            if not self._validateEmail(email) or not self._validatePassword(password):
                print("   Incorrect email or password format")
                continue

            print("   email and password formats acceptable")

            student = self.dataManager.findStudentByLogin(email, password)

            if student is None:
                print("   Student does not exist")
                return

            self.currentStudent = student
            print("   Login successful. Welcome, {0}.".format(student.name))
            self.menu()
            return

    def _validateEmail(self, email):
        pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
        return bool(re.match(pattern, email))

    def _validatePassword(self, password):
        pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'
        return bool(re.match(pattern, password))

    # --- Public aliases used by GUI controllers ---
    def checkValidNameEmail(self, name, email):
        """GUI register_controller calls this to validate name + email."""
        parts = name.strip().split()
        if len(parts) != 2:
            return False
        first, last = parts
        expected = "{0}.{1}@university.com".format(first.lower(), last.lower())
        if email.lower() != expected:
            return False
        return self._validateEmail(email)

    def checkValidPwd(self, password):
        """GUI register_controller calls this to validate password."""
        return self._validatePassword(password)

    def _emailToName(self, email):
        local = email.split("@")[0]
        parts = local.split(".")
        return " ".join(p.capitalize() for p in parts)

    def menu(self):
        while True:
            ip = input("Student Course Menu (c/e/r/s/x): ").strip().lower()

            if ip == "c":
                self.changePassword()
            elif ip == "e":
                self.enrolSubject()
            elif ip == "r":
                self.removeSubject()
            elif ip == "s":
                self.viewEnrolmentList()
            elif ip == "x":
                self.currentStudent = None
                break
            else:
                print("Invalid input! Please try again.")

    def enrolSubject(self):
        if len(self.currentStudent.subjects) >= 4:
            print("   Students are allowed to enrol in 4 subjects only")
            return

        subject_id = self._generateSubjectId()
        mark = random.randint(25, 100)
        new_subject = Subject(subject_id, mark)
        self.currentStudent.subjects.append(new_subject)
        self.dataManager.updateStudent(self.currentStudent)

        count = len(self.currentStudent.subjects)
        print("   Enrolling in Subject-{0}".format(subject_id))
        print("   You are now enrolled in {0} out of 4 subjects".format(count))

    def _generateSubjectId(self):
        current_ids = {s.subjectId for s in self.currentStudent.subjects}
        while True:
            new_id = str(random.randint(1, 999)).zfill(3)
            if new_id not in current_ids:
                return new_id

    def removeSubject(self):
        if len(self.currentStudent.subjects) == 0:
            print("   No enrolled subjects.")
            return

        subject_id = input("   Remove Subject by ID: ").strip()

        target = None
        for s in self.currentStudent.subjects:
            if s.subjectId == subject_id:
                target = s
                break

        if target is None:
            print("   Subject {0} not found.".format(subject_id))
            return

        self.currentStudent.subjects.remove(target)
        self.dataManager.updateStudent(self.currentStudent)
        count = len(self.currentStudent.subjects)
        print("   Droping Subject-{0}".format(subject_id))
        print("   You are now enrolled in {0} out of 4 subjects".format(count))

    def viewEnrolmentList(self):
        count = len(self.currentStudent.subjects)
        print("   Showing {0} subjects".format(count))
        for s in self.currentStudent.subjects:
            print("   [ Subject::{0} -- mark = {1} -- grade = {2:>3} ]".format(
                s.subjectId, s.mark, s.grade))

    def changePassword(self):
        print("   Updating Password")
        while True:
            new_pwd = input("   New Password: ")
            confirm_pwd = input("   Confirm Password: ")

            if new_pwd != confirm_pwd:
                print("   Password does not match -- try again")
                continue

            if not self._validatePassword(new_pwd):
                print("   Incorrect password format")
                continue

            self.currentStudent.password = new_pwd
            self.dataManager.updateStudent(self.currentStudent)
            break
