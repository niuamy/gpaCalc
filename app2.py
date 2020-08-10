from tkinter import *

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

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

for frame in (f1, f2, f3, f4, f5):
    frame.grid(row=0, column=0, sticky='news')

#Variables
fileName = StringVar()

#Start Page
Button(f1, text='New File', width=10, command=lambda:raise_frame(f2)).pack()
Button(f1, text='Existing File', width=10, command=lambda:raise_frame(f4)).pack()

#New file: get new file name
Label(f2, text='Please Enter File Name', font=('Arial Bold', 10)).pack()
Entry(f2, bd = 2, width = 12, font='Arial 10', textvariable=fileName).pack()
Button(f2, text="Submit", width=10, command=lambda:raise_frame(f3)).pack()

#Existing file: get file name
Label(f4, text='Please Enter File Name', font=('Arial Bold', 10)).pack()
Entry(f4, bd = 2, width = 12, font='Arial 10', textvariable=fileName).pack()
Button(f4, text="Submit", width=10, command=lambda:raise_frame(f5)).pack()

#New file: get new file content
rowCount = 0
col = 0
rowItems = []
scores = []
weights = []
gpaList = []

#Add score and weight entry
def getEntry():
    global rowCount
    score = StringVar()
    weight = IntVar()
    scoreLabel = Label(f3, text='Grade', font=('Arial Bold', 10))
    weightLabel = Label(f3, text='  Weight', font=('Arial Bold', 10))
    scoreEntry = Entry(f3, bd = 2, width = 6, font='Arial 10', textvariable=score)
    weightEntry = Entry(f3, bd = 2, width = 6, font='Arial 10', textvariable=weight)
    scoreLabel.grid(row=rowCount,column=0, padx=7)
    scoreEntry.grid(row=rowCount,column=1)
    weightLabel.grid(row=rowCount,column=2, padx=4, pady=10)
    weightEntry.grid(row=rowCount,column=3)

    row = [scoreLabel, weightLabel, scoreEntry, weightEntry]
    rowItems.append(row)
    scores.append(scoreEntry)
    weights.append(weightEntry)
    rowCount += 1

#Removes the last score and weight entry
def removeEntry():
    global rowCount
    lastItem = len(rowItems) - 1
    for i in rowItems[lastItem]:
        i.destroy()
    rowItems.pop(lastItem)
    scores.pop(lastItem)
    weights.pop(lastItem)
    rowCount -= 1

#Creates a new file with the scores and weights
def createFile():
    out = open("files/" + fileName.get(), "a")
    for i in range(len(scores)):
        out.write(scores[i].get())
        out.write(weights[i].get())
        out.write("\n")
    out.close()

#Reads a file that contains the scores and weights
def readFile():
    text = open("files/" + fileName.get(), "r")
    for line in text:
        grade = line[:1]
        weight = line[1:3]
        print(grade)
        print(weight)
        gpaList.append(gpa(weight,grade))
    text.close() 

#Gets and displays cumulative GPA
def getCumulativeGPA():
    gpa = getEarned(gpaList)/getTotal(gpaList)
    gpaLbl.configure(text=str(gpa))

#Sets up window for content retrieval page
for i in range(4):
    getEntry()
addEntry = Button(f3, text='Add entry', command=getEntry)
removeEntry = Button(f3, text='Remove entry', command=removeEntry)
submit = Button(f3, text='Submit', command=lambda:[createFile(), raise_frame(f5)])
addEntry.grid(row=0, column=4, padx=7, pady=8)
removeEntry.grid(row=1, column=4, padx=7, pady=8)
submit.grid(row=2, column=4, padx=7, pady=8)

#Sets up window for GPA calculation page
cumulativeGPA = Button(f5, text="Cumulative GPA", command=lambda:[readFile(),getCumulativeGPA()])
gpaLbl = Label(f5, text='', font=('Arial Bold', 10))
cumulativeGPA.pack()
gpaLbl.pack()

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