import tkinter as tk
from tkinter import ttk


class DashboardFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        header = tk.Frame(self, bg='black', pady=10)
        self.welcomeLabel = tk.Label(header, text="Welcome", font=("Arial", 18, "bold"), fg='white', bg='black')
        self.welcomeLabel.pack(side="left", padx=20)
        self.studentInfoLabel = tk.Label(header, text="", font=("Arial", 18), fg='white', bg='black')
        self.studentInfoLabel.pack(side="left", padx=20)
        header.pack(fill="x", pady=(10, 10))

        table_frame = tk.Frame(self, bg='black', pady=20)
        self.subjectTree = ttk.Treeview(table_frame, columns=("subject", "mark", "grade"), show="headings", height=10)
        self.subjectTree.heading("subject", text="Subject ID")
        self.subjectTree.heading("mark", text="Mark")
        self.subjectTree.heading("grade", text="Grade")
        self.subjectTree.column("subject", width=200, anchor="center")
        self.subjectTree.column("mark", width=120, anchor="center")
        self.subjectTree.column("grade", width=120, anchor="center")
        self.subjectTree.pack(side="left", fill="both", expand=True)

        self.scrollBar = ttk.Scrollbar(table_frame, orient="vertical", command=self.subjectTree.yview)
        self.subjectTree.configure(yscroll=self.scrollBar.set)
        self.scrollBar.pack(side="right", fill="y")
        table_frame.pack(fill="both", expand=True)

        self.buttonFrame = tk.Frame(self, bg='black', pady=20)
        btnEnroll = tk.Button(self.buttonFrame, text="Enrol Subject", width=16, command=lambda: controller.handleEnroll(self))
        btnRemove = tk.Button(self.buttonFrame, text="Remove Selected", width=16, command=lambda: controller.handleRemoveSubject(self))
        btnChangePassword = tk.Button(self.buttonFrame, text="Change Password", width=16, command=lambda: controller.handleChangePassword(self))
        btnLogout = tk.Button(self.buttonFrame, text="Logout", width=16, command=lambda: controller.handleLogout(self))

        btnEnroll.grid(row=0, column=0, padx=8, pady=5, sticky="ew")
        btnRemove.grid(row=0, column=1, padx=8, pady=5, sticky="ew")
        btnChangePassword.grid(row=1, column=0, padx=8, pady=5, sticky="ew")
        btnLogout.grid(row=1, column=1, padx=8, pady=5, sticky="ew")

        self.buttonFrame.grid_columnconfigure(0, weight=1)
        self.buttonFrame.grid_columnconfigure(1, weight=1)
        self.buttonFrame.pack(pady=10)

    def refreshDashboard(self, student) -> None:
        self.welcomeLabel.config(text=f"Welcome, {student.name}")
        self.studentInfoLabel.config(text=f"Student ID: {student.id}")

        for item in self.subjectTree.get_children():
            self.subjectTree.delete(item)

        for subject in student.subjects:
            self.subjectTree.insert("", tk.END, values=(subject.subjectId, subject.mark, subject.grade))
