from admin_system import AdminSystem
from controller import StudentGUI
import tkinter as tk

def main():
    while True:
        print("Welcome To UniApp CLI version! Select your subsystem")
        print("1: Login as student")
        print("2: Login as admin")
        print("3: Exit system")

        ip = input("Enter your option: ")

        if ip == "1":
            root = tk.Tk()
            StudentGUI(root)
            root.mainloop()
        elif ip == "2":
            asys = AdminSystem()
            asys.run()
        elif ip == "3":
            print("System out!")
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()