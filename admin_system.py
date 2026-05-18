from data_manager import DataManager
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class AdminSystem:
    def __init__(self):
        self.dataManager = DataManager()

    def run(self):
        clear_screen()
        print("Entering Admin System...\n")
        input("Press Enter to continue...")
        self.menu()

    def menu(self):
        while True:
            clear_screen()
            print("Admin System")
            print("(c) clear database")
            print("(g) group students")
            print("(p) partition students")
            print("(r) remove student")
            print("(s) show")
            print("(x) exit\n")

            ip = input("Enter your option: ").strip().lower()

            if ip == "c":
                self.clearStudentData()
            elif ip == "g":
                self.groupStudentsByGrade()
            elif ip == "p":
                self.partitionStudents()
            elif ip == "r":
                self.removeStudent()
            elif ip == "s":
                self.viewStudents()
            elif ip == "x":
                clear_screen()
                break
            else:
                print("Invalid input! Please try again.\n")
                input("Press Enter to continue...")

    def viewStudents(self):
        clear_screen()
        students = self.dataManager.loadAllStudentsList()

        if len(students) == 0:
            print("No student data found.\n")
            input("Press Enter to continue...")
            return

        print("Student List")
        print("------------")
        for student in students:
            print(f"  {student.id} :: {student.name} --> Email: {student.email}")
            if len(student.subjects) == 0:
                print("     No enrolled subjects.")
            else:
                for subject in student.subjects:
                    print(f"     Subject ID: {subject.subjectId}, Mark: {subject.mark}, Grade: {subject.grade}")
        print()
        input("Press Enter to continue...")

    def groupStudentsByGrade(self):
        clear_screen()
        students = self.dataManager.loadAllStudentsList()

        if len(students) == 0:
            print("No student data found.\n")
            input("Press Enter to continue...")
            return

        # Collect all subjects across all students, grouped by grade
        grade_groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in students:
            for subject in student.subjects:
                grade = subject.grade
                if grade in grade_groups:
                    grade_groups[grade].append((student, subject))

        print("Students grouped by grade")
        print("--------------------------")

        for grade in ["HD", "D", "C", "P", "Z"]:
            entries = grade_groups[grade]
            print(f"\n  {grade} -->")
            if len(entries) == 0:
                print("    No students in this grade.")
            else:
                for student, subject in entries:
                    print(f"    {student.name} :: {student.id} --> Subject: {subject.subjectId}, Mark: {subject.mark}")

        print()
        input("Press Enter to continue...")

    def partitionStudents(self):
        clear_screen()
        students = self.dataManager.loadAllStudentsList()

        if len(students) == 0:
            print("No student data found.\n")
            input("Press Enter to continue...")
            return

        pass_students = []
        fail_students = []

        for student in students:
            if len(student.subjects) == 0:
                fail_students.append(student)
            else:
                total_mark = sum(subject.mark for subject in student.subjects)
                average_mark = total_mark / len(student.subjects)
                if average_mark >= 50:
                    pass_students.append(student)
                else:
                    fail_students.append(student)

        print("Student Partition")
        print("-----------------")

        print("\n  PASS -->")
        if len(pass_students) == 0:
            print("    No students in PASS category.")
        else:
            for student in pass_students:
                total_mark = sum(subject.mark for subject in student.subjects)
                average_mark = total_mark / len(student.subjects)
                print(f"    {student.name} :: {student.id} --> Average Mark: {average_mark:.1f}")

        print("\n  FAIL -->")
        if len(fail_students) == 0:
            print("    No students in FAIL category.")
        else:
            for student in fail_students:
                if len(student.subjects) == 0:
                    print(f"    {student.name} :: {student.id} --> Average Mark: N/A (no subjects)")
                else:
                    total_mark = sum(subject.mark for subject in student.subjects)
                    average_mark = total_mark / len(student.subjects)
                    print(f"    {student.name} :: {student.id} --> Average Mark: {average_mark:.1f}")

        print()
        input("Press Enter to continue...")

    def removeStudent(self):
        clear_screen()
        students = self.dataManager.loadAllStudentsList()

        if len(students) == 0:
            print("No student data found.\n")
            input("Press Enter to continue...")
            return

        print("Student List")
        print("------------")
        for student in students:
            print(f"  {student.id} :: {student.name}")
        print()

        student_id = input("Enter student ID to remove: ").strip()

        # Find student by ID
        target = None
        for student in students:
            if student.id == student_id:
                target = student
                break

        if target is None:
            print(f"Student with ID {student_id} not found.\n")
            input("Press Enter to continue...")
            return

        self.dataManager.deleteStudent(target.id)
        print(f"Student {target.name} ({target.id}) has been removed.\n")
        input("Press Enter to continue...")

    def clearStudentData(self):
        clear_screen()
        confirm = input("Are you sure you want to clear all student data? (yes/no): ").strip().lower()

        if confirm == "yes":
            self.dataManager.saveAllStudents([])
            print("All student data has been cleared.\n")
        else:
            print("Operation cancelled.\n")

        input("Press Enter to continue...")
