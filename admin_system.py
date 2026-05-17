from data_manager import DataManager
import os


class AdminSystem:
    def __init__(self):
        self.dataManager = DataManager()
    def run(self):
        os.system("cls")
        print("Entering Admin System...\n")
        input("Press Enter to continue...")
        self.menu()

    def menu(self):
        while True:
            os.system("cls")
            print("Admin Menu")
            print("1: View all students")
            print("2: Remove a student")
            print("3: Clear all student data")
            print("4: Logout\n")

            ip = input("Enter your option: ")

            if ip == "1":
                self.viewStudents()
            elif ip == "2":
                self.removeStudent()
            elif ip == "3":
                self.clearStudentData()
            elif ip == "4":
                os.system("cls")
                break
            else:
                print("Invalid input! Please try again.\n")
                input("Press Enter to continue...")

    def viewStudents(self):
        os.system("cls")
        students = self.dataManager.loadAllStudentsList()

        if len(students) == 0:
            print("No student data found.\n")
            input("Press Enter to continue...")
            return

        print("Student List")
        for i, student in enumerate(students, start=1):
            print(f"{i}. SID: {student.id}, Name: {student.name}, Email: {student.email}")
            if len(student.subjects) == 0:
                print("   No enrolled subject.")
            else:
                for subject in student.subjects:
                    print(f"   Subject ID: {subject.subjectId}, Mark: {subject.mark}, Grade: {subject.grade}")
            print()

        input("Press Enter to continue...")

    def removeStudent(self):
        while True:
            os.system("cls")
            students = self.dataManager.loadAllStudentsList()

            if len(students) == 0:
                print("No student data found.\n")
                input("Press Enter to continue...")
                return

            print("Student List")
            for i, student in enumerate(students, start=1):
                print(f"{i}. SID: {student.id}, Name: {student.name}, Email: {student.email}")
            print(f"{len(students) + 1}. Exit\n")

            choice = input("Select the student number to remove: ")

            if not choice.isdigit():
                print("Invalid input! Please try again.\n")
                input("Press Enter to continue...")
                continue

            choice = int(choice)

            if choice == len(students) + 1:
                break

            if 1 <= choice <= len(students):
                student = students[choice - 1]
                self.dataManager.deleteStudent(student.id)
                print(f"Student {student.name} ({student.id}) has been removed.\n")
                input("Press Enter to continue...")
                break
            else:
                print("Invalid option! Please try again.\n")
                input("Press Enter to continue...")

    def clearStudentData(self):
        os.system("cls")
        confirm = input("Are you sure you want to clear all student data? (yes/no): ")

        if confirm.lower() == "yes":
            self.dataManager.saveAllStudents([])
            print("All student data has been cleared.\n")
        else:
            print("Operation cancelled.\n")

        input("Press Enter to continue...")