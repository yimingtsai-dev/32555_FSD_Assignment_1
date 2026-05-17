import random
from tkinter import messagebox as mb, simpledialog
from Model.subject import Subject


class DashboardController:
    def __init__(self, app):
        self.app = app

    def generateSubjectId(self):
        existing_ids = {subject.subjectId for subject in self.app.currentStudent.subjects}
        while True:
            new_id = str(random.randint(1, 999)).zfill(3)
            if new_id not in existing_ids:
                return new_id

    def handleEnrol(self, frame):
        if self.app.currentStudent is None:
            return

        if len(self.app.currentStudent.subjects) >= 4:
            mb.showwarning("Limit Reached", "You can only enrol in up to four subjects.")
            return

        subject_id = self.generateSubjectId()
        mark = random.randint(25, 100)
        new_subject = Subject(subject_id, mark)
        self.app.currentStudent.subjects.append(new_subject)
        self.app.dataManager.updateStudent(self.app.currentStudent)
        frame.refreshDashboard(self.app.currentStudent)
        mb.showinfo("Subject Enrolled", f"Subject {subject_id} enrolled. Mark: {mark}, Grade: {new_subject.grade}")

    def handleRemoveSubject(self, frame):
        selected = frame.subjectTree.selection()
        if not selected:
            mb.showwarning("Select Subject", "Please select a subject to remove.")
            return

        subject_id = frame.subjectTree.item(selected[0], "values")[0]
        self.app.currentStudent.subjects = [s for s in self.app.currentStudent.subjects if s.subjectId != subject_id]
        self.app.dataManager.updateStudent(self.app.currentStudent)
        frame.refreshDashboard(self.app.currentStudent)
        mb.showinfo("Removed", f"Subject {subject_id} removed.")

    def handleChangePassword(self, frame):
        if self.app.currentStudent is None:
            return

        new_password = simpledialog.askstring("Change Password", "Enter new password:", show="*")
        if new_password is None:
            return

        confirm_password = simpledialog.askstring("Change Password", "Confirm new password:", show="*")
        if confirm_password is None:
            return

        if new_password != confirm_password:
            mb.showwarning("Password Mismatch", "The password entries do not match.")
            return

        if not self.app.system.checkValidPwd(new_password):
            mb.showwarning(
                "Invalid Password",
                "Password must start with an uppercase letter, contain at least five letters, and end with at least three digits.",
            )
            return

        self.app.currentStudent.password = new_password
        self.app.dataManager.updateStudent(self.app.currentStudent)
        mb.showinfo("Password Updated", "Your password has been updated.")

    def handleLogout(self, frame):
        self.app.currentStudent = None
        self.app.showFrame("login")
