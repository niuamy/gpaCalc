from tkinter import *
from tkinter import ttk

#Add styling
class colors:   
    blue = '#cbe6fa'
    pink = '#ffd2cf'

#individual class gpa
class gpa:
    def __init__(self, creditHours, grade):
        self.creditHours = float(creditHours)
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

#GUI
def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root, width=200, height=150, bg=colors.blue)
f2 = Frame(root, bg=colors.blue)
f3 = Frame(root, bg=colors.blue)
f4 = Frame(root, bg=colors.blue)
f5 = Frame(root, bg=colors.blue)
f6 = Frame(root, bg=colors.blue)
f7 = Frame(root, bg=colors.blue)

for frame in (f1, f2, f3, f4, f5, f6, f7):
    frame.grid(row=0, column=0, sticky='news')

#Variables
fileName = StringVar()

#Start Page
newFile = Button(f1, text='New File', width=18, command=lambda:raise_frame(f2), bg=colors.pink)
oldFile = Button(f1, text='Existing File', width=18, command=lambda:raise_frame(f4), bg=colors.pink)
courseGrade = Button(f1, text='Calculate Course Grade', width=18, command=lambda:[clear(),createCourseGradePage(),raise_frame(f7)], bg=colors.pink)
newFile.config(font=('Arial', 11))
oldFile.config(font=('Arial', 11))
courseGrade.config(font=('Arial',11))
newFile.pack(padx=30, pady=(50,20))
oldFile.pack()
courseGrade.pack(pady=(20,0))

#New file: get new file name
newFileLbl = Label(f2, text='Please Enter File Name', bg=colors.blue, font=('Arial', 13))
newFileEntry = Entry(f2, bd = 2, width = 20, font='Arial 11', textvariable=fileName)
submitNew = Button(f2, text="Submit", width=22, bg=colors.pink, command=lambda:[clear(),createNewFilePage(),raise_frame(f3)])
backNew = Button(f2, text='Back', width=22, bg=colors.pink, command=lambda:raise_frame(f1))
newFileLbl.pack(pady=(40,25), padx=90)
newFileEntry.pack(pady=(0,25))
submitNew.pack(pady=(0,10))
backNew.pack(pady=(0,80))

#Existing file: get file name
oldFileLbl = Label(f4, text='Please Enter File Name', bg=colors.blue, font=('Arial', 13))
oldFileEntry = Entry(f4, bd = 2, width = 20, font='Arial 11', textvariable=fileName)
submitOld = Button(f4, text="Submit", width=22, bg=colors.pink, command=lambda:[readFile(), getCumulativeGPA(), raise_frame(f5)])
backOld = Button(f4, text='Back', width=22, bg=colors.pink, command=lambda:raise_frame(f1))
oldFileLbl.pack(pady=(40,25), padx=90)
oldFileEntry.pack(pady=(0,25))
submitOld.pack(pady=(0,10))
backOld.pack(pady=(0,80))

def clear():
    row.count = 0
    row.items.clear()
    grade.scores.clear()
    grade.weights.clear()

#New file: get new file content
class row:
    count = 0
    items = []

class grade:
    scores = []
    weights = []
    gpaList = []
    cumulative = 0
    testGPA = 0

#Add score and weight entry
def getEntry(page):
    score = StringVar()
    weight = IntVar()
    scoreLabel = Label(page, text='Grade', font=('Arial Bold', 10), bg=colors.blue)
    weightLabel = Label(page, text='Weight', font=('Arial Bold', 10), bg=colors.blue)
    scoreEntry = Entry(page, bd = 2, width = 6, font='Arial 10', textvariable=score)
    weightEntry = Entry(page, bd = 2, width = 6, font='Arial 10', textvariable=weight)
    scoreLabel.grid(row=row.count,column=0, padx=7)
    scoreEntry.grid(row=row.count,column=1)
    weightLabel.grid(row=row.count,column=2, padx=(8,4), pady=10)
    weightEntry.grid(row=row.count,column=3)
    rows = [scoreLabel, weightLabel, scoreEntry, weightEntry]
    row.items.append(rows)
    grade.scores.append(scoreEntry)
    grade.weights.append(weightEntry)
    row.count += 1

#Removes the last score and weight entry
def removeEntry():
    lastItem = len(row.items) - 1
    for i in row.items[lastItem]:
        i.destroy()
    row.items.pop(lastItem)
    grade.scores.pop(lastItem)
    grade.weights.pop(lastItem)
    row.count -= 1

#Creates a new file with the scores and weights
def createFile():
    if (fileName.get() != ""):
        out = open("files/" + fileName.get(), "a")
        for i in range(len(grade.scores)):
            out.write(grade.scores[i].get())
            out.write(grade.weights[i].get())
            out.write("\n")
        out.close()

#Reads a file that contains the scores and weights
def readFile():
    grade.gpaList.clear()
    if (fileName.get() != ""):
        text = open("files/" + fileName.get(), "r")
        for line in text:
            grades = line[:len(line) - 2]
            weights = line[len(line) - 2:]
            grade.gpaList.append(gpa(weights,grades))
        text.close() 

#Gets and displays cumulative GPA
def getCumulativeGPA():
    if (getTotal(grade.gpaList) != 0):
        cumulativeGPA.config(text=str(round(getEarned(grade.gpaList)/getTotal(grade.gpaList),2)))

