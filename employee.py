from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Cheeku Singh's Employee Management System")


        
        #Heading
        lbl_title = Label(self.root,text = "EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',35,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1600,height=50)


        #Logo
        img_logo=Image.open( 'Images/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=300,y=0,width=50,height=50)

        #Image Frame
        img_frame =Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=200)

        #1st Image
        img1=Image.open( 'Images/1.jpg')
        img1=img1.resize((540,200),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=200)

        #2nd Image
        img2=Image.open( 'Images/2.jpg')
        img2=img2.resize((540,200),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=540,y=0,width=540,height=200)

        #3rd Image
        img3=Image.open( 'Images/3.jpg')
        img3=img3.resize((540,200),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1080,y=0,width=540,height=200)

        #Main Frame
        main_frame =Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=15,y=250,width=1500,height=560)

        #Upper Frame
        upper_frame =LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information', font=('times new roman',15,'bold'),fg='red')
        upper_frame.place(x=15,y=0,width=1470,height=250)

        #varialbes for entry
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_design=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_marital=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()


        #Labels and Entry Fields
        # 0th Row
        #Department
        lbl_dept = Label(upper_frame, text="Department:", font=('ariel',11,'bold'), bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        #Select Department
        combo_dept =ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('ariel',11,'bold'),width=20,state='readonly')
        combo_dept['value']=('Select Department','HR','Engineer','Manager')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #name
        lbl_name = Label(upper_frame, text="Name:", font=('ari3l',11,'bold'), bg='white')
        lbl_name.grid(row=0,column=2,padx=2,sticky=W)

        #name entry
        txt_name=ttk.Entry(upper_frame, textvariable=self.var_name, width=22,font=("ariel",11,"bold"))
        txt_name.grid(row=0,column=3, sticky=W, padx=2,pady=7)

        #phone number
        lbl_phone = Label(upper_frame, text="Contact Number:", font=('ariel',11,'bold'), bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,sticky=W)

        #phone number entry
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_contact,width=22,font=("ariel",11,"bold"))
        txt_phone.grid(row=0,column=5, sticky=W, padx=2,pady=7)

        #------------------------------------------------------------------------------------------------

        # 1st Row
        #designation
        lbl_desig = Label(upper_frame, text="Designation:", font=('ariel',11,'bold'), bg='white')
        lbl_desig.grid(row=1,column=0,padx=2,sticky=W)

        #designation Entry
        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_design,width=22,font=("ariel",11,"bold"))
        txt_desig.grid(row=1,column=1, sticky=W, padx=2,pady=7)

        #email
        lbl_email = Label(upper_frame, text="Email:", font=('ariel',11,'bold'), bg='white')
        lbl_email.grid(row=1,column=2,padx=2,sticky=W)

        #email entry
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("ariel",11,"bold"))
        txt_email.grid(row=1,column=3, sticky=W, padx=2,pady=7)

        #country
        lbl_country = Label(upper_frame, text="Country:", font=('ariel',11,'bold'), bg='white')
        lbl_country.grid(row=1,column=4,padx=2,sticky=W)
        
        #country entry
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("ariel",11,"bold"))
        txt_country.grid(row=1,column=5, sticky=W, padx=2,pady=7)

        #----------------------------------------------------------------------------------------------

        #2nd Row
        #address
        lbl_add = Label(upper_frame, text="Address:", font=('ariel',11,'bold'), bg='white')
        lbl_add.grid(row=2,column=0,padx=2,sticky=W)

        #address entry
        txt_add=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("ariel",11,"bold"))
        txt_add.grid(row=2,column=1, sticky=W, padx=2,pady=7)

        #Married Status
        lbl_marital = Label(upper_frame, text="Marital Status:", font=('ariel',11,'bold'), bg='white')
        lbl_marital.grid(row=2,column=2,padx=2,sticky=W)

        #marital status entry
        combo_marital =ttk.Combobox(upper_frame,textvariable=self.var_marital,font=('ariel',11,'bold'),width=20,state='readonly')
        combo_marital['value']=('Select Status','Married','Unmarried')
        combo_marital.current(0)
        combo_marital.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        #Annual Salary
        lbl_salary = Label(upper_frame, text="Annual Salary(CTC):", font=('ariel',11,'bold'), bg='white')
        lbl_salary.grid(row=2,column=4,padx=2,sticky=W)

        #Annual Salary Entry
        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("ariel",11,"bold"))
        txt_salary.grid(row=2,column=5, sticky=W, padx=2,pady=7)

        #-----------------------------------------------------------------------------

        #3rd Row
        #DOB
        lbl_DOB = Label(upper_frame, text="Date of Birth:", font=('ariel',11,'bold'), bg='white')
        lbl_DOB.grid(row=3,column=0,padx=2,sticky=W)

        #DOB entry
        txt_DOB=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("ariel",11,"bold"))
        txt_DOB.grid(row=3,column=1, sticky=W, padx=2,pady=7)

        #DOJ
        lbl_DOJ = Label(upper_frame, text="Date of Joining:", font=('ariel',11,'bold'), bg='white')
        lbl_DOJ.grid(row=3,column=2,padx=2,sticky=W)

        #DOJ entry
        txt_DOJ=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("ariel",11,"bold"))
        txt_DOJ.grid(row=3,column=3, sticky=W, padx=2,pady=7)

        #-------------------------------------------------------------------------------

        #4th row
        #ID
        combo_ID =ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('ariel',11,'bold'),width=20,state='readonly')
        combo_ID['value']=('Select ID','AADHAAR','DRIVING LICENCE','PAN CARD','VOTER ID CARD')
        combo_ID.current(0)
        combo_ID.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        #ID Numb
        txt_Num=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("ariel",11,"bold"))
        txt_Num.grid(row=4,column=1, sticky=W, padx=2,pady=7)

        #gender
        lbl_DOJ = Label(upper_frame, text="Gender:", font=('ariel',11,'bold'), bg='white')
        lbl_DOJ.grid(row=4,column=2,padx=2,sticky=W)

        #Gender entry
        combo_Gender =ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('ariel',11,'bold'),width=20,state='readonly')
        combo_Gender['value']=('Select Gender','Male','Female','TransGender')
        combo_Gender.current(0)
        combo_Gender.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        #----------------------------------------------------------------------------------------

        #profile photo
        img_profile=Image.open( 'Images/4.jpg')
        img_profile=img_profile.resize((200,200),Image.ANTIALIAS)
        self.photo_profile=ImageTk.PhotoImage(img_profile)

        self.img_profile=Label(upper_frame,image=self.photo_profile)
        self.img_profile.place(x=1050,y=5,width=200,height=200)

        #----------------------------------------------------------------------------------------

        #Button Frame
        btn_frame =Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=1300,y=10,width=150,height=195)


        btn_add=Button(btn_frame, text="Save",command=self.add_data, font=("ariel",15,"bold"), width= 11, bg="blue", fg="white")
        btn_add.grid(row=0,column=0,padx=2,pady=3)

        btn_update=Button(btn_frame, text="Update", font=("ariel",15,"bold"), width= 11, bg="blue", fg="white")
        btn_update.grid(row=1,column=0,padx=2,pady=3)

        btn_delete=Button(btn_frame, text="Delete", font=("ariel",15,"bold"), width= 11, bg="blue", fg="white")
        btn_delete.grid(row=2,column=0,padx=2,pady=3)

        btn_clear=Button(btn_frame, text="Clear", font=("ariel",15,"bold"), width= 11, bg="blue", fg="white")
        btn_clear.grid(row=3,column=0,padx=2,pady=3)

        #-----------------------------------------------------------------------------------------------

        #Down Frame
        down_frame =LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table', font=('times new roman',15,'bold'),fg='red')
        down_frame.place(x=15,y=250,width=1470,height=250)

        #search Frame
        search_frame =LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information', font=('times new roman',15,'bold'),fg='red')
        search_frame.place(x=15,y=0,width=1440,height=70)

        #search
        search_by=Label(search_frame,font=("arial",11,"bold"),text ="Search By:", fg="black", bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=15)

        #search options
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Options","Department","Designation","Name","country","Marital Status","Date of Birth","Date of joining","Contact Number","ID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=15)

        #search entry
        txt_search=ttk.Entry(search_frame,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=15)

        #btn search
        btn_search=Button(search_frame, text="Search", font=("ariel",11,"bold"), width= 11, bg="blue", fg="white")
        btn_search.grid(row=0,column=3,padx=15)

        #btn showall
        btn_showall=Button(search_frame, text="Show all", font=("ariel",11,"bold"), width= 11, bg="blue", fg="white")
        btn_showall.grid(row=0,column=4,padx=15)

        #-------------------------------------------------------------------------------------

        #Employee Table

        #table frame
        table_frame =LabelFrame(down_frame,bd=3,relief=RIDGE,font=('times new roman',15,'bold'))
        table_frame.place(x=15,y=75,width=1440,height=130)

        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        #table
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desig','email','add','marital','dob','doj','idproofcombo','idproof','gender','contact','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #table pack
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        #scroll pack
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        #heading pack
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('add',text='Address')
        self.employee_table.heading('marital',text='Marital Status')
        self.employee_table.heading('dob',text='Date of Birth')
        self.employee_table.heading('doj',text='Date of Joining')
        self.employee_table.heading('idproofcombo',text='ID Proof')
        self.employee_table.heading('idproof',text='ID Number')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('contact',text='Contact Number')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Annual Salary(CTC)')

        self.employee_table['show']='headings'
        #self.employee_table.column("dep",width=100)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    #function

    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" :
            messagebox.showerror('Error!','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Rahul@2203',database='employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('INSERT INTO emp1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)',
                (self.var_dep.get(),
                self.var_name.get(),
                self.var_design.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_marital.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_idproofcomb.get(),
                self.var_idproof.get(),
                self.var_gender.get(),
                self.var_contact.get(),
                self.var_country.get(),
                self.var_salary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Rahul@2203',database='employee_management_system')
        my_cursor=conn.cursor()
        my_cursor.execute('SELECT * FROM emp1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def fet_cursor(self, event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_design.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_marital.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproof.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_contact.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    #Update data
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" :
            messagebox.showerror('Error!','All fields are required')
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update this data?")
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Rahul@2203',database='employee_management_system')
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE emp1 SET Department=%s,
                    Name=%s,
                    Designation=%s,
                    Email=%s,
                    Address=%s,
                    Marital=%s,
                    DOB=%s,
                    DOJ=%s,
                    ID_proof_type=%s,
                    Gender=%s,
                    Phone=%s,
                    Country=%s,
                    Salary=%s
                    where ID_proof=%s,(")






if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()