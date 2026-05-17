import tkinter as tk


class LoginFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        title = tk.Label(self, text="Student Login", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

        self.emailLabel = tk.Label(self, text="Email:", anchor="w", width=16, fg='white', bg='black')
        self.emailLabel.grid(row=1, column=0, sticky="w")

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(self, textvariable=self.emailText, fg="white", width=40)
        self.emailField.grid(row=1, column=1, pady=6, sticky="ew")
        self.grid_columnconfigure(1, weight=1)

        self.passwordLabel = tk.Label(self, text="Password:", anchor="w", width=16, fg='white', bg='black')
        self.passwordLabel.grid(row=2, column=0, sticky="w")
        
        self.passwordText = tk.StringVar()
        self.passwordField = tk.Entry(self,textvariable=self.passwordText,show="*", width=40)
        self.passwordField.grid(row=2, column=1, pady=6)


        self.statusText = tk.Label(self, text="", fg="red", bg='black')
        self.statusText.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="w")

        self.loginBtn = tk.Button(self,text="Login",width=14,command=lambda: controller.handleLogin(self))
        self.loginBtn.grid(column=0,row=4,sticky="W",padx=5,pady=5)
        self.registerBtn = tk.Button(self,text="Register",width=14,command=lambda: controller.showFrame("register"))
        self.registerBtn.grid(column=1,row=4,sticky="E",padx=5,pady=5)



    def clearFields(self) -> None:
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)
        self.statusText.config(text="")

