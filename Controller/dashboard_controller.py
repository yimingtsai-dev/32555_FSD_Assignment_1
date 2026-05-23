import random
import tkinter as tk
from tkinter import messagebox as mb
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

    def handleEnroll(self, frame):
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

        passwords = self.askPasswordPair(frame)
        if passwords is None:
            return

        new_password, confirm_password = passwords

        if new_password == "" or confirm_password == "":
            mb.showwarning("Missing Password", "Please enter and confirm the new password.")
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

    def askPasswordPair(self, frame):
        dialog = tk.Toplevel(frame)
        dialog.title("Change Password")
        dialog.resizable(False, False)
        dialog.configure(bg="white")
        dialog.transient(frame.winfo_toplevel())
        dialog.grab_set()

        result = {"value": None}

        rule_text = (
            "Password rules:\n"
            "1. Start with an uppercase letter\n"
            "2. Have at least 5 letters\n"
            "3. Have 3 or more digits at the end\n"
            "e.g. Password123"
        )
        tk.Label(dialog, text=rule_text, bg="white", fg="darkgreen", justify="left").grid(
            row=0, column=0, columnspan=2, padx=12, pady=(12, 8), sticky="w"
        )

        tk.Label(dialog, text="New password:", bg="white").grid(row=1, column=0, padx=12, pady=6, sticky="w")
        new_entry = tk.Entry(dialog, show="*", width=28)
        new_entry.grid(row=1, column=1, padx=12, pady=6)

        tk.Label(dialog, text="Confirm password:", bg="white").grid(row=2, column=0, padx=12, pady=6, sticky="w")
        confirm_entry = tk.Entry(dialog, show="*", width=28)
        confirm_entry.grid(row=2, column=1, padx=12, pady=6)

        def submit():
            result["value"] = (new_entry.get(), confirm_entry.get())
            dialog.destroy()

        def cancel():
            dialog.destroy()

        button_frame = tk.Frame(dialog, bg="white")
        button_frame.grid(row=3, column=0, columnspan=2, pady=12)
        tk.Button(button_frame, text="OK", width=10, command=submit).pack(side="left", padx=8)
        tk.Button(button_frame, text="Cancel", width=10, command=cancel).pack(side="left", padx=8)

        dialog.update_idletasks()
        main_window = frame.winfo_toplevel()
        x = main_window.winfo_x() + (main_window.winfo_width() - dialog.winfo_width()) // 2
        y = main_window.winfo_y() + (main_window.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")

        new_entry.focus_set()
        dialog.bind("<Return>", lambda event: submit())
        dialog.bind("<Escape>", lambda event: cancel())
        frame.wait_window(dialog)
        return result["value"]

    def handleLogout(self, frame):
        self.app.currentStudent = None
        self.app.showFrame("login")
