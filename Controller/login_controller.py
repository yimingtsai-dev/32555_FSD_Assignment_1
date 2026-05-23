class LoginController:
    def __init__(self, app):
        self.app = app

    def showFrame(self, name):
        self.app.showFrame(name)

    def handleLogin(self, frame):
        email = frame.emailText.get().strip()
        password = frame.passwordText.get()

        if email == "" or password == "":
            frame.statusText.config(text="Please enter both email and password.")
            return

        if not self.app.system._validateEmail(email):
            frame.statusText.config(text="Invalid email format. Use firstname.lastname@university.com.")
            return

        if not self.app.system.checkValidPwd(password):
            frame.statusText.config(text="Invalid password format. Use uppercase letter, at least 5 letters, then 3 or more digits.")
            return

        student = self.app.dataManager.findStudentByLogin(email, password)
        if student is None:
            frame.statusText.config(text="Student does not exist or password is incorrect.")
            return

        self.app.currentStudent = student
        frame.statusText.config(text="")
        frame.clearFields()
        self.app.frames["dashboard"].refreshDashboard(student)
        self.app.showFrame("dashboard")
