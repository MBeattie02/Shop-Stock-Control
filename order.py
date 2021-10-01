from tkinter import*
from tkinter import ttk

import sqlite3
from datetime import datetime




class TransactionWindow(object):
    
    def __init__(self,window):
        # Window Title
        window.wm_title("Order Products")        
        self.runningtotal = 0        
        # Create frame 1
        self.myFrame1=Frame(window, bd=2, relief=SUNKEN, bg = "white")
        self.myFrame1.pack(side=TOP, fill = BOTH)
        # frame label
        self.orderformlabel = Label(self.myFrame1, text='Place an Order', bg = "white", fg = "black")
        self.orderformlabel.grid(row = 1, column = 0, sticky = "NW")
        self.stafflabel = Label(self.myFrame1,text='Select a Staff Member', bg = "white", fg = "black")
        self.stafflabel.grid(row = 2, column = 0, sticky = "NW")

        #Select Staff Menu
        self.stafflist = self.getstaff()
        self.selectstaff = StringVar(window)
        self.selectstaff.set(self.stafflist[0])
        self.StaffMenu = OptionMenu(self.myFrame1,self.selectstaff , *self.stafflist)
        self.StaffMenu.config(bg="red")
        self.StaffMenu["menu"].config(bg="black")
        self.StaffMenu.grid(row = 3, column = 0, sticky = "NW", padx = 3, pady = 3)

        # Create frame 2
        # Transaction# Label
        self.myFrame2=Frame(window, bd=2, relief=SUNKEN, bg = "white")
        self.myFrame2.pack(anchor=W)
        self.TransIDlabel = Label(self.myFrame2, text = "TransID:", bg = "white", fg = "black")
        self.TransIDlabel.grid(row = 0, column = 0,sticky = "W")

        #Order# Entry
        self.setTransID = self.gettransID()
        self.TransID = IntVar(window)
        self.TransID.set(self.setTransID)
        self.TransIDentry = Entry(self.myFrame2, textvariable = self.TransID)
        self.TransIDentry.grid(row = 0, column = 1, sticky = "W", padx = 3, pady = 3)

        #Select Product Menu
        self.productlabel = Label(self.myFrame2,text='Select a product', bg = "white", fg = "black")
        self.productlabel.grid(row = 1, column = 0, sticky = "W")
        self.productslist = self.getproducts()#array of tuples of all products     
        self.selectproducts = StringVar(window)
        self.selectproducts.set(self.productslist[0   ])
        self.productsmenu = OptionMenu(self.myFrame2, self.selectproducts, *self.productslist)# select products
        self.productsmenu.config(bg="black")
        self.productsmenu["menu"].config(bg="black")
        self.productsmenu.grid(row = 1, column = 1, sticky = "W",padx = 3, pady = 3)

        #Qty Label & Entry
        self.qtylabel = Label(self.myFrame2, text = "Enter Quantity:", bg = "white", fg = "black")
        self.qtylabel.grid(row = 2, column = 0,sticky = "W")
        self.qty = StringVar(window)
        self.qtyentry = Entry(self.myFrame2, textvariable = self.qty)
        self.qtyentry.grid(row = 2, column = 1, sticky = "W",padx = 3, pady = 3)

        #Add Product Button
        self.transDetails = []# Where product details will be stoblack
        self.addbutton = Button(self.myFrame2, text="Add", command = self.addproduct, bg="black")
        self.addbutton.grid(row = 2, column =2, sticky = "W",padx = 3, pady = 3)
        #Remove Product Button
        self.removebutton = Button(self.myFrame2, text="Remove",command=self.removeproduct, bg = "black")
        self.removebutton.grid(row = 2, column =3, sticky = "W",padx = 3, pady = 3)

        #Order ListBox Widget
        self.currenttranslabel = Label(self.myFrame2,text='Current Transaction', bg = "white", fg = "black")
        self.currenttranslabel.grid(row = 4, column = 0, sticky = "NW")
        self.boxtitleslabel = Label(self.myFrame2,text='Product  Price  Qty', bg = "white", fg = "black")
        self.boxtitleslabel.grid(row = 3, column = 1, sticky = "W")
        self.productslist = Listbox(self.myFrame2)
        self.productslist.grid(row = 4, column = 1, sticky = "WE",padx = 3, pady = 3)

        #Total Label & Entry
        self.transtotallabel = Label(self.myFrame2,text='Transaction Total', bg = "white", fg = "black")
        self.transtotallabel.grid(row = 5, column = 0, sticky = "NW")
        self.transtotal = DoubleVar(window)
        self.transtotalentry = Entry(self.myFrame2, textvariable = self.transtotal)
        self.transtotalentry.grid(row = 5, column = 1, sticky = "NW",padx = 3, pady = 3)

        #Create frame 3
        self.myFrame3=Frame(window, bd=2, relief=SUNKEN, bg = "white")
        self.myFrame3.pack(side=BOTTOM, fill = X)
        #Save button
        self.savebutton = Button(self.myFrame3, text="Save", command = self.savetrans,bg="black")
        self.savebutton.grid(row = 0, column =0, sticky = "WE", padx = 3, pady = 3)
    
        # New Order Button
        self.newtransbutton = Button(self.myFrame3, text="New Transaction", command = self.newtransaction, bg = "black")
        self.newtransbutton.grid(row = 0, column =2, sticky = "WE", padx = 3, pady = 3)
        # Exit Button
        self.exitbutton = Button(self.myFrame3, text="Exit", command = window.destroy, bg = "black")
        self.exitbutton.grid(row = 0, column =3, sticky = "WE", padx = 3, pady = 3)
        # General feedback label
        self.feedbacklabel = Label(self.myFrame3, text="!", fg="white", bg="black")
        self.feedbacklabel.grid(row=0, column=6, columnspan=2)

   

    def savetrans(self):
        self.counter = 0

        

        date = datetime.now().strftime("%Y-%m-%d")  # date
        time = datetime.now().strftime("%H:%M:%S")  # time
        transactionvalues = (date,time)  # tuple used in database manipulation
        self.placetrans(transactionvalues)  # saves to database
        

        for item in self.transDetails:
            product_id = self.transDetails[self.counter][0]
            quantity = self.transDetails[self.counter][3]
            self.counter += 1
            transDetailValues = (product_id, quantity)  # tuple used in database
            self.placetransDetails(transDetailValues)  # saves to database
            
        self.newtransaction()  # empties fields

    def placetrans(self,values):
        #saves transaction in to database
        with sqlite3.connect("supervalu.db") as db:
            cursor = db.cursor()
            sql = """insert into
            Transact(Date, Time)
            values (?,?) """
            cursor.execute(sql,values)
            db.commit()
            return


    def placetransDetails(self, values):
        #saves trans details to database
        with sqlite3.connect("supervalu.db") as db:
            cursor = db.cursor()
            sql = """insert into
            TransDetails(product_id, Quantity)
            values (?,?)"""
            cursor.execute(sql,values)
            db.commit()
        return

    def addproduct(self):
        self.quantity= self.qty.get()
        if self.quantity == "":
            self.feedback_label["text"] = "Please enter a quantity!"
            return
        elif self.quantity.isdigit() == False:
            self.feedback_label["text"] = "Please enter a valid quantity!"
            return
        elif self.quantity == "0":
            self.feedback_label["text"] = "Please enter a valid quantity!"
            return
        else:                
            self.transDetail = self.selectproducts.get()  # product details from menu
            self.transDetail = self.transDetail.replace('(', '').replace(')', '').replace(",", '').replace("'", '')
            self.transDetail = self.transDetail.split()# splits into name and price and ID
            self.transDetail.append(self.quantity)  # gets quantity
            self.transDetails.append(self.transDetail)  # appends quantity to list of name and price and ID
            part1 = self.transDetail[1]
            part2 = self.transDetail[2]
            part3 = str(self.qty.get())  # these are for display in listbox
            self.productslist.insert(END,part1 + "    " + part2 + "    " + part3 )  # shows in listbox
            self.addtotal()  # amends running total

    def removeproduct(self):
        if len (self.transDetails) >= 1:
            self.transDetails.pop()  # removes product from sale
        self.productslist.delete(END)  # removes from display
        self.dectotal()  # amends running total

    def addtotal(self):
        self.runningtotal = self.runningtotal + (float(self.transDetail[2]) * int(self.qty.get()))
        self.transtotal.set(self.runningtotal)

    def dectotal(self):
        self.runningtotal = self.runningtotal - (float(self.transDetail[2]) * int(self.qty.get()))
        if self.runningtotal <=1:
            self.transtotal.set(0)
            self.runningtotal = 0
        else:
            self.transtotal.set(self.runningtotal)
        
        

    def getstaff(self):
        # gets staff ID's for menu
        with sqlite3.connect("supervalu.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT staffid, firstname FROM staff")
            staff = cursor.fetchall()
            
        return staff

    def getproducts(self):
        # gets Product ID's for menu
        with sqlite3.connect("supervalu.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT product_id, product_name, product_price FROM product")
            products = cursor.fetchall()
           
        return products
        


    def gettransID(self):
        # used for incrementing transID
        with sqlite3.connect("supervalu.db") as db:
            cursor = db.cursor()  # db query
            cursor.execute("SELECT MAX(TransID)FROM Transact")
            transactions = cursor.fetchone()
            transID = transactions[0]
            if transID is None:  # if no transactions already
                transID = 1
            else:
                transID += 1  # add 1
        return transID

    def newtransaction(self):
        if len(self.transDetails)>= 1:
            self.transDetails = []
            self.productslist.delete(0,END)
            self.TransID.set(self.gettransID())
            self.qty.set(0)
            self.transtotal.set(0)
            self.runningtotal = 0



    def transactionTableMenu():
        menu =int(input("\n\n1) (Re)Create Transaction Table\n2) Insert Transaction\n3) Update Transaction Info\n4) Delete Transaction\n5)Search for one Transaction\n6)Print All Transactions"))
        try:
            if menu==1:
                createTransactionTable()
            elif menu==2:
                insertTransactionData()
            elif menu==3:
                updateTransaction()
            elif menu==4:
                deleteTransaction()
            elif menu==5:
                print(searchOneTransaction())
            elif menu==6:
                searchAllTransactions()         
            else:
                print("Invalid Number")
                return False
        except ValueError:
            print("Must be an integer")
            return False




def transactionmenu():

    TransactionWin = Tk()
    TransactionWin["bg"] = "black"
    main = TransactionWindow(TransactionWin)
    TransactionWin.mainloop()

if __name__ == "__main__":
     
    transactionmenu()
    
    

