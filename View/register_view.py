import tkinter as tk


class RegisterFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        title = tk.Label(self, text="New Student Registration", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

        self.nameLabel = tk.Label(self, text="Name:", anchor="w", width=16, fg='white', bg='black')
        self.nameLabel.grid(row=1, column=0, sticky="w")
        self.nameText = tk.StringVar()
        self.nameText.trace_add("write", self._onNameChange)
        self.nameField = tk.Entry(self, textvariable=self.nameText, fg="black", bg="white", width=40)
        self.nameField.grid(row=1, column=1, pady=6)
        self.nameField.focus()

        self.nameWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.nameWarning.grid(row=2, column=1, sticky="w")

        self.emailLabel = tk.Label(self, text="Email:", anchor="w", width=16, fg='white', bg='black')
        self.emailLabel.grid(row=3, column=0, sticky="w")
        self.emailText = tk.StringVar()
        self.emailText.trace_add("write", self._onEmailChange)
        self.emailField = tk.Entry(self, textvariable=self.emailText, fg="black", bg="white", width=40)
        self.emailField.grid(row=3, column=1, pady=6)
        self.emailRules = tk.Label(
            self,
            text='Format: firstname.lastname@university.com\ne.g. John Smith → john.smith@university.com',
            anchor="w",
            font=("Arial", 10),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )
        self.emailRules.grid(row=4, column=1, columnspan=2, sticky="w")

        self.emailWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.emailWarning.grid(row=5, column=1, sticky="w")

        self.passwordLabel = tk.Label(self, text="Password:", anchor="w", width=16, fg='white', bg='black')
        self.passwordLabel.grid(row=6, column=0, sticky="w")
        self.passwordText = tk.StringVar()
        self.passwordText.trace_add("write", self._onPasswordChange)
        self.passwordField = tk.Entry(self, textvariable=self.passwordText, fg="black", bg="white", width=40, show="*", bd=2)
        self.passwordField.grid(row=6, column=1, pady=6)
        self.passwordRules = tk.Label(
            self,
            text='1. Start with an uppercase letter\n2. Have at least 5 letters\n3. Have 3 or more digits at the end\ne.g. Password123',
            anchor="w",
            font=("Arial", 10),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )
        self.passwordRules.grid(row=7, column=1, columnspan=2, sticky="w")

        self.passwordWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.passwordWarning.grid(row=8, column=1, sticky="w")

        self.confirmPasswordLabel = tk.Label(self, text="Confirm Password:", anchor="w", width=16, fg='white', bg='black')
        self.confirmPasswordLabel.grid(row=9, column=0, sticky="w")
        self.confirmPasswordText = tk.StringVar()
        self.confirmPasswordText.trace_add("write", self._onConfirmPasswordChange)
        self.confirmPasswordField = tk.Entry(self, textvariable=self.confirmPasswordText, fg="black", bg="white", width=40, show="*", bd=2)
        self.confirmPasswordField.grid(row=9, column=1, pady=6)

        self.confirmWarning = tk.Label(self, text="", anchor="w", font=("Arial", 9), fg='red', bg='black')
        self.confirmWarning.grid(row=10, column=1, sticky="w")

        self.registerStatus = tk.Label(self, text="", fg="red", bg='black')
        self.registerStatus.grid(row=11, column=0, columnspan=2, pady=(10, 0), sticky="w")

        buttonFrame = tk.Frame(self, bg='black')
        tk.Button(buttonFrame, text="Cancel", width=14, command=lambda: controller.showFrame("login")).pack(side="left", padx=10)
        tk.Button(buttonFrame, text="Register", width=14, command=lambda: controller.handleRegister(self)).pack(side="left")
        buttonFrame.grid(row=12, column=0, columnspan=2, pady=20)

    def _onNameChange(self, *args):
        name = self.nameText.get().strip()
        if name and len(name.split()) != 2:
            self.nameWarning.config(text="Please enter first name and last name.")
        else:
            self.nameWarning.config(text="")
        self.registerStatus.config(text="")

    def _onEmailChange(self, *args):
        email = self.emailText.get()
        name = self.nameText.get().strip()
        if ' ' in email:
            self.emailWarning.config(text="Email cannot contain spaces.")
        elif email and not email.endswith("@university.com"):
            self.emailWarning.config(text='Email must end with "@university.com"')
        elif email and len(name.split()) == 2:
            first, last = name.split()
            expected = f"{first.lower()}.{last.lower()}@university.com"
            if email.lower() != expected:
                self.emailWarning.config(text="Email should match the entered name.")
            else:
                self.emailWarning.config(text="")
        else:
            self.emailWarning.config(text="")
        self.registerStatus.config(text="")

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
        self._onConfirmPasswordChange()
        self.registerStatus.config(text="")

    def _onConfirmPasswordChange(self, *args):
        password = self.passwordText.get()
        confirm = self.confirmPasswordText.get()
        if confirm and password != confirm:
            self.confirmWarning.config(text="Passwords do not match.")
        else:
            self.confirmWarning.config(text="")

    def clearFields(self) -> None:
        self.nameField.delete(0, tk.END)
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)
        self.confirmPasswordField.delete(0, tk.END)
        self.registerStatus.config(text="")
        self.nameWarning.config(text="")
        self.emailWarning.config(text="")
        self.passwordWarning.config(text="")
        self.confirmWarning.config(text="")
