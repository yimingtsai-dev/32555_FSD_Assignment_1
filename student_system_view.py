from data_manager import DataManager
from student_system import StudentSystem
from login_controller import LoginController
from register_controller import RegisterController
from dashboard_controller import DashboardController
from login_view import LoginFrame
from register_view import RegisterFrame
from dashboard_view import DashboardFrame


class StudentSystemView:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("UniApp Student System")
        self.root.geometry("760x520")
        self.root.resizable(False, False)
        self.root.configure(bg='black')

        self.system = StudentSystem()
        self.dataManager: DataManager = self.system.dataManager
        self.currentStudent = None

        self.loginController = LoginController(self)
        self.registerController = RegisterController(self)
        self.dashboardController = DashboardController(self)

        self.frames = {}
        self.frames["login"] = LoginFrame(root, self.loginController)
        self.frames["register"] = RegisterFrame(root, self.registerController)
        self.frames["dashboard"] = DashboardFrame(root, self.dashboardController)

        self.frames["login"].place( anchor="center", relx=0.5, rely=0.5)

    def showFrame(self, name) -> None:
        for frame in self.frames.values():
            frame.place_forget()

        if name == "login":
            self.frames["login"].clearFields()
        elif name == "register":
            self.frames["register"].clearFields()
        self.frames[name].place( anchor="center", relx=0.5, rely=0.5)    