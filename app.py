from tkinter import *
from tkinter import ttk

#individual class gpa
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

#cumulative credit hours earned
def getEarned(classes):
    earned = 0
    for i in range(len(classes)):
        earned += classes[i].earnedCreditHours()
    return earned

#cumulative credit hours taken
def getTotal(classes):
    total = 0
    for i in range(len(classes)):
        total += classes[i].totalCreditHours()
    return total

#hardcoded classes
yr1sem1 = [gpa(3, 'A-'), gpa(3, 'B'),gpa(3, 'C'), gpa(3, 'A'), gpa(3, 'A')]
thisSem = [gpa(3, 'A-'), gpa(3, 'B'),gpa(3, 'C'), gpa(3, 'A'), gpa(3, 'A')]
#this is for when there are more semesters added
classes = yr1sem1

#colors
blue = '#cbe6fa'
pink = '#ffd2cf'

#GUI setup
window = Tk()
window.title('GPA Calculator')

#creates tabs
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

#creates labels
lbl = Label(tab1, text='hello!', font=('Arial Bold', 20), bg=blue)
lbl2 = Label(tab2, text='', font=('Arial Bold', 20), bg=blue)

#displays how GPA will be affected by this semester's classes
tabControl.add(tab1, text="TestGPA")
#displays cumulative GPA
tabControl.add(tab2, text="Cumulative")

#Styles tabs
style = ttk.Style()
style.theme_create("soft", parent="alt", settings={
    ".":{ #"." - styles the background of the tabs
        "configure": {"background": blue}
    },
    "TNotebook":{ #TNotebook - color behind the Notebook
        "configure": {"background": pink}
    },
    "TNotebook.Tab":{ #TNotebook.tab - color of non-selected tab-button
        "configure": {"padding":[7,2], "background": blue},
        "map":       {"background": [("selected", blue)],}
    }
})
style.theme_use("soft")
#tab1 - TestGPA
tabControl.pack()
select1 = IntVar()
select2 = IntVar()
select3 = IntVar()
select4 = IntVar()
select5 = IntVar()
def clicked():
    #calculates current earned and total credit hours
    earn = getEarned(classes)
    total = getTotal(classes)

    #calculates current course(s) current and total credit hours
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

    #sets the label
    if total != 0:
        res = str(round(earn / total,2))
    else:
        res = 0.0
    lbl.configure(text= res)

#check boxes to select which classes to compare
check1 = Checkbutton(tab1, text='Class1', var=select1, onvalue=float("1"), offvalue=float("0"), bg=blue)
check2 = Checkbutton(tab1, text='Class2', var=select2, onvalue=float("1"), offvalue=float("0"), bg=blue)
check3 = Checkbutton(tab1, text='Class3', var=select3, onvalue=float("1"), offvalue=float("0"), bg=blue)
check4 = Checkbutton(tab1, text='Class4', var=select4, onvalue=float("1"), offvalue=float("0"), bg=blue)
check5 = Checkbutton(tab1, text='Class5', var=select5, onvalue=float("1"), offvalue=float("0"), bg=blue)
btn = Button(tab1, text="Click to Calculate GPA", command=clicked, bg=pink)

#displays on GUI for tab1
lbl.pack(padx=30,pady=10)
check1.pack()
check2.pack()
check3.pack()
check4.pack()
check5.pack()
btn.pack(padx=60,pady=20)

#tab2 - Cumulative gpa
def selected():
    lbl2.configure(text=str(round(getEarned(classes) / getTotal(classes),2)))
btn2 = Button(tab2, text="Current Cumulative GPA", command=selected, bg=pink)

#displays on GUI for tab2
lbl2.pack(padx=30,pady=30)
btn2.pack(padx=60,pady=0)

#Sets window to appear in center of screen
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x,y))
#window['bg'] = '#cbe6fa'
window.mainloop()
