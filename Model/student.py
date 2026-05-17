class Student:
    def __init__(self, student_id, name, email, password):
        self.id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def addSubject(self, subject):
        self.subjects.append(subject)

    def removeSubject(self, subject_id):
        for subject in self.subjects:
            if subject.subjectId == subject_id:
                self.subjects.remove(subject)
                break

    def updatePassword(self, newPwd):
        self.password = newPwd

    def viewEnrollmentList(self):
        for subject in self.subjects:
            print(subject.subjectId, subject.mark, subject.grade)
