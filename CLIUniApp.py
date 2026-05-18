from admin_system import AdminSystem
from View.student_system_view import StudentSystemView
import tkinter as tk
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        ip = input("University System: (A)dmin, (S)tudent, or X : ").strip()

        if ip.upper() == "A":
            asys = AdminSystem()
            asys.run()
        elif ip.upper() == "S":
            root = tk.Tk()
            StudentSystemView(root)
            root.mainloop()
        elif ip.upper() == "X":
            print("Thank You")
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()
