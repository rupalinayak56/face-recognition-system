from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os #for storing face images in data folder
import time

class Student_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1580x830+0+0')
        self.root.title('Student Details ')
        #text var for add_dat function
        self.var_DEPT=StringVar()
        self.var_COURSE=StringVar()
        self.var_YEAR=StringVar()
        self.var_SEM=StringVar()
        self.var_ID=StringVar()
        self.var_NAME=StringVar()
        self.var_DIV=StringVar()
        self.var_ROLLNO=StringVar()
        self.var_GENDER=StringVar()
        self.var_DOB=StringVar()
        self.var_EMAIL=StringVar()
        self.var_PHONENO=StringVar()
        self.var_ADDRESS=StringVar()
        self.var_TEACHER=StringVar()
       

        #fst
        img1=Image.open('./Images/f7.jpg')
        img1=img1.resize((359,150),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        fst_lbl=Label(self.root,image=self.photoimg1)
        fst_lbl.place(x=0,y=0,width=359,height=150)
        #sec
        img2=Image.open('./Images/s1.webp')
        img2=img2.resize((359,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        fst_lbl=Label(self.root,image=self.photoimg2)
        fst_lbl.place(x=359,y=0,width=359,height=150)
        #third
        img3=Image.open('./Images/s5.jpg')
        img3=img3.resize((450,170),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        fst_lbl=Label(self.root,image=self.photoimg3)
        fst_lbl.place(x=713,y=0,width=359,height=150)
        #fourth
        img4=Image.open('./Images/s2.jpg')
        img4=img4.resize((371,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        fst_lbl=Label(self.root,image=self.photoimg4)
        fst_lbl.place(x=1069,y=0,width=371,height=150)

        #background
        img5=Image.open('./Images/bg1.jpg')
        img5=img5.resize((1580,640),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=0,y=170,width=1580,height=640)

        #title
        ttl_lbl=Label(bg_img,text='STUDENT MANAGEMENT SYSTEM',font=('Arial',25,'bold'),fg='white',bg='royalblue')
        ttl_lbl.place(x=0,y=0,width=1590,height=35)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=40,width=1550,height=590)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Information',font=('arial',12,'bold'),bg='white',fg='blue')
        left_frame.place(x=10,y=10,width=720,height=565)

        left_img=Image.open('./Images/s6.jpg')
        left_img=left_img.resize((720,100),Image.LANCZOS)
        self.photoimgl=ImageTk.PhotoImage(left_img)
        
        fst_lbl=Label(left_frame,image=self.photoimgl)
        fst_lbl.place(x=0,y=0,width=715,height=100)

        #CURRENTCOURSE
        current_course=LabelFrame(left_frame,bd=2,relief=RIDGE,text='Current Course Information',font=('arial',12,'bold'),bg='white',fg='blue')
        current_course.place(x=5,y=100,width=710,height=100)

        #department
        dep_label=Label(current_course,text='Department',font=('arial',12,'bold'),bg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_DEPT,font=('arial',12,'bold'),state='readonly',width=20)
        dep_combo['values']=('Select Department','CSE','MECH','CIVIL','EEE','ECE','EE')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #course
        course_label=Label(current_course,text='Course',font=('arial',12,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_COURSE,font=('arial',12,'bold'),state='readonly',width=20)
        course_combo['values']=('Select Course','BTECH','MCA','MBA','MTECH')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #year
        year_label=Label(current_course,text='Year',font=('arial',12,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_YEAR,font=('arial',12,'bold'),state='readonly',width=20)
        year_combo['values']=('Select Year','2020-21','2021-22','2022-23','2023-24')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #semester
        sem_label=Label(current_course,text='Semester',font=('arial',12,'bold'),bg='white')
        sem_label.grid(row=1,column=2,padx=5,sticky=W)

        sem_combo=ttk.Combobox(current_course,textvariable=self.var_SEM,font=('arial',12,'bold'),state='readonly',width=20)
        sem_combo['values']=('Select Semester','SEM-1','SEM-2','SEM-3','SEM-4','SEM-5','SEM-6','SEM-7','SEM-8')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #CLASS STUDENT INFORMATION
        std_info_label=LabelFrame(left_frame,bd=2,relief=RIDGE,text='Class Student Information',font=('arial',12,'bold'),bg='white',fg='blue')
        std_info_label.place(x=5,y=205,width=710,height=325)

        #studentid
        std_id=Label(std_info_label,text='StudentId No:',font=('arial',12,'bold'),bg='white')
        std_id.grid(row=0,column=0,sticky=W,padx=10)

        std_entry=ttk.Entry(std_info_label,textvariable=self.var_ID,width=20,font=('arial',12,'bold'))
        std_entry.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #studentname
        std_name=Label(std_info_label,text='Student Name:',font=('arial',12,'bold'),bg='white')
        std_name.grid(row=0,column=2,sticky=W,padx=10)

        std_entry=ttk.Entry(std_info_label,textvariable=self.var_NAME,width=20,font=('arial',12,'bold'))
        std_entry.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #classdivision
        class_div=Label(std_info_label,text='Class Division:',font=('arial',12,'bold'),bg='white')
        class_div.grid(row=1,column=0,sticky=W,padx=10)
        
        div_combo=ttk.Combobox(std_info_label,textvariable=self.var_DIV,font=('arial',12,'bold'),state='readonly',width=20)
        div_combo['values']=('Select Division','A','B','C','D')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #rollno
        roll_no=Label(std_info_label,text='Roll No:',font=('arial',12,'bold'),bg='white')
        roll_no.grid(row=1,column=2,sticky=W,padx=10)

        roll_entry=ttk.Entry(std_info_label,textvariable=self.var_ROLLNO,width=20,font=('arial',12,'bold'))
        roll_entry.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #gender
        gender=Label(std_info_label,text='Gender:',font=('arial',12,'bold'),bg='white')
        gender.grid(row=2,column=0,sticky=W,padx=10)
        
        gender_combo=ttk.Combobox(std_info_label,textvariable=self.var_GENDER,font=('arial',12,'bold'),state='readonly',width=20)
        gender_combo['values']=('Select Gender','MALE','FEMALE','OTHER')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        
        #dob
        dob=Label(std_info_label,text='DOB:',font=('arial',12,'bold'),bg='white')
        dob.grid(row=2,column=2,sticky=W,padx=10)

        dob_entry=ttk.Entry(std_info_label,textvariable=self.var_DOB,width=20,font=('arial',12,'bold'))
        dob_entry.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #email
        email=Label(std_info_label,text='Email Id:',font=('arial',12,'bold'),bg='white')
        email.grid(row=3,column=0,sticky=W,padx=10)

        email_entry=ttk.Entry(std_info_label,textvariable=self.var_EMAIL,width=20,font=('arial',12,'bold'))
        email_entry.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #number
        phn_no=Label(std_info_label,text='Phone No:',font=('arial',12,'bold'),bg='white')
        phn_no.grid(row=3,column=2,sticky=W,padx=10)

        phn_entry=ttk.Entry(std_info_label,textvariable=self.var_PHONENO,width=20,font=('arial',12,'bold'))
        phn_entry.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        #address
        add=Label(std_info_label,text='Address:',font=('arial',12,'bold'),bg='white')
        add.grid(row=4,column=0,sticky=W,padx=10)

        add_entry=ttk.Entry(std_info_label,textvariable=self.var_ADDRESS,width=20,font=('arial',12,'bold'))
        add_entry.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        #teachername
        teacher_name=Label(std_info_label,text='Teacher Name:',font=('arial',12,'bold'),bg='white')
        teacher_name.grid(row=4,column=2,sticky=W,padx=10)

        teacher_entry=ttk.Entry(std_info_label,textvariable=self.var_TEACHER,width=20,font=('arial',12,'bold'))
        teacher_entry.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(std_info_label,variable=self.var_radio1,text="Take Photo Sample",value='Yes')
        radiobtn1.grid(row=5,column=0,padx=2,pady=5)

        radiobtn2=ttk.Radiobutton(std_info_label,variable=self.var_radio1,text="No Photo Sample",value='No')
        radiobtn2.grid(row=5,column=1,padx=2,pady=5)

        #BUTTONFRAME
        btn_frame=Frame(std_info_label,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=228,width=704,height=34)

        save_btn=Button(btn_frame,text='Save',command=self.add_data,font=('Arial',12,'bold'),bg='royalblue',fg='white',width=17)
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text='Update',command=self.update_data,font=('Arial',12,'bold'),bg='green',fg='white',width=17)
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,text='Delete',command=self.delete_data,font=('Arial',12,'bold'),bg='red',fg='white',width=17)
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,font=('Arial',12,'bold'),bg='blue',fg='white',width=17)
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(std_info_label,bd=2,relief=RIDGE)
        btn_frame2.place(x=0,y=262,width=704,height=34)

        take_photo_btn=Button(btn_frame2,text='Take Photo Sample',command=self.generate_dataset,font=('Arial',12,'bold'),bg='blue',fg='white',width=35)
        take_photo_btn.grid(row=1,column=0)
        update_photo_btn=Button(btn_frame2,text='Update Photo Sample',font=('Arial',12,'bold'),bg='green',fg='white',width=35)
        update_photo_btn.grid(row=1,column=1)

        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Details',font=('arial',12,'bold'),bg='white',fg='blue')
        right_frame.place(x=740,y=10,width=666,height=565)

        right_img=Image.open('./Images/s7.jpg')
        right_img=right_img.resize((715,130),Image.LANCZOS)
        self.photoimgr=ImageTk.PhotoImage(right_img)
        
        fst_lbl=Label(right_frame,image=self.photoimgr)
        fst_lbl.place(x=0,y=0,width=715,height=130)

        #SEARCH BY SYSTEM
        Search_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text='View Student Details & Search System',font=('Arial',12,'bold'),fg='blue')
        Search_frame.place(x=5,y=135,width=655,height=70)

        search_opt=Label(Search_frame,text='Search By:',font=('Arial',12,'bold'),bg='white')
        search_opt.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        search_combo=ttk.Combobox(Search_frame,font=('Arial',12,'bold'),state='readonly',width=18)
        search_combo['value']=('Select','Roll No','Phone No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=7)
        
        search_entry=ttk.Entry(Search_frame,font=('Arial',12,'bold'),width=18)
        search_entry.grid(row=0,column=2,padx=2,pady=7)

        search_opt2=Label(Search_frame,text='SEARCH',font=('Arial',12,'bold'),bg='green',fg='white')
        search_opt2.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        show=Label(Search_frame,text='SHOW ALL',font=('Arial',12,'bold'),bg='royalblue',fg='white')
        show.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        
        #TABLEFRAME
        table_frame=Frame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=210,width=655,height=300)

        #for scrolling
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        #creating table
        self.student_table=ttk.Treeview(table_frame,column=('DEPT','COURSE','YEAR','SEM','ID','NAME','DIV','ROLLNO','GENDER','DOB','EMAIL','PHONENO','ADDRESS','TEACHER','PHOTO'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #hear i am packing the scrollbars of x and y axis
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        #scroll_x.config(command=self.student_table.xview): This configures the horizontal scrollbar (scroll_x) to communicate with the table (self.student_table) so that when you scroll the scrollbar, it will move horizontally across the content of the table (or any widget you have linked with it).
        #self.student_table.xview: The xview method of a widget (like a Treeview table, Canvas, or other scrollable widgets) returns a way to control the horizontal scrolling. The xview method of the widget takes a value representing how far the content should scroll horizontally, and it also returns the range of scrolling (how much content can be scrolled).
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading('DEPT',text='DEPARTMENT')
        self.student_table.heading('COURSE',text='COURSE')
        self.student_table.heading('YEAR',text='YEAR')
        self.student_table.heading('SEM',text='SEMESTER')
        self.student_table.heading('ID',text='STUDENT ID')
        self.student_table.heading('NAME',text='STUDENT NAME ')
        self.student_table.heading('DIV',text='DIVISION')
        self.student_table.heading('ROLLNO',text='ROLL NO')
        self.student_table.heading('GENDER',text='GENDER')

        self.student_table.heading('DOB',text='DOB')
        self.student_table.heading('EMAIL',text='EMAIL')
        self.student_table.heading('PHONENO',text='PHONE NO')
        self.student_table.heading('ADDRESS',text='ADDRESS')
        self.student_table.heading('TEACHER',text='TEACHER')
        self.student_table.heading('PHOTO',text='PHOTO SAMPLE STATUS')
        self.student_table['show']='headings'
        #width set
        self.student_table.column('DEPT',width=150)
        self.student_table.column('COURSE',width=150)
        self.student_table.column('YEAR',width=150)
        self.student_table.column('SEM',width=150)
        self.student_table.column('ID',width=150)
        self.student_table.column('NAME',width=150)
        self.student_table.column('DIV',width=150)
        self.student_table.column('ROLLNO',width=150)
        self.student_table.column('GENDER',width=150)

        self.student_table.column('DOB',width=150)
        self.student_table.column('EMAIL',width=150)
        self.student_table.column('PHONENO',width=150)
        self.student_table.column('ADDRESS',width=150)
        self.student_table.column('TEACHER',width=150)
        self.student_table.column('PHOTO',width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()
    #creating function for data adding
    def add_data(self):
        #validation in entryfield
        if self.var_DEPT.get()=='Select Department' or self.var_NAME.get()=='' or self.var_ID.get()=='':
            #msgbox(error)
            messagebox.showerror('Error','All Fields are required',parent=self.root)

        else:
            # messagebox.showinfo('success','Successfully Saved')
            # for adding data we need to create database (go to mysql workbench)
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_DEPT.get(),
                                                                                                                self.var_COURSE.get(),
                                                                                                                self.var_YEAR.get(),
                                                                                                                self.var_SEM.get(),
                                                                                                                self.var_ID.get(),
                                                                                                                self.var_NAME.get(),
                                                                                                                self.var_DIV.get(),
                                                                                                                self.var_ROLLNO.get(),
                                                                                                                self.var_GENDER.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_EMAIL.get(),
                                                                                                                self.var_PHONENO.get(),
                                                                                                                self.var_ADDRESS.get(),
                                                                                                                self.var_TEACHER.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Student Details Has Been Added Successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('error',f'Due to :{str(es)}',parent=self.root)

    #fetching data in student table
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognition')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from student')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
            conn.close()
    #get_cursor
    def get_cursor(self,event=''):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']
        self.var_DEPT.set(data[0]),
        self.var_COURSE.set(data[1]),
        self.var_YEAR.set(data[2]),
        self.var_SEM.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_NAME.set(data[5]),
        self.var_DIV.set(data[6]),
        self.var_ROLLNO.set(data[7]),
        self.var_GENDER.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_EMAIL.set(data[10]),
        self.var_PHONENO.set(data[11]),
        self.var_ADDRESS.set(data[12]),
        self.var_TEACHER.set(data[13]),
        self.var_radio1.set(data[14])
    #update
    def update_data(self):
        #validation in entryfield
        if self.var_DEPT.get()=='Select Department' or self.var_NAME.get()=='' or self.var_ID.get()=='':
            #msgbox(error)
            messagebox.showerror('Error','All Fields are required',parent=self.root)
        else:
            try:
                Update=messagebox.askyesno('Update','Do You want to update this student details',parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognition')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set DEPT=%s,COURSE=%s,YEAR=%s,SEM=%s,NAME=%s,`DIV`=%s,`ROLL NO`=%s,`GENDER`=%s,DOB=%s,EMAIL=%s,`PHONE NO`=%s,ADDRESS=%s,TEACHER=%s,PHOTO=%s where ID=%s",(
                                                                                                                                                                                                        self.var_DEPT.get(),
                                                                                                                                                                                                        self.var_COURSE.get(),
                                                                                                                                                                                                        self.var_YEAR.get(),
                                                                                                                                                                                                        self.var_SEM.get(),
                                                                                                                                                                                                        self.var_NAME.get(),
                                                                                                                                                                                                        self.var_DIV.get(),
                                                                                                                                                                                                        self.var_ROLLNO.get(),
                                                                                                                                                                                                        self.var_GENDER.get(),
                                                                                                                                                                                                        self.var_DOB.get(),
                                                                                                                                                                                                        self.var_EMAIL.get(),
                                                                                                                                                                                                        self.var_PHONENO.get(),
                                                                                                                                                                                                        self.var_ADDRESS.get(),
                                                                                                                                                                                                        self.var_TEACHER.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_ID.get() 
                                                                                                                                                                                                        ))                                                                                                                                                                                                      

                                                                                                                                                                                                    
                else:
                    if not Update:
                        return
                messagebox.showinfo('success','Student Details Successfully Updated',parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()          
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root) 
                                                                                                                                                                                                  
    #delete
    def delete_data(self):
        if self.var_ID.get=='':
            messagebox.showerror('Error','Student Id must be required',parent=self.root)
        else:
            try:
                delete=messagebox.askyesno('Student Delete Page','Do You Want To Delete This Student',parent=self.root) 
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognition')
                    my_cursor=conn.cursor()
                    sql='delete from student where ID=%s'
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Successfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)
    
    #reset
    def reset_data(self):
        self.var_DEPT.set('Select Department'),
        self.var_COURSE.set('Select Course'),
        self.var_YEAR.set('Select Year'),
        self.var_SEM.set('Select Semester'),
        self.var_ID.set(''),
        self.var_NAME.set(''),
        self.var_DIV.set('Select Division'),
        self.var_ROLLNO.set(''),
        self.var_GENDER.set('Select Gender'),
        self.var_DOB.set(''),
        self.var_EMAIL.set(''),
        self.var_PHONENO.set(''),
        self.var_ADDRESS.set(''),
        self.var_TEACHER.set(''),
        self.var_radio1.set('')
    

    def generate_dataset(self):
        if self.var_DEPT.get() == 'Select Department' or self.var_NAME.get() == '' or self.var_ID.get() == '':
            messagebox.showerror('Error', 'All Fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognition')
                my_cursor = conn.cursor()

                # Use the ID from the form
                student_id = self.var_ID.get()  # Get the student ID directly from the form
                my_cursor.execute("UPDATE student SET DEPT=%s, COURSE=%s, YEAR=%s, SEM=%s, NAME=%s, `DIV`=%s, `ROLL NO`=%s, `GENDER`=%s, DOB=%s, EMAIL=%s, `PHONE NO`=%s, ADDRESS=%s, TEACHER=%s, PHOTO=%s WHERE ID=%s", (
                    self.var_DEPT.get(),
                    self.var_COURSE.get(),
                    self.var_YEAR.get(),
                    self.var_SEM.get(),
                    self.var_NAME.get(),
                    self.var_DIV.get(),
                    self.var_ROLLNO.get(),
                    self.var_GENDER.get(),
                    self.var_DOB.get(),
                    self.var_EMAIL.get(),
                    self.var_PHONENO.get(),
                    self.var_ADDRESS.get(),
                    self.var_TEACHER.get(),
                    self.var_radio1.get(),
                    student_id  # Use the ID from the form
                ))
                conn.commit()
                self.fetch_data()  # Assuming this is a method to refresh data
                self.reset_data()  # Assuming this resets the input fields
                conn.close()

                # Load predefined face detection data from OpenCV
                face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
                    return None  # Return None if no face is detected

                # Open camera
                cap = cv2.VideoCapture(0)  # Use the default webcam
                img_id = 0  # Set initial image id to 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # # Generate a unique filename using student ID and img_id
                        # timestamp = int(time.time())  # Use timestamp to ensure unique filenames
                        # file_name_path = f'data_img/user.{student_id}.{timestamp}_{img_id}.jpg'
                        file_name_path = f'data_img/user.{student_id}.{img_id}.jpg'

                        cv2.imwrite(file_name_path, face)

                        # Display the image being captured
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow('Cropped Face', face)

                    if cv2.waitKey(1) == 13 or img_id >= 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Generating Datasets Completed!')

            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    #generate data set or take photo sample
#     def generate_dataset(self):
#         if self.var_DEPT.get()=='Select Department' or self.var_NAME.get()=='' or self.var_ID.get()=='':
#             #msgbox(error)
#             messagebox.showerror('Error','All Fields are required',parent=self.root)
#         else:
#             try:
#                 conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognition')
#                 my_cursor=conn.cursor()
#                 my_cursor.execute('select * from student')
#                 myresult=my_cursor.fetchall()
#                 id=0
#                 for x in myresult:
#                     id+=1
#                 my_cursor.execute("update student set DEPT=%s,COURSE=%s,YEAR=%s,SEM=%s,NAME=%s,`DIV`=%s,`ROLL NO`=%s,`GENDER`=%s,DOB=%s,EMAIL=%s,`PHONE NO`=%s,ADDRESS=%s,TEACHER=%s,PHOTO=%s where ID=%s",(
#                                                                                                                                                                                                          self.var_DEPT.get(),
#                                                                                                                                                                                                          self.var_COURSE.get(),
#                                                                                                                                                                                                          self.var_YEAR.get(),
#                                                                                                                                                                                                          self.var_SEM.get(),
#                                                                                                                                                                                                          self.var_NAME.get(),
#                                                                                                                                                                                                          self.var_DIV.get(),
#                                                                                                                                                                                                          self.var_ROLLNO.get(),
#                                                                                                                                                                                                          self.var_GENDER.get(),
#                                                                                                                                                                                                          self.var_DOB.get(),
#                                                                                                                                                                                                          self.var_EMAIL.get(),
#                                                                                                                                                                                                          self.var_PHONENO.get(),
#                                                                                                                                                                                                          self.var_ADDRESS.get(),
#                                                                                                                                                                                                          self.var_TEACHER.get(),
#                                                                                                                                                                                                          self.var_radio1.get(),
#                                                                                                                                                                                                          self.var_ID.get()
#                                                                                                                                                                                                          ))                                                                                                                                                                                                      
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()
#                 #load predefined data on face frontals from opencv
#                 face_classifier=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
                
#                 def face_cropped(img):
#                     #chnging color of photo(red,green,bluee.....) to gray
#                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                     #scaling factor=1.3,min neighbour=5
#                     faces=face_classifier.detectMultiScale(gray,1.3,5)

#                     for(x,y,w,h) in faces:
#                         face_cropped=img[y:y+h,x:x+w]
#                         return face_cropped
#                 #for opening camera
#                 cap=cv2.VideoCapture(0) #webcamera=0
#                 img_id=0 #want to capture 100 images
#                 while True:
#                     ret,my_frame=cap.read()
#                     if face_cropped(my_frame) is not None:
#                         img_id+=1
#                         face=cv2.resize(face_cropped(my_frame),(450,450))
#                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
#                         #storing images
#                         # file_name_path='data_img/user.'+str(id)+'.'+str(img_id)+'.jpg'
#                         # Create unique filename using current time to avoid overwriting
#                         timestamp = int(time.time())  # Use timestamp for unique filenames
#                         file_name_path = f'data_img/user.{id}.{timestamp}_{img_id}.jpg'
#                         cv2.imwrite(file_name_path,face)
#                         # 2=font scale,(0,255,0)=font color(last=255),thickness text=2,origin=(50,50)
#                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                         cv2.imshow('Cropped Face',face)
#                     #waitkey function use to delay
#                     if cv2.waitKey(1)==13 or int(img_id)==100:
#                         break

#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo('result','Generating Datasets Completed!!')
#             except Exception as es:
#                 messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)



# if __name__=='__main__':
#     root=Tk()
#     obj=Student_Details(root)
#     root.mainloop()        

if __name__=='__main__':
     root=Tk()
     obj=Student_Details(root)
     root.mainloop()        
        




