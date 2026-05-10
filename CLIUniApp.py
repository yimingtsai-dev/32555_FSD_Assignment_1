from student_system import StudentSystem
import os
def main():
    while True:
        os.system("cls")
        print("Welcome To UniApp CLI version! Select your subsystem")
        print("1: Login as student")
        print("2: Login as admin")
        print("3: Exit system")

        ip = input("Enter your option: ")

        if ip == "1":
            os.system("cls")
            ss = StudentSystem()
            ss.run()
        elif ip == "2":
            os.system("cls")
            # Admin system is not implemented, so we just print a message and return to the main menu
            break
        elif ip == "3":
            print("System out!")
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()