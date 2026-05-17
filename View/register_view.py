import tkinter as tk


class RegisterFrame(tk.Frame):
    def __init__(self, master, controller) -> None:
        super().__init__(master, padx=20, pady=20, bg='black')

        title = tk.Label(self, text="New Student Registration", font=("Arial", 20, "bold"), fg='white', bg='black')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")

        # Name, email, password, confirm password fields with validation rules displayed underneath each field

        self.nameLabel = tk.Label(self, text="Name:", anchor="w", width=16, bg='black')
        self.nameLabel.grid(row=1, column=0, sticky="w")
        self.nameText = tk.StringVar()
        self.nameField = tk.Entry(self, textvariable=self.nameText, fg="white", width=40)
        self.nameField.grid(row=1, column=1, pady=6)
        self.nameField.focus()

        self.emailLabel = tk.Label(self, text="Email:", anchor="w", width=16, bg='black')
        self.emailLabel.grid(row=2, column=0, sticky="w")
        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(self, textvariable=self.emailText, fg="white", width=40)
        self.emailField.grid(row=2, column=1, pady=6)
        self.emailRules = tk.Label(
            self,
            text='Emails must end with "@university.com"',
            anchor="w",
            font=("Arial", 10),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )

        self.emailRules.grid(row=3, column=1, columnspan=2, sticky="w")

        self.passwordLabel = tk.Label(self, text="Password:", anchor="w", width=16, bg='black')
        self.passwordLabel.grid(row=4, column=0, sticky="w")
        self.passwordText = tk.StringVar()
        self.passwordField = tk.Entry(self, textvariable=self.passwordText, fg="white", width=40, show="*", bd=2)
        self.passwordField.grid(row=4, column=1, pady=6)
        self.passwordRules = tk.Label(
            self,
            text='1. Start with an uppercase letter \n2. Have at least 5 letters \n3. Have 3 or more digits.',
            anchor="w",
            font=("Arial", 10),
            fg='yellow',
            bg='black',
            wraplength=360,
            justify="left"
        )
        self.passwordRules.grid(row=5, column=1, columnspan=2, sticky="w")


        self.confirmPasswordLabel = tk.Label(self, text="Confirm password:", anchor="w", width=16, bg='black')
        self.confirmPasswordLabel.grid(row=6, column=0, sticky="w")
        self.confirmPasswordText = tk.StringVar()
        self.confirmPasswordField = tk.Entry(self, textvariable=self.confirmPasswordText, fg="white", width=40, show="*", bd=2)
        self.confirmPasswordField.grid(row=6, column=1, pady=6)

        self.registerStatus = tk.Label(self, text="", fg="red", bg='black')
        self.registerStatus.grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="w")

        buttonFrame = tk.Frame(self, bg='black')
        tk.Button(buttonFrame, text="Cancel", width=14, command=lambda: controller.showFrame("login")).pack(side="left", padx=10)
        tk.Button(buttonFrame, text="Register", width=14, command=lambda: controller.handleRegister(self)).pack(side="left")
        buttonFrame.grid(row=8, column=0, columnspan=2, pady=20)

    def clearFields(self) -> None:
        self.nameField.delete(0, tk.END)
        self.emailField.delete(0, tk.END)
        self.passwordField.delete(0, tk.END)
        self.confirmPasswordField.delete(0, tk.END)
        self.registerStatus.config(text="")
