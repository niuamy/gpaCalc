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


yr1sem1 = [gpa(3, 'A'), gpa(3, 'A'),gpa(3, 'A'), gpa(3, 'A'), gpa(3, 'A')]


def cumulativeGPA():
    classes = yr1sem1
    return getEarned(classes) / getTotal(classes)

window = Tk()
window.title('GPA Calculator')
lbl = Label(window, text='hello!', font=('Arial Bold', 20))
def clicked():
    res = str(round(cumulativeGPA(),2))
    lbl.configure(text= res)
btn = Button(window, text="Click to Calculate GPA", command=clicked)
lbl.pack(padx=20,pady=10)
btn.pack(padx=30,pady=20)
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x,y))
window.mainloop()
