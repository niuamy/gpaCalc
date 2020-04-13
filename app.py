from tkinter import *

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

yr0 = [gpa(4,'A'),gpa(3,'A'),gpa(3,'A')]
yr1sem1 = [gpa(4, 'A-'), gpa(4, 'B+'),gpa(3, 'A'), gpa(2, 'A'), gpa(1, 'A')]
yr1sem2 = [gpa(4, 'A'), gpa(3,'A'), gpa(3,'A'),gpa(2,'A')]

def cumulativeGPA():
    classes = yr0 + yr1sem1 + yr1sem2
    return getEarned(classes) / getTotal(classes)

m = Tk()
m.title('GPA Calculator')
w = Label(m, text=str(round(cumulativeGPA(),2)))
w.pack()
m.mainloop()
