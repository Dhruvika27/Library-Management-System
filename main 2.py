from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibrayManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title(" Library Management System")
        self.root.geometry("1550x800+0+0")

        # =============================== Variable =========================================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finalprice = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # ================================DATAFRAME LEFT===============================

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", bd=12, relief=RIDGE,
                                   font=("arial", 15, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("arial", 13, "bold"), padx=2,
                          pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 13, "bold"), textvariable=self.member_var,
                                 width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue", text="PRN NO", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("times new roman", 13, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg="powder blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Name", padx=2, pady=6,
                             bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name", padx=2, pady=6,
                            bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address1", padx=2, pady=6,
                            bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2", padx=2, pady=6,
                            bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code", padx=2, pady=6,
                            bg="powder blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile", padx=2, pady=6, bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6,
                             bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAutherName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=6,
                              bg="powder blue")
        lblAutherName.grid(row=2, column=2, sticky=W)
        txtAutherName = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.auther_var, width=29)
        txtAutherName.grid(row=2, column=3)

        lblDataBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6,
                                bg="powder blue")
        lblDataBorrowed.grid(row=3, column=2, sticky=W)
        txtDataBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDataBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6,
                           bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysonBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days on Book:", padx=2, pady=6,
                              bg="powder blue")
        lblDaysonBook.grid(row=5, column=2, sticky=W)
        txtDaysonBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.daysonbook, width=29)
        txtDaysonBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6,
                                  bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.latereturnfine_var,
                                  width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6,
                               bg="powder blue")
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateoverdue, width=29)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6,
                               bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.finalprice, width=29)
        txtActualPrice.grid(row=8, column=3)

        # ==================================== DataFrame Right============================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", bd=12, relief=RIDGE,
                                    font=("arial", 12, "bold"))
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBoooks = ['Head First Book', 'Learn Python The Hard Way', 'Python Programming', "Secrete Rahshy",
                      'Python CookBook',
                      'Intro to Machine Learning', 'Fluent Python', 'Machine tecno', 'My Python', 'Joss Ellif guru',
                      'Elite Jungle python', 'Jungli Python', 'Mumbai Python', 'Pune Python', 'Machine Python',
                      'Advance Python',
                      'Inton Python', 'RedChili Python', 'Ishq Python', 'Guru of Python', 'Python for Beginners',
                      'Safari', 'Machine Learning', "Artificial Intelligence"]

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Head First Book":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.788")

            elif x == "Learn Python The Hard Way":
                self.bookid_var.set("BKID54")
                self.booktitle_var.set("Introduction to Python")
                self.auther_var.set("j.k shah")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=10)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.75")

            elif x == "Python Programming":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Python Programming")
                self.auther_var.set("Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.1000")

            elif x == "Secrete Rahshy":
                self.bookid_var.set("ABS5")
                self.booktitle_var.set("Rahshy")
                self.auther_var.set("Jigrra")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.10")

            elif x == "Python CookBook":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Python")
                self.auther_var.set("Harry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.200")

            elif x == "Intro to Machine Learning":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("ML")
                self.auther_var.set("John")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.60")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.300")

            elif x == "Fluent Python":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Fluent")
                self.auther_var.set("Jack")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.425")

            elif x == "Machine tecno":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Machine Tecno")
                self.auther_var.set("Rock")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.500")

            elif x == "My Python":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Python")
                self.auther_var.set("Zudio")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.600")

            elif x == "Joss Ellif guru":
                self.bookid_var.set("ABC")
                self.booktitle_var.set("Joss Guru")
                self.auther_var.set("Guru")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.150")

            elif x == "Elite Jungle python":
                self.bookid_var.set("ABS5454")
                self.booktitle_var.set("Jungle")
                self.auther_var.set("Elite")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.250")

            elif x == "Jungli Python":
                self.bookid_var.set("CCC5454")
                self.booktitle_var.set("Programming")
                self.auther_var.set("AAA")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.600")

            elif x == "Mumbai Python":
                self.bookid_var.set("AGT454")
                self.booktitle_var.set("Mumbai")
                self.auther_var.set("jay")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.999")

            elif x == "Pune Python":
                self.bookid_var.set("5454")
                self.booktitle_var.set("Pune")
                self.auther_var.set("Dhruvi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.30")


            elif x == "Machine Python":
                self.bookid_var.set("FDFDD")
                self.booktitle_var.set("Machine")
                self.auther_var.set("Ujash")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.1500")

            elif x == "Advance Python":
                self.bookid_var.set("GDGD")
                self.booktitle_var.set("Advance")
                self.auther_var.set("Het")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.159")

            elif x == "Inton Python":
                self.bookid_var.set("JKHK")
                self.booktitle_var.set("Intro")
                self.auther_var.set("Jash")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.459")

            elif x == "RedChili Python":
                self.bookid_var.set("JBFKJ")
                self.booktitle_var.set("Redchili")
                self.auther_var.set("Mahatma")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.299")

            elif x == "Ishq Python":
                self.bookid_var.set("JHBGJHG")
                self.booktitle_var.set("Ishq")
                self.auther_var.set("AHAHA")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.399")

            elif x == "Guru of Python":
                self.bookid_var.set("RERE")
                self.booktitle_var.set("Python Guru")
                self.auther_var.set("Guru")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.150")

            elif x == "Python for Beginners":
                self.bookid_var.set("5225")
                self.booktitle_var.set("beginners")
                self.auther_var.set("Bill gates")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.199")

            elif x == "Safari":
                self.bookid_var.set("2656")
                self.booktitle_var.set("jungle")
                self.auther_var.set("tata")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.599")

            elif x == "Machine Learning":
                self.bookid_var.set("78787")
                self.booktitle_var.set("ABCD")
                self.auther_var.set("Ratan ")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.399")

            elif x == "Artificial Intelligence":
                self.bookid_var.set("5115412")
                self.booktitle_var.set("AAA")
                self.auther_var.set("AIAI")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs.299")


        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END, item)

        # ==================================Buttons Frame======================================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, command=self.adda_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton,command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton,command=self.update ,text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, command=self.delete,text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton,command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, command=self.iExit,text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        # ==================================Information Frame======================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.libray_table = ttk.Treeview(Table_frame,
                                         column=("membertype", "prnno", "title", "firstname", "lastname", "address1",
                                                 "address2", "postid", "mobile", "bookid", "booktitle", "auther",
                                                 "dateborrowed",
                                                 "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),
                                         xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)

        self.libray_table.heading("membertype", text="Member Type")
        self.libray_table.heading("prnno", text="PRN No.")
        self.libray_table.heading("title", text="Title")
        self.libray_table.heading("firstname", text="First Name")
        self.libray_table.heading("lastname", text="Last Name")
        self.libray_table.heading("address1", text="Address1")
        self.libray_table.heading("address2", text="Address2")
        self.libray_table.heading("postid", text="Post ID")
        self.libray_table.heading("mobile", text="Mobile Number")
        self.libray_table.heading("bookid", text="Book ID")
        self.libray_table.heading("booktitle", text="Book Title")
        self.libray_table.heading("auther", text="Auther")
        self.libray_table.heading("dateborrowed", text="Date of Borrowed")
        self.libray_table.heading("datedue", text="Date Due")
        self.libray_table.heading("days", text="DaysOnBook")
        self.libray_table.heading("latereturnfine", text="LateReturnFine")
        self.libray_table.heading("dateoverdue", text="DateOverDue")
        self.libray_table.heading("finalprice", text="Final Price")

        self.libray_table["show"] = "headings"
        self.libray_table.pack(fill=BOTH, expand=1)

        self.libray_table.column("membertype", width=100)
        self.libray_table.column("prnno", width=100)
        self.libray_table.column("title", width=100)
        self.libray_table.column("firstname", width=100)
        self.libray_table.column("lastname", width=100)
        self.libray_table.column("address1", width=100)
        self.libray_table.column("address2", width=100)
        self.libray_table.column("postid", width=100)
        self.libray_table.column("mobile", width=100)
        self.libray_table.column("bookid", width=100)
        self.libray_table.column("booktitle", width=100)
        self.libray_table.column("auther", width=100)
        self.libray_table.column("dateborrowed", width=100)
        self.libray_table.column("datedue", width=100)
        self.libray_table.column("days", width=100)
        self.libray_table.column("latereturnfine", width=100)
        self.libray_table.column("dateoverdue", width=100)
        self.libray_table.column("finalprice", width=100)

        self.fetch_data()
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)

        
    def adda_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue.get(),
            self.finalprice.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")


    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "UPDATE library SET Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Auther=%s,Dateborrowed=%s,Datedue=%s,Daysonbook=%s,Latereturnfine=%s,Dateoverdue=%s,Finalprice=%s where PRN_NO=%s",
            (
                self.member_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.auther_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue.get(),
                self.finalprice.get(),
                self.prn_var.get(),
            ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success", "Member has been Updated") 
        
       

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in rows:
                self.libray_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_rows=self.libray_table.focus()
        content=self.libray_table.item(cursor_rows)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n" )
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get() + "\n" )
        self.txtBox.insert(END,"ID NO:\t\t"+ self.id_var.get() + "\n" )
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n" )
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n" )
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n" )
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n" )
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n" )
        self.txtBox.insert(END,"Mobile NO:\t\t"+ self.mobile_var.get() + "\n" )
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n" )
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n" )
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n" )
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n" )
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n" )
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook.get() + "\n" )
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.latereturnfine_var.get() + "\n" )
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue.get() + "\n" )
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice.get() + "\n" )

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue.set(""),
        self.finalprice.set(""),
        self.txtBox.delete("1.0",END),

  

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management system", "Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()==""or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="Mydata")
            my_cursor = conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")







        

if __name__ == "__main__":
    root = Tk()
    obj = LibrayManagementSystem(root)
    root.mainloop()
