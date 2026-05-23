from Model.student import Student


class RegisterController:
    def __init__(self, app):
        self.app = app

    def showFrame(self, name):
        self.app.showFrame(name)

    def handleRegister(self, frame):
        name = frame.nameText.get().strip()
        email = frame.emailText.get().strip()
        password = frame.passwordText.get()
        confirm_password = frame.confirmPasswordText.get()

        if name == "" or email == "" or password == "" or confirm_password == "":
            frame.registerStatus.config(text="Please complete all fields.")
            return

        name_parts = name.split()
        if len(name_parts) != 2:
            frame.registerStatus.config(text="Please enter first name and last name, for example John Smith.")
            return

        if not self.app.system._validateEmail(email):
            frame.registerStatus.config(text="Invalid email format. Use firstname.lastname@university.com.")
            return

        if not self.app.system.checkValidNameEmail(name, email):
            frame.registerStatus.config(text="Email must match the entered first and last name.")
            return

        if self.app.dataManager.emailExists(email):
            frame.registerStatus.config(text="This email is already registered.")
            return

        if not self.app.system.checkValidPwd(password):
            frame.registerStatus.config(text="Invalid password format. Use uppercase letter, at least 5 letters, then 3 or more digits.")
            return

        if password != confirm_password:
            frame.registerStatus.config(text="Passwords do not match.")
            return

        student_id = self.app.dataManager.generateStudentId()
        new_student = Student(student_id, name, email, password)
        self.app.dataManager.addStudent(new_student)
        self.app.currentStudent = new_student

        frame.registerStatus.config(text="")
        frame.clearFields()
        self.app.frames["dashboard"].refreshDashboard(new_student)
        self.app.showFrame("dashboard")
