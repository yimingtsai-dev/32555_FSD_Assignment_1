import tkinter as tk


class LoginFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        title = tk.Label(self, text="Student Login", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 16), sticky="ew")

        self.emailLabel = tk.Label(self, text="Email:", anchor="w", width=16, fg='white', bg='black')
        self.emailLabel.grid(row=1, column=0, sticky="w")

        self.emailText = tk.StringVar()
        self.emailText.trace_add("write", self._onEmailChange)
        self.emailField = tk.Entry(self, textvariable=self.emailText, fg="black", bg="white", width=40)
        self.emailField.grid(row=1, column=1, pady=6, sticky="ew")
        self.grid_columnconfigure(1, weight=1)

        self.emailHint = tk.Label(
            self,
            text='Format: firstname.lastname@university.com\ne.g. John Smith → john.smith@university.com',
            anchor="w",
            font=("Arial", 9),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )
        self.emailHint.grid(row=2, column=1, sticky="w", pady=(0, 4))

        self.emailWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.emailWarning.grid(row=3, column=1, sticky="w")

        self.passwordLabel = tk.Label(self, text="Password:", anchor="w", width=16, fg='white', bg='black')
        self.passwordLabel.grid(row=4, column=0, sticky="w")

        self.passwordText = tk.StringVar()
        self.passwordText.trace_add("write", self._onPasswordChange)
        self.passwordField = tk.Entry(self, textvariable=self.passwordText, show="*", fg="black", bg="white", width=40)
        self.passwordField.grid(row=4, column=1, pady=6)

        self.passwordHint = tk.Label(
            self,
            text='1. Start with an uppercase letter\n2. Have at least 5 letters\n3. Have 3 or more digits at the end\ne.g. Password123',
            anchor="w",
            font=("Arial", 9),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )
        self.passwordHint.grid(row=5, column=1, sticky="w", pady=(0, 4))

        self.passwordWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.passwordWarning.grid(row=6, column=1, sticky="w")

        self.statusText = tk.Label(self, text="", fg="red", bg='black', font=("Arial", 9))
        self.statusText.grid(row=7, column=0, columnspan=2, pady=(4, 0), sticky="w")

        self.loginBtn = tk.Button(self, text="Login", width=14, command=lambda: controller.handleLogin(self))
        self.loginBtn.grid(column=0, row=8, sticky="W", padx=5, pady=8)
        self.registerBtn = tk.Button(self, text="Register", width=14, command=lambda: controller.showFrame("register"))
        self.registerBtn.grid(column=1, row=8, sticky="E", padx=5, pady=8)

    def _onEmailChange(self, *args):
        email = self.emailText.get()
        if " " in email:
            self.emailWarning.config(text="Email cannot contain spaces.")
        elif email and not email.endswith("@university.com"):
            self.emailWarning.config(text='Email must end with "@university.com"')
        else:
            self.emailWarning.config(text="")
        self.statusText.config(text="")

    def _onPasswordChange(self, *args):
        password = self.passwordText.get()
        if password and not password[0].isupper():
            self.passwordWarning.config(text="Password must start with an uppercase letter.")
        elif password and len(password) < 8:
            self.passwordWarning.config(text="Password must include at least 5 letters and 3 digits.")
        elif password and not password[-3:].isdigit():
            self.passwordWarning.config(text="Password must end with 3 or more digits.")
        else:
            self.passwordWarning.config(text="")
        self.statusText.config(text="")

    def clearFields(self) -> None:
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)
        self.statusText.config(text="")
        self.emailWarning.config(text="")
        self.passwordWarning.config(text="")
