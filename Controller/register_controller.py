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

        if not self.app.system.checkValidNameEmail(name, email):
            frame.registerStatus.config(text="Invalid name or email format.")
            return

        if self.app.dataManager.emailExists(email):
            frame.registerStatus.config(text="This email is already registered.")
            return

        if password != confirm_password:
            frame.registerStatus.config(text="Passwords do not match.")
            return

        if not self.app.system.checkValidPwd(password):
            frame.registerStatus.config(text="Password must start with uppercase letters and end with at least 3 digits.")
            return

        student_id = self.app.dataManager.generateStudentId()
        new_student = Student(student_id, name, email, password)
        self.app.dataManager.addStudent(new_student)
        self.app.currentStudent = new_student

        frame.registerStatus.config(text="")
        frame.clearFields()
        self.app.frames["dashboard"].refreshDashboard(new_student)
        self.app.showFrame("dashboard")
