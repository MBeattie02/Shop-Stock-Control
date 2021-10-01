from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import order
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Supervalu Richhill System")


# Screen Layout 
width = 1400
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="maroon")

#VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCTID = IntVar()
PRODUCT_TYPE = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
FRIDGEID = IntVar()
SEARCH = StringVar()
EXPIRYDATE = StringVar()



def Database():
    global conn, cursor
    conn = sqlite3.connect("supervalu.db") #connect to database 
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT, fridgeid TEXT, product_type TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Supervalu Richhill System', 'Are you sure you want to exit?', icon="warning")#on screen verification 
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Supervalu Richiill System', 'Are you sure you want to exit?', icon="warning")#On screen verification 
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Supervalu Inventory System/Account Login")#Title layout 
    width = 1400
    height = 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    



#Login Screen 
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)#
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)#entry box 
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")#entry box 
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    

def Home():
    global Home
    Home = Tk()
    Home.title("Supervalu Inventory System/Home")
    width = 1400
    height = 800
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Supervalu Inventory System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)#number of menubar options 
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)#commands performed by menubar buttons 
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    filemenu3.add_command(label="view", command=showContact)
    filemenu4.add_command(label="view/ Add Fridge Logs", command=showLog)
    filemenu5.add_command(label="Order Products", command=makeOrder)
    filemenu5.add_command(label="View Orders ", command=viewOrder)

    menubar.add_cascade(label="Account", menu=filemenu)#menubar titles
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Staff" , menu=filemenu3)
    menubar.add_cascade(label="Log" , menu=filemenu4)
    menubar.add_cascade(label="Order" , menu=filemenu5)
    
    Home.config(menu=menubar)
    Home.config(bg="maroon")

    Home.config(menu=menubar)
    Home.config(bg="maroon")


def showContact():
    global showcontact
    import contact 

def showLog():
    global showLog
    import logs


def makeOrder():
    global makeOrder
    import order 


def viewOrder():
    global ViewOrder 
    import index 


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Supervalu Inventory System/Add New Product")
    width = 900 
    height = 900
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()



def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=3000, bd=6, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    
    RadioGroup = Frame(MidAddNew)
    Chilled = Radiobutton(RadioGroup, text="Chilled", variable=PRODUCT_TYPE, value="Chilled",  font=('arial', 14)).pack(side=LEFT)#set of 3 predetermined options 
    Ambient = Radiobutton(RadioGroup, text="Ambient", variable=PRODUCT_TYPE, value="Ambient",  font=('arial', 14)).pack(side=LEFT)
    Frozen = Radiobutton(RadioGroup, text="Frozen", variable=PRODUCT_TYPE, value="Frozen",  font=('arial', 14)).pack(side=LEFT)


    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    lbl_productid = Label(MidAddNew, text="ProductID:", font=('arial', 25), bd=10)
    lbl_productid.grid(row=3, sticky=W)
    lbl_fridgeid = Label(MidAddNew, text=" FridgeID:", font=('arial', 25), bd=10)
    lbl_fridgeid.grid(row=4, sticky=W)
    lbl_producttype = Label(MidAddNew, text="Product Type:", font=('arial', 25), bd=10)
    lbl_producttype.grid(row=5, sticky=W)
    lbl_expiryDate = Label(MidAddNew, text="Expiry Date:", font=('arial', 25), bd=10)
    lbl_expiryDate.grid(row=7, sticky=W)
    


    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)#entry box 
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)#entry box 
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)#entry box 
    productprice.grid(row=2, column=1)
    productid = Entry(MidAddNew, textvariable=PRODUCTID, font=('arial', 25), width=15)#entry box 
    productid.grid(row=3, column=1)
    fridgeid = Entry(MidAddNew, textvariable=FRIDGEID, font=('arial', 25), width=15)#entry box 
    fridgeid.grid(row=4, column=1)
    producttype = Entry(MidAddNew, textvariable=PRODUCT_TYPE, font=('arial', 25), width=15)#entry box 
    producttype.grid(row=5, column=1)
    expiryDate = Entry(MidAddNew, textvariable=EXPIRYDATE, font=('arial', 25), width=15)#entry box 
    expiryDate.grid(row=7, column=1)
    RadioGroup.grid(row=6, column=1)


    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=12, columnspan=2, pady=20)




def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (product_id, product_name, product_qty, product_price, product_type, fridgeid, expirydate) VALUES(?, ?, ?, ?, ?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get()), int(FRIDGEID.get()), int(PRODUCTID.get()),str(PRODUCT_TYPE.get()),str(EXPIRYDATE.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    PRODUCTID.set("")
    PRODUCT_TYPE.set("")
    FRIDGEID.set("")
    EXPIRYDATE.set("")
    cursor.close()
    conn.close()



def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=1000, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=100)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=100)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price", "FridgeID", "Product Type", "Expiry Date"), selectmode="extended", height=1000, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('ProductID', text="ProductID",anchor=W)#create tree column headings 
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.heading('Product Type', text="Product Type",anchor=W)
    tree.heading('FridgeID', text="FridgeID",anchor=W)
    tree.heading('Expiry Date', text="Expiry Date",anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)#defines size of tree column 
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=200)

    tree.pack()
    DisplayData()





def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))#selects products from database
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())#resets the tree search 
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Supervalu Inventory System', 'Are you sure you want to delete this record?', icon="warning")#on screen verification 
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])#selects data to be deleted 
            conn.commit()
            cursor.close()
            conn.close()
    

def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Supervalu Inventory System/View Product")
    width = 1400
    height = 800
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def Logout():
    result = tkMessageBox.askquestion('Supervalu Inventory System', 'Are you sure you want to logout?', icon="warning")#on screen verification 
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
  
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#MENUBAR WIDGETS
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#FRAME
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#LABEL WIDGET
lbl_display = Label(Title, text="Supervalu Inventory System", font=('arial', 45))
lbl_display.pack()

#INITIALIZATION
if __name__ == '__main__':
    root.mainloop()
