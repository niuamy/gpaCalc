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
tab0 = ttk.Frame(tabControl)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

#creates labels
lbl = Label(tab1, text='hello!', font=('Arial Bold', 20), bg=blue)

#Open file/Add new file
tabControl.add(tab0, text="file")
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

#tab0
tabControl.pack()
def newFile():
    fileName = input("Enter file name: ")
    out = open(fileName, "w")
    grade = input("Enter your grade (enter twice to finish): ")
    while(len(grade) > 0):
        out.write(grade)
        out.write("\n")
        grade = input("Enter your grade (enter twice to finish): ")
    out.close()

def oldFile():
    fileName = input("Enter file name: ")
    read = open(fileName, "r")


newFileBtn = Button(tab0, text="New File", width=10, command=newFile, bg=pink)
existingFileBtn = Button(tab0, text="Existing File", width=10, command=oldFile, bg=pink)

newFileBtn.place(x=82, y=70)
existingFileBtn.place(x=82, y=120)



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
score1 = StringVar()
weight1 = StringVar()
score2 = StringVar()
weight2 = StringVar()
score3 = StringVar()
weight3 = StringVar()
score4 = StringVar()
weight4 = StringVar()
score5 = StringVar()
weight5 = StringVar()

#labels
lbl2 = Label(tab2, text='Score', font=('Arial Bold', 10), bg=blue)
lbl3 = Label(tab2, text='  Weight', font=('Arial Bold', 10), bg=blue)
lbl4 = Label(tab2, text='Score', font=('Arial Bold', 10), bg=blue)
lbl5 = Label(tab2, text='  Weight', font=('Arial Bold', 10), bg=blue)
lbl6 = Label(tab2, text='Score', font=('Arial Bold', 10), bg=blue)
lbl7 = Label(tab2, text='  Weight', font=('Arial Bold', 10), bg=blue)
lbl8 = Label(tab2, text='Score', font=('Arial Bold', 10), bg=blue)
lbl9 = Label(tab2, text='  Weight', font=('Arial Bold', 10), bg=blue)
lbl10 = Label(tab2, text='Score', font=('Arial Bold', 10), bg=blue)
lbl11 = Label(tab2, text='  Weight', font=('Arial Bold', 10), bg=blue)
lbl12 = Label(tab2, text='Total:', font=('Arial Bold', 10), bg=blue)
lbl13 = Label(tab2, text='', font=('Arial Bold', 10), bg=blue)

#calculates total score in one course
def selected():
    #lbl2.configure(text=str(round(getEarned(classes) / getTotal(classes),2)))
    group1 = 0
    group2 = 0
    group3 = 0
    group4 = 0
    group5 = 0
    if len(score1.get()) != 0 and len(weight1.get()) != 0:
        group1 = float(score1.get())*float(weight1.get())/100
    if len(score2.get()) != 0 and len(weight2.get()) != 0:
        group2 = float(score2.get())*float(weight2.get())/100
    if len(score3.get()) != 0 and len(weight3.get()) != 0:
        group3 = float(score3.get())*float(weight3.get())/100
    if len(score4.get()) != 0 and len(weight4.get()) != 0:
        group4 = float(score4.get())*float(weight4.get())/100
    if len(score5.get()) != 0 and len(weight5.get()) != 0:
        group5 = float(score5.get())*float(weight5.get())/100
    total = str(round((group1 + group2 + group3 + group4 + group5),2))
    lbl13.configure(text=total)

#all entries to enter scores and weights
entry1 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=score1)
entry2 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=weight1)
entry3 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=score2)
entry4 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=weight2)
entry5 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=score3)
entry6 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=weight3)
entry7 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=score4)
entry8 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=weight4)
entry9 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=score5)
entry10 = Entry(tab2, bd = 2, width = 6, font='Arial 10', textvariable=weight5)

#calculates total
btn2 = Button(tab2, text="Calculate", command=selected, bg=pink)

#displays on GUI for tab2
lbl2.grid(row=0,column=0, padx=7)
entry1.grid(row=0,column=1)
lbl3.grid(row=0,column=2, padx=4, pady=10)
entry2.grid(row=0,column=3)

lbl4.grid(row=1,column=0, padx=7)
entry3.grid(row=1,column=1)
lbl5.grid(row=1,column=2, padx=4, pady=10)
entry4.grid(row=1,column=3)

lbl6.grid(row=2,column=0, padx=7)
entry5.grid(row=2,column=1)
lbl7.grid(row=2,column=2, padx=4, pady=10)
entry6.grid(row=2,column=3)

lbl8.grid(row=3,column=0, padx=7)
entry7.grid(row=3,column=1)
lbl9.grid(row=3,column=2, padx=4, pady=10)
entry8.grid(row=3,column=3)

lbl10.grid(row=4,column=0, padx=7)
entry9.grid(row=4,column=1)
lbl11.grid(row=4,column=2, padx=4, pady=10)
entry10.grid(row=4,column=3)

lbl12.grid(row=5,column=0, pady=5)
lbl13.grid(row=5,column=1,pady=5)
btn2.grid(row=5,column=3,pady=8)

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