#Gets and displays test cumulative GPA
def getTestGPA():
    testGPA = grade.gpaList.copy()
    for i in range(len(grade.scores)):
        testGPA.append(gpa(grade.weights[i].get(),grade.scores[i].get()))
    grade.testGPA = str(round(getEarned(testGPA)/getTotal(testGPA),2))
    return grade.testGPA
    
#Sets up window for content retrieval page
def createNewFilePage():
    for i in range(4):
        getEntry(f3)
    addEntryButton = Button(f3, text='Add entry', command=addRegEntry, width=10, bg=colors.pink)
    removeEntryButton = Button(f3, text='Remove entry', command=removeEntry, width=10, bg=colors.pink)
    submit = Button(f3, text='Submit', width=10, bg=colors.pink, command=lambda:[createFile(), readFile(), getCumulativeGPA(), raise_frame(f5)])
    addEntryButton.grid(row=0, column=4, padx=7, pady=8)
    removeEntryButton.grid(row=1, column=4, padx=7, pady=8)
    submit.grid(row=2, column=4, padx=7, pady=8)

#Sets up window for GPA calculation page
gpaLbl = Label(f5, text='Current cumulative GPA:', font=('Arial', 13), bg=colors.blue)
cumulativeGPA = Label(f5, text='', font=('Arial', 13), bg=colors.blue)
testGPA = Button(f5, text="Test GPA", width=15, bg=colors.pink, command=lambda:[clear(),createTestGPAPage(),raise_frame(f6)])
home = Button(f5, text='Home', width=15, bg=colors.pink, command=lambda:raise_frame(f1))
gpaLbl.pack(pady=(15,10))
cumulativeGPA.pack(pady=(0,10))
testGPA.pack(pady=7)
home.pack(pady=7)

#Sets up window for Test GPA calculation page
def createTestGPAPage():
    for i in range(4):
        getEntry(f6)
    addEntryButton = Button(f6, text='Add entry', command=addTestEntry, width=10, bg=colors.pink)
    removeEntryButton = Button(f6, text='Remove entry', command=removeEntry, width=10, bg=colors.pink)
    submit = Button(f6, text='Submit', command=lambda:[updateTestGPA(testGPAContainer,getTestGPA())], width=10, bg=colors.pink)
    testGPAContainer = Label(f6, text=getTestGPA(), font=('Arial Bold', 10), bg=colors.blue)
    testGPALbl = Label(f6, text='GPA: ', font=('Arial Bold', 10), bg=colors.blue)
    home = Button(f6, text='Home', width=10, bg=colors.pink, command=lambda:[clearFrame(f6),raise_frame(f1)])
    back = Button(f6, text='Back', width=10, bg=colors.pink, command=lambda:[clearFrame(f6),raise_frame(f5)])
    addEntryButton.grid(row=0, column=4, padx=(12,7), pady=8)
    removeEntryButton.grid(row=1, column=4, padx=(12,7), pady=8)
    submit.grid(row=2, column=4, padx=(13,6), pady=8)
    testGPALbl.grid(row=3, column=4, padx=(13,6), pady=8)
    testGPAContainer.grid(row=4, column=4, padx=(13,6), pady=8)
    back.grid(row=5, column=4, padx=(13,6), pady=8)
    home.grid(row=6, column=4, padx=(13,6), pady=8)
    
#Diplay updated test GPA
def updateTestGPA(label,gpa):
    label.config(text=gpa)

#Add Test Entry
def addTestEntry():
    getEntry(f6)

#Add Regular Entry
def addRegEntry():
    getEntry(f3)

def getCourseGrade(gradeContainer):
    grades = 0
    for i in range(len(grade.scores)):
       if(grade.scores[i].get() != ''):
            grades+= float(grade.scores[i].get()) * float(grade.weights[i].get())
    gradeContainer.config(text=str(grades))

#Calculates course grade
def createCourseGradePage():
    for i in range(4):
        getEntry(f7)
    addEntryButton = Button(f7, text='Add entry', command=lambda:[getEntry(f7)], width=10, bg=colors.pink)
    removeEntryButton = Button(f7, text='Remove entry', command=removeEntry, width=10, bg=colors.pink)
    gradeContainer = Label(f7, text='', font=('Arial Bold', 10), bg=colors.blue)
    submit = Button(f7, text='Submit', command=lambda:[getCourseGrade(gradeContainer)], width=10, bg=colors.pink)
    gradeLbl = Label(f7, text='Grade:', font=('Arial Bold', 10), bg=colors.blue)
    addEntryButton.grid(row=0, column=4, padx=7, pady=8)
    removeEntryButton.grid(row=1, column=4, padx=7, pady=8)
    back = Button(f7, text='Back', width=10, bg=colors.pink, command=lambda:[clearFrame(f7),raise_frame(f1)])
    submit.grid(row=2, column=4, padx=7, pady=8)
    gradeLbl.grid(row=3, column=4, padx=7, pady=8)
    gradeContainer.grid(row=4, column=4, padx=7, pady=8)
    back.grid(row=5, column=4, padx=7, pady=8)

#Clears the frame
def clearFrame(frame):
    for i in frame.winfo_children():
        i.destroy()

#Sets window to appear in center of screen
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('+%d+%d' % (x,y))

raise_frame(f1)
root.mainloop()