class LoginController:
    def __init__(self, app):
        self.app = app

    def showFrame(self, name):
        self.app.showFrame(name)

    def handleLogin(self, frame):

        print("LoginController: handleLogin called")
        print(frame)
        email = frame.emailText.get().strip()
        password = frame.passwordText.get()

        student = self.app.dataManager.findStudentByLogin(email, password)
        if student is None:
            frame.statusText.config(text="Invalid email or password")
            return

        self.app.currentStudent = student
        frame.statusText.config(text="")
        self.app.frames["dashboard"].refreshDashboard(student)
        self.app.showFrame("dashboard")
