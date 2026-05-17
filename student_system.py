from getpass import getpass
import random
from data_manager import DataManager, Subject
from student import Student
import os


class StudentSystem:
    def __init__(self):
        self.currentStudent = None
        self.dataManager = DataManager()

    def run(self):
        while True:
            print("Student System")
            print("1: New register")
            print("2: Login")
            print("3: Exit to main menu\n")

            ip = input("Enter your option: ")

            if ip == "1":
                os.system("cls")
                print("New register")
                self.registerStudent()
            elif ip == "2":
                os.system("cls")
                self.loginStudent()
            elif ip == "3":
                print("Returning to main menu...")
                break
            else:
                print("Invalid input! Please try again")

    def registerStudent(self):
        while True:
            name = input("Enter your name: ")
            email = input("Enter your email: ")

            if self.checkValidNameEmail(name, email):
                if self.dataManager.emailExists(email):
                    print("This email is already registered. Please try again.\n")
                else:
                    break

        os.system("cls")

        while True:
            pwd = getpass("Enter your password: ")

            if self.checkValidPwd(pwd):
                repwd = getpass("Confirm your password: ")

                if repwd == pwd:
                    print("Password confirmed, creating student data...")
                    break
                else:
                    print("Passwords do not match. Please try again.\n")

        student_id = self.dataManager.generateStudentId()
        student = Student(student_id, name, email, pwd)

        self.dataManager.addStudent(student)
        self.currentStudent = student

        print(f"Registration successful. Your student ID is {student.id}\n")
        input("Press Enter to continue...")
        os.system("cls")
        self.menu()

    def loginStudent(self):
        while True:
            print("Login")
            print("Enter 'exit' at any time to return to the previous menu.\n")
            email = input("Enter your email: ")

            if email.lower() == "exit":
                os.system("cls")
                break

            pwd = getpass("Enter your password: ")

            if pwd.lower() == "exit":
                os.system("cls")
                break

            student = self.dataManager.findStudentByLogin(email, pwd)

            if student is not None:
                self.currentStudent = student
                print(f"Login successful. Welcome, {student.name}.\n")
                input("Press Enter to continue...")
                os.system("cls")
                self.menu()
                break
            else:
                print("Invalid email or password.\n")
                input("Press Enter to try again...")
                os.system("cls")

    def checkValidNameEmail(self, name, email):
        parts = name.strip().split()

        if len(parts) != 2:
            print("Invalid name! Please enter first name and last name.\n")
            return False

        first_name = parts[0]
        last_name = parts[1]

        expected_email = f"{first_name.lower()}.{last_name.lower()}@university.com"

        if email.lower() != expected_email:
            print("Invalid email format! Please try again.\n")
            return False

        return True

    def checkValidPwd(self, password):
        if not password:
            print("Password cannot be empty.\n")
            return False

        if not password[0].isupper():
            print("Password must start with an upper-case letter.\n")
            return False

        letters_part = ""
        digits_part = ""
        i = 0

        while i < len(password) and password[i].isalpha():
            letters_part += password[i]
            i += 1

        while i < len(password) and password[i].isdigit():
            digits_part += password[i]
            i += 1

        if i != len(password):
            print("Password must contain letters first, followed by digits only.\n")
            return False

        if len(letters_part) < 5:
            print("Password must contain at least five letters.\n")
            return False

        if len(digits_part) < 3:
            print("Password must be followed by at least three digits.\n")
            return False

        return True
    
    def menu(self):
        while True:
            os.system("cls")
            print(f"Welcome, {self.currentStudent.name}！ SID: {self.currentStudent.id}")
            print("Student Menu")
            print("1: Enrol in a subject")
            print("2: Remove a subject from enrolment list")
            print("3: View current enrolment list")
            print("4: Change password")
            print("5: Logout\n")

            ip = input("Enter your option: ")

            if ip == "1":
                self.enrolSubject()
            elif ip == "2":
                print("Remove subject function")
                self.removeSubject()
            elif ip == "3":
                print("View enrolment list function")
                self.viewEnrolmentList()
            elif ip == "4":
                self.changePassword()
            elif ip == "5":
                os.system("cls")
                self.currentStudent = None
                break
            else:
                print("Invalid input! Please try again.\n")
                input("Press Enter to continue...")

    def enrolSubject(self):
        if self.currentStudent is None:
            print("No student is currently logged in.\n")
            return

        if len(self.currentStudent.subjects) >= 4:
            print("You cannot enrol in more than four subjects.\n")
            return
        os.system("cls")
        subject_id = self.generateSubjectId()
        mark = random.randint(25, 100)

        new_subject = Subject(subject_id, mark)
        self.currentStudent.subjects.append(new_subject)

        self.dataManager.updateStudent(self.currentStudent)

        print("Subject enrolled successfully.")
        print(f"Subject ID: {new_subject.subjectId}")
        print(f"Mark: {new_subject.mark}")
        print(f"Grade: {new_subject.grade}\n")
        print("Press Enter to continue...")
        input()
        os.system("cls")
    
    def generateSubjectId(self):
        current_ids = set()

        for subject in self.currentStudent.subjects:
            current_ids.add(subject.subjectId)

        while True:
            new_id = str(random.randint(1, 999)).zfill(3)
            if new_id not in current_ids:
                return new_id

    def removeSubject(self):
        if self.currentStudent is None:
            print("No student is currently logged in.\n")
            input("Press Enter to continue...")
            return

        if len(self.currentStudent.subjects) == 0:
            print("No enrolled subject.\n")
            input("Press Enter to continue...")
            return

        while True:
            os.system("cls")
            print("Current Enrolment List")

            for i, subject in enumerate(self.currentStudent.subjects, start=1):
                print(f"{i}. Subject ID: {subject.subjectId}, Mark: {subject.mark}, Grade: {subject.grade}")

            print(f"{len(self.currentStudent.subjects) + 1}. Exit\n")

            choice = input("Select the subject number to remove: ")

            if not choice.isdigit():
                print("Invalid input! Please try again.\n")
                input("Press Enter to continue...")
                continue

            choice = int(choice)

            if choice == len(self.currentStudent.subjects) + 1:
                break

            if 1 <= choice <= len(self.currentStudent.subjects):
                self.currentStudent.subjects.pop(choice - 1)
                self.dataManager.updateStudent(self.currentStudent)
                print("Subject removed successfully.\n")
                input("Press Enter to continue...")
                os.system("cls")    
                break
            else:
                print("Invalid option! Please try again.\n")
                input("Press Enter to continue...")
    def viewEnrolmentList(self):
        os.system("cls")
        if self.currentStudent is None:
            print("No student is currently logged in.\n")
            input("Press Enter to continue...")
            return
        if len(self.currentStudent.subjects) == 0:
            print("No enrolled subject.\n")
            input("Press Enter to continue...")
            return

        print("Current Enrolment List")
        for subject in self.currentStudent.subjects:
            print(f"Subject ID: {subject.subjectId}, Mark: {subject.mark}, Grade: {subject.grade}")
        print()
        input("Press Enter to continue...")
        os.system("cls")

    def changePassword(self):
        os.system("cls")

        if self.currentStudent is None:
            print("No student is currently logged in.\n")
            input("Press Enter to continue...")
            return

        old_pwd = getpass("Enter your current password: ")

        if old_pwd != self.currentStudent.password:
            print("Incorrect current password.\n")
            input("Press Enter to continue...")
            return

        while True:
            new_pwd = getpass("Enter your new password: ")

            if not self.checkValidPwd(new_pwd):
                continue

            confirm_pwd = getpass("Confirm your new password: ")

            if confirm_pwd != new_pwd:
                print("Passwords do not match. Please try again.\n")
                continue

            self.currentStudent.password = new_pwd
            self.dataManager.updateStudent(self.currentStudent)
            print("Password changed successfully.\n")
            input("Press Enter to continue...")
            os.system("cls")
            break
