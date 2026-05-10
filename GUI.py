import random
import tkinter as tk
from tkinter import messagebox as mb, simpledialog
from tkinter import ttk

from data_manager import DataManager
from student import Student
from student_system import StudentSystem
from subject import Subject


class LoginFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        # Add title label
        title = tk.Label(self, text="Student Login", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.pack(pady=(0, 20))

        # Create form frame
        form = tk.Frame(self, bg='black')
        tk.Label(form, text="Email:", anchor="w", width=16, fg='white', bg='black').grid(row=0, column=0, sticky="w")
        self.login_email = tk.Entry(form, width=40, bg='white', bd=2)
        self.login_email.grid(row=0, column=1, pady=6)

        tk.Label(form, text="Password:", anchor="w", width=16, fg='white', bg='black').grid(row=1, column=0, sticky="w")
        self.login_password = tk.Entry(form, width=40, show="*", bg='white', bd=2)
        self.login_password.grid(row=1, column=1, pady=6)
        form.pack()

        # Status label
        self.login_status = tk.Label(self, text="", fg="red", bg='black')
        self.login_status.pack(pady=(10, 0))

        # Button frame
        button_frame = tk.Frame(self, bg='black')
        tk.Button(button_frame, text="Login", width=14, command=lambda: controller.handle_login(self)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Register", width=14, command=lambda: controller.show_frame("register")).pack(side="left")
        button_frame.pack(pady=20)

    def clear_fields(self) -> None:
        self.login_email.delete(0, tk.END)
        self.login_password.delete(0, tk.END)
        self.login_status.config(text="")


class RegisterFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        # Add title label
        title = tk.Label(self, text="New Student Registration", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.pack(pady=(0, 20))

        # Create form frame
        form = tk.Frame(self, bg='black')
        tk.Label(form, text="Full name:", anchor="w", width=16, fg='white', bg='black').grid(row=0, column=0, sticky="w")
        self.reg_name = tk.Entry(form, width=40, bg='white', bd=2)
        self.reg_name.grid(row=0, column=1, pady=6)

        tk.Label(form, text="Email:", anchor="w", width=16, fg='white', bg='black').grid(row=1, column=0, sticky="w")
        self.reg_email = tk.Entry(form, width=40, bg='white', bd=2)
        self.reg_email.grid(row=1, column=1, pady=6)

        tk.Label(form, text="Password:", anchor="w", width=16, fg='white', bg='black').grid(row=2, column=0, sticky="w")
        self.reg_password = tk.Entry(form, width=40, show="*", bg='white', bd=2)
        self.reg_password.grid(row=2, column=1, pady=6)

        tk.Label(form, text="Confirm password:", anchor="w", width=16, fg='white', bg='black').grid(row=3, column=0, sticky="w")
        self.reg_confirm = tk.Entry(form, width=40, show="*", bg='white', bd=2)
        self.reg_confirm.grid(row=3, column=1, pady=6)
        form.pack()

        # Status label
        self.register_status = tk.Label(self, text="", fg="red", bg='black')
        self.register_status.pack(pady=(10, 0))

        # Button frame
        button_frame = tk.Frame(self, bg='black')
        tk.Button(button_frame, text="Register", width=14, command=lambda: controller.handle_register(self)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Back to Login", width=14, command=lambda: controller.show_frame("login")).pack(side="left")
        button_frame.pack(pady=20)

    def clear_fields(self) -> None:
        self.reg_name.delete(0, tk.END)
        self.reg_email.delete(0, tk.END)
        self.reg_password.delete(0, tk.END)
        self.reg_confirm.delete(0, tk.END)
        self.register_status.config(text="")


class DashboardFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        # Header frame
        header = tk.Frame(self, bg='black')
        self.welcome_label = tk.Label(header, text="Welcome", font=("Arial", 18, "bold"), fg='white', bg='black')
        self.welcome_label.pack(side="left")
        self.student_info_label = tk.Label(header, text="", font=("Arial", 12), fg='white', bg='black')
        self.student_info_label.pack(side="left", padx=20)
        header.pack(fill="x", pady=(0, 10))

        # Table frame
        table_frame = tk.Frame(self, bg='black')
        self.subject_tree = ttk.Treeview(table_frame, columns=("subject", "mark", "grade"), show="headings", height=10)
        self.subject_tree.heading("subject", text="Subject ID")
        self.subject_tree.heading("mark", text="Mark")
        self.subject_tree.heading("grade", text="Grade")
        self.subject_tree.column("subject", width=200, anchor="center")
        self.subject_tree.column("mark", width=120, anchor="center")
        self.subject_tree.column("grade", width=120, anchor="center")
        self.subject_tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.subject_tree.yview)
        self.subject_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        table_frame.pack(fill="both", expand=True)

        # Button frame
        button_frame = tk.Frame(self, bg='black')
        tk.Button(button_frame, text="Enrol Subject", width=16, command=lambda: controller.handle_enrol(self)).pack(side="left", padx=8, pady=10)
        tk.Button(button_frame, text="Remove Selected", width=16, command=lambda: controller.handle_remove_subject(self)).pack(side="left", padx=8)
        tk.Button(button_frame, text="Change Password", width=16, command=lambda: controller.handle_change_password(self)).pack(side="left", padx=8)
        tk.Button(button_frame, text="Logout", width=16, command=lambda: controller.handle_logout(self)).pack(side="left", padx=8)
        button_frame.pack(pady=10)

    def refresh_dashboard(self, student) -> None:
        self.welcome_label.config(text=f"Welcome, {student.name}")
        self.student_info_label.config(text=f"Student ID: {student.id}")

        for item in self.subject_tree.get_children():
            self.subject_tree.delete(item)

        for subject in student.subjects:
            self.subject_tree.insert("", tk.END, values=(subject.subjectId, subject.mark, subject.grade))


class StudentGUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("UniApp Student System")
        self.root.geometry("760x520")
        self.root.resizable(False, False)
        self.root.configure(bg='black')

        self.system = StudentSystem()
        self.data_manager: DataManager = self.system.data_manager
        self.current_student = None

        self.frames = {}
        self.frames["login"] = LoginFrame(root, self)
        self.frames["register"] = RegisterFrame(root, self)
        self.frames["dashboard"] = DashboardFrame(root, self)

        self.show_frame("login")

    def show_frame(self, name) -> None:
        for frame in self.frames.values():
            frame.place_forget()

        if name == "login":
            self.frames["login"].clear_fields()
        elif name == "register":
            self.frames["register"].clear_fields()
        self.frames[name].place(relx=0.5, rely=0.5, anchor="center")

    def handle_login(self, frame) -> None:
        email = frame.login_email.get().strip()
        password = frame.login_password.get()

        student = self.data_manager.find_student_by_login(email, password)
        if student is None:
            frame.login_status.config(text="Invalid email or password.")
            return

        self.current_student = student
        frame.login_status.config(text="")
        self.frames["dashboard"].refresh_dashboard(student)
        self.show_frame("dashboard")

    def handle_register(self, frame) -> None:
        name = frame.reg_name.get().strip()
        email = frame.reg_email.get().strip()
        password = frame.reg_password.get()
        confirm_password = frame.reg_confirm.get()

        if not self.system.check_valid_name_email(name, email):
            frame.register_status.config(text="Invalid name or email format.")
            return

        if self.data_manager.email_exists(email):
            frame.register_status.config(text="This email is already registered.")
            return

        if password != confirm_password:
            frame.register_status.config(text="Passwords do not match.")
            return

        if not self.system.check_valid_pwd(password):
            frame.register_status.config(text="Password must start with uppercase letters and end with at least 3 digits.")
            return

        student_id = self.data_manager.generate_student_id()
        new_student = Student(student_id, name, email, password)
        self.data_manager.add_student(new_student)
        self.current_student = new_student

        frame.register_status.config(text="")
        frame.clear_fields()
        self.frames["dashboard"].refresh_dashboard(new_student)
        mb.showinfo("Registration Successful", f"Student registered successfully. Your student ID is {student_id}.")
        self.show_frame("dashboard")

    def generate_subject_id(self) -> str:
        existing_ids = {subject.subjectId for subject in self.current_student.subjects}
        while True:
            new_id = str(random.randint(1, 999)).zfill(3)
            if new_id not in existing_ids:
                return new_id

    def handle_enrol(self, frame) -> None:
        if self.current_student is None:
            return

        if len(self.current_student.subjects) >= 4:
            mb.showwarning("Limit Reached", "You can only enrol in up to four subjects.")
            return

        subject_id = self.generate_subject_id()
        mark = random.randint(25, 100)
        new_subject = Subject(subject_id, mark)
        self.current_student.subjects.append(new_subject)
        self.data_manager.update_student(self.current_student)
        frame.refresh_dashboard(self.current_student)
        mb.showinfo("Subject Enrolled", f"Subject {subject_id} enrolled. Mark: {mark}, Grade: {new_subject.grade}")

    def handle_remove_subject(self, frame) -> None:
        selected = frame.subject_tree.selection()
        if not selected:
            mb.showwarning("Select Subject", "Please select a subject to remove.")
            return

        subject_id = frame.subject_tree.item(selected[0], "values")[0]
        self.current_student.subjects = [s for s in self.current_student.subjects if s.subjectId != subject_id]
        self.data_manager.update_student(self.current_student)
        frame.refresh_dashboard(self.current_student)
        mb.showinfo("Removed", f"Subject {subject_id} removed.")

    def handle_change_password(self, frame) -> None:
        if self.current_student is None:
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

        if not self.system.check_valid_pwd(new_password):
            mb.showwarning(
                "Invalid Password",
                "Password must start with an uppercase letter, contain at least five letters, and end with at least three digits.",
            )
            return

        self.current_student.password = new_password
        self.data_manager.update_student(self.current_student)
        mb.showinfo("Password Updated", "Your password has been updated.")

    def handle_logout(self, frame) -> None:
        self.current_student = None
        self.show_frame("login")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()
