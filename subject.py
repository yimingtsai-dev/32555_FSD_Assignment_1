class Subject:
    def __init__(self, subjectId, mark):
        self.subjectId = subjectId
        self.mark = mark
        self.grade = self.calculateGrade()

    def calculateGrade(self):
        if self.mark < 50:
            return "Z"
        elif 50 <= self.mark < 65:
            return "P"
        elif 65 <= self.mark < 75:
            return "C"
        elif 75 <= self.mark < 85:
            return "D"
        else:
            return "HD"
        
