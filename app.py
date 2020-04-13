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

#hardcoded classes
yr1sem1 = [gpa(4, 'A-'), gpa(4, 'B'),gpa(3, 'A'), gpa(2, 'A'), gpa(1, 'A')]

def cumulativeGPA():
    classes = yr0 + yr1sem1
    return getEarned(classes) / getTotal(classes)

#GUI setup
window = Tk()
window.title('GPA Calculator')
lbl = Label(window, text='hello!', font=('Arial Bold', 20), bg="#cbe6fa")

select1 = IntVar()
select2 = IntVar()
select3 = IntVar()
select4 = IntVar()
select5 = IntVar()
def clicked():
    earn = 0
    total = 0
    if select1.get() == 1:
        earn+=yr1sem1[0].earnedCreditHours()
        total+=yr1sem1[0].totalCreditHours()
    if select2.get() == 1:
        earn+=yr1sem1[1].earnedCreditHours()
        total+=yr1sem1[1].totalCreditHours()
    if select3.get() == 1:
        earn+=yr1sem1[2].earnedCreditHours()
        total+=yr1sem1[2].totalCreditHours()
    if select4.get() == 1:
        earn+=yr1sem1[3].earnedCreditHours()
        total+=yr1sem1[3].totalCreditHours()
    if select5.get() == 1:
        earn+=yr1sem1[4].earnedCreditHours()
        total+=yr1sem1[4].totalCreditHours()

    #res = str(round(cumulativeGPA(),2))
    if total != 0:
        res = str(round(earn / total,2))
    else:
        res = 0.0
    lbl.configure(text= res)
check1 = Checkbutton(window, text='Class1', var=select1, onvalue=float("1"), offvalue=float("0"), bg="#cbe6fa")
check2 = Checkbutton(window, text='Class2', var=select2, onvalue=float("1"), offvalue=float("0"), bg="#cbe6fa")
check3 = Checkbutton(window, text='Class3', var=select3, onvalue=float("1"), offvalue=float("0"), bg="#cbe6fa")
check4 = Checkbutton(window, text='Class4', var=select4, onvalue=float("1"), offvalue=float("0"), bg="#cbe6fa")
check5 = Checkbutton(window, text='Class5', var=select5, onvalue=float("1"), offvalue=float("0"), bg="#cbe6fa")
btn = Button(window, text="Click to Calculate GPA", command=clicked, bg="#ffd2cf")

#displays on GUI
lbl.pack(padx=30,pady=10)
check1.pack()
check2.pack()
check3.pack()
check4.pack()
check5.pack()
btn.pack(padx=40,pady=20)

#Sets window to appear in center of screen
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x,y))
window['bg'] = '#cbe6fa'
window.mainloop()
