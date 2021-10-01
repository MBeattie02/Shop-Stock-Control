from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("temperature List")
width = 1200
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="maroon")

#variables 
log_id = StringVar()
STAFFNAME = StringVar()
FRIDGENAME = StringVar()
TIME = StringVar()
DATE= StringVar()
PROBLEMS = StringVar()
TEMPERATURE = StringVar()





def Database():
    conn = sqlite3.connect("supervalu.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `log` (log_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, staffname TEXT, fridgename TEXT, time TEXT, date TEXT, problems TEXT, temperature TEXT)")
    cursor.execute("SELECT * FROM `log` ORDER BY `fridgename` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  STAFFNAME.get() == "" or FRIDGENAME.get() == "" or TIME.get() == "" or DATE.get() == "" or PROBLEMS.get() == "" or TEMPERATURE.get() == "":
        result = tkmessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("supervalu.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `log` (staffname, fridgename, time, date, problems, temperature) VALUES(?, ?, ?, ?, ?, ?)", (str(STAFFNAME.get()), str(FRIDGENAME.get()), str(TIME.get()), str(DATE.get()), str(PROBLEMS.get()), str(TEMPERATURE.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `log` ORDER BY `fridgename` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        STAFFNAME.set("")
        FRIDGENAME.set("")
        TIME.set("")
        DATE.set("")
        PROBLEMS.set("")
        TEMPERATURE.set("")

def UpdateData():
    if TIME.get() == "":
       result = tkmessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("supervalu.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `log` SET `staffname` = ?, `fridgename` = ?, `time` =?, `date` = ?,  `problems` = ?, `temperature` = ? WHERE `log_id` = ?", (str(STAFFNAME.get()), str(FRIDGENAME.get()), str(TIME.get()), str(DATE.get()), str(PROBLEMS.get()), str(TEMPERATURE.get()), int(log_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `log` ORDER BY `fridgename` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        STAFFNAME.set("")
        FRIDGENAME.set("")
        TIME.set("")
        DATE.set("")
        PROBLEMS.set("")
        TEMPERATURE.set("")
        
    

def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("supervalu.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `log` WHERE `log_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow():
    global NewWindow
    
    FRIDGENAME.set("")
    STAFFNAME.set("")
    TIME.set("")
    DATE.set("")
    PROBLEMS.set("")
    TEMPERATURE.set("")
    NewWindow = Toplevel()
    NewWindow.title("temperature List")
    width = 600
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #FRAMES
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    temperatureForm = Frame(NewWindow)
    temperatureForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(temperatureForm)
    Morning = Radiobutton(RadioGroup, text="Morning", variable=TIME, value="morning",  font=('arial', 14)).pack(side=LEFT)
    Evening = Radiobutton(RadioGroup, text="evening", variable=TIME, value="evening",  font=('arial', 14)).pack(side=LEFT)
    
    #LABELS
    lbl_title = Label(FormTitle, text="Adding New temperature", font=('arial', 16), bg="maroon",  width = 300)
    lbl_title.pack(fill=X)
    lbl_staffname = Label(temperatureForm, text="staffname", font=('arial', 14), bd=5)
    lbl_staffname.grid(row=0, sticky=W)
    lbl_fridgename = Label(temperatureForm, text="fridgename", font=('arial', 14), bd=5)
    lbl_fridgename.grid(row=1, sticky=W)
    lbl_time = Label(temperatureForm, text="time", font=('arial', 14), bd=5)
    lbl_time.grid(row=2, sticky=W)
    lbl_date = Label(temperatureForm, text="date", font=('arial', 14), bd=5)
    lbl_date.grid(row=3, sticky=W)
    lbl_problems = Label(temperatureForm, text="problems", font=('arial', 14), bd=5)
    lbl_problems.grid(row=4, sticky=W)
    lbl_temperature = Label(temperatureForm, text="temperature", font=('arial', 14), bd=5)
    lbl_temperature.grid(row=5, sticky=W)

    #ENTRY
    staffname = Entry(temperatureForm, textvariable=STAFFNAME, font=('arial', 14))
    staffname.grid(row=0, column=1)
    fridgename = Entry(temperatureForm, textvariable=FRIDGENAME, font=('arial', 14))
    fridgename.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    date = Entry(temperatureForm, textvariable=DATE,  font=('arial', 14))
    date.grid(row=3, column=1)
    problems = Entry(temperatureForm, textvariable=PROBLEMS,  font=('arial', 14))
    problems.grid(row=4, column=1)
    temperature = Entry(temperatureForm, textvariable=TEMPERATURE,  font=('arial', 14))
    temperature.grid(row=5, column=1)
    
#BUTTONS
    btn_addcon = Button(temperatureForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)




    
#FRAMES
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="maroon")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="maroon")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#LABELS
lbl_title = Label(Top, text="Fridge Logs", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#ENTRY

#BUTTONS
btn_add = Button(MidLeft, text="+ ADD NEW", bg="#66ff66", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

#TABLES
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("logID", "staffname", "fridgename", "time", "date", "problems", "temperature"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('logID', text="logID", anchor=W)
tree.heading('staffname', text="staffname", anchor=W)
tree.heading('fridgename', text="fridgename", anchor=W)
tree.heading('time', text="time", anchor=W)
tree.heading('date', text="date", anchor=W)
tree.heading('problems', text="problems", anchor=W)
tree.heading('temperature', text="temperature", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=180)
tree.column('#2', stretch=NO, minwidth=0, width=180)
tree.column('#3', stretch=NO, minwidth=0, width=180)
tree.column('#4', stretch=NO, minwidth=0, width=180)
tree.column('#5', stretch=NO, minwidth=0, width=180)
tree.column('#6', stretch=NO, minwidth=0, width=180)
tree.column('#7', stretch=NO, minwidth=0, width=180)
tree.pack()


#INITIALIZATION
if __name__ == '__main__':
    Database()
    root.mainloop()
    
