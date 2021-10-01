from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import connection



root = Tk()
root.title("View Orders")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


def populateView():
    tree.delete(*tree.get_children())
    connection.Database()
    connection.cursor.execute("""SELECT TransDetails.TransID, TransDetails.product_id, TransDetails.Quantity, transact.date, transact.Time,transact.staffid
FROM TransDetails 
INNER JOIN transact
ON TransDetails.TransID = transact.TransID;""")
    						

    fetch = connection.cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
    connection.cursor.close()
    connection.conn.close()
    


Top = Frame(root, width=700, height=50, bd=8)
Top.pack(side=TOP)
Button_Group=Frame(root, width=700, height=50)
Button_Group.pack(side=TOP)
Buttons = Frame(Button_Group, width=200, height=50)
Buttons.pack(side=LEFT)
Buttons1 = Frame(Button_Group, width=500, height=50)
Buttons1.pack(side=RIGHT)
Body = Frame(root, width=700, height=300, bd=8,)
Body.pack(side=BOTTOM)



txt_title = Label(Top, width=300, font=('arial', 24), text = "Orders Placed")
txt_title.pack()


btn_display = Button(Buttons, width=15, text="Display All", command= populateView)
btn_display.pack(side=LEFT)



scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = ttk.Treeview(Body, columns=("TransID", "product_id", "Quantity","Date", "Time",), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('TransID', text="TransID", anchor=W)
tree.heading('product_id', text="product_id", anchor=W)
tree.heading('Quantity', text="Quantity", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Time', text="Time", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=200)
tree.column('#4', stretch=NO, minwidth=0, width=200)
tree.column('#5', stretch=NO, minwidth=0, width=200)

tree.pack()



if __name__ == '__main__':
    root.mainloop()
   
