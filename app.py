
class gpa:
    def __init__(self, creditHours, grade):
        self.creditHours = creditHours
        self.grade = grade

    def earnedCreditHours(self):
        gradeConversion = 0

        if self.grade == 'A':
            gradeConversion = 4.0
        elif self.grade == 'A-':
            gradeConversion = 3.7
        elif self.grade == 'B+':
            gradeConversion = 3.3
        elif self.grade == 'B':
            gradeConversion = 3.0
        elif self.grade == 'B-':
            gradeConversion = 2.7
        elif self.grade == 'C+':
            gradeConversion = 2.3
        elif self.grade == 'C':
            gradeConversion = 2.0
        elif self.grade == 'C-':
            gradeConversion = 1.7
        else:
            gradeConversion = 0

        return gradeConversion * self.creditHours

    def totalCreditHours(self):
        return self.creditHours

def getEarned(classes):
    earned = 0
    for i in range(len(classes)):
        earned += classes[i].earnedCreditHours()
    return earned

def getTotal(classes):
    total = 0
    for i in range(len(classes)):
        total += classes[i].totalCreditHours()
    return total

def year1sem1():
    classes = [gpa(4, 'A-'), gpa(4, 'A'),gpa(3, 'B'), gpa(3, 'B+'), gpa(3, 'A')]
    earned = getEarned(classes)
    total = getTotal(classes)
    return earned/total




print(year1sem1())