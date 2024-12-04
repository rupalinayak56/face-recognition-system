from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from cv2.face import LBPHFaceRecognizer_create
import csv
from tkinter import filedialog

mydata=[] #for storing csv file data
class Attendace_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1580x830+0+0')
        self.root.title('Attendace')

        #for showing data on table
        self.var_att_NAME=StringVar()
        self.var_att_ID=StringVar()
        self.var_att_ROLL=StringVar()
        self.var_att_DEPT=StringVar()
        self.var_att_TIME=StringVar()
        self.var_att_DATE=StringVar()
        self.var_att_STATUS=StringVar()












        #img1
        img_1=Image.open('./Images/s6.jpg')
        img_1=img_1.resize((730,180),Image.LANCZOS)
        self.photoimga1=ImageTk.PhotoImage(img_1)

        fst_label=Label(self.root,image=self.photoimga1)
        fst_label.place(x=0,y=0,width=730,height=180)

        #img2
        img_2=Image.open('./Images/s2.jpg')
        img_2=img_2.resize((780,180),Image.LANCZOS)
        self.photoimga2=ImageTk.PhotoImage(img_2)

        fst_label2=Label(self.root,image=self.photoimga2)
        fst_label2.place(x=720,y=0,width=780,height=180)

        #title
        title_lbl=Label(self.root,text='STUDENT ATTENDANCE MANAGEMENT SYSTEM',font=('Arial',25,'bold'),bg='royalblue',fg='white',width=1530)
        title_lbl.place(x=0,y=181,width=1530,height=40)

        #bg
        img3=Image.open('./Images/bg1.jpg')
        img3=img3.resize((1580,640),Image.LANCZOS)
        self.photoimga3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimga3)
        bg_img.place(x=0,y=220,width=1580,height=640)

        #main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=5,width=1530,height=590)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Attendance Details',font=('arial',12,'bold'),bg='white',fg='green')
        left_frame.place(x=10,y=10,width=720,height=565)

        left_img=Image.open('./Images/f7.jpg')
        left_img=left_img.resize((715,155),Image.LANCZOS)
        self.photoimgl=ImageTk.PhotoImage(left_img)
        
        fst_lbl=Label(left_frame,image=self.photoimgl)
        fst_lbl.place(x=0,y=0,width=715,height=155)

        inner_frame=LabelFrame(left_frame,bd=2,bg='white')
        inner_frame.place(x=5,y=160,width=710,height=360)

        #STUDENT ID
        std_id=Label(inner_frame,text='Student Id:',font=('arial',12,'bold'),bg='white')
        std_id.grid(row=0,column=2,sticky=W,padx=10)

        std_entry=ttk.Entry(inner_frame,textvariable=self.var_att_ID,width=20,font=('arial',12,'bold'))
        std_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #roll
        roll=Label(inner_frame,text='Roll No:',font=('arial',12,'bold'),bg='white')
        roll.grid(row=1,column=0,sticky=W,padx=10)

        roll_entry=ttk.Entry(inner_frame,textvariable=self.var_att_ROLL,width=20,font=('arial',12,'bold'))
        roll_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        #name
        name=Label(inner_frame,text='Name:',font=('arial',12,'bold'),bg='white')
        name.grid(row=0,column=0,sticky=W,padx=10)

        name_entry=ttk.Entry(inner_frame,textvariable=self.var_att_NAME,width=20,font=('arial',12,'bold'))
        name_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #department
        dept=Label(inner_frame,text='Department:',font=('arial',12,'bold'),bg='white')
        dept.grid(row=1,column=2,sticky=W,padx=10)

        dept_entry=ttk.Entry(inner_frame,textvariable=self.var_att_DEPT,width=20,font=('arial',12,'bold'))
        dept_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #time
        time=Label(inner_frame,text='Time:',font=('arial',12,'bold'),bg='white')
        time.grid(row=2,column=0,sticky=W,padx=10)

        time_entry=ttk.Entry(inner_frame,textvariable=self.var_att_TIME,width=20,font=('arial',12,'bold'))
        time_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        #date
        date=Label(inner_frame,text='Date:',font=('arial',12,'bold'),bg='white')
        date.grid(row=2,column=2,sticky=W,padx=10)

        date_entry=ttk.Entry(inner_frame,textvariable=self.var_att_DATE,width=20,font=('arial',12,'bold'))
        date_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        
        #attendance
        att=Label(inner_frame,text='Attendance Status:',font=('arial',12,'bold'),bg='white')
        att.grid(row=3,column=0,sticky=W,padx=10)

        att_combo=ttk.Combobox(inner_frame,font=('arial',12,'bold'),state='readonly',textvariable=self.var_att_STATUS,width=20)
        att_combo['values']=('Status','Present','Absent')
        att_combo.current(0)
        att_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #BUTTONFRAME
        btn_frame=Frame(inner_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=235,width=704,height=34)

        import_btn=Button(btn_frame,text='Import CSV',command=self.import_csv,font=('Arial',12,'bold'),bg='blue',fg='white',width=17)
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,text='Export CSV',command=self.export_csv,font=('Arial',12,'bold'),bg='blue',fg='white',width=17)
        export_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text='Update',command=self.update_data,font=('Arial',12,'bold'),bg='blue',fg='white',width=16)
        update_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_datas,font=('Arial',12,'bold'),bg='blue',fg='white',width=16)
        reset_btn.grid(row=0,column=3)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Attendance Details',font=('arial',12,'bold'),bg='white',fg='green')
        right_frame.place(x=732,y=10,width=680,height=565)

        inner_frame1=LabelFrame(right_frame,bd=2,bg='white')
        inner_frame1.place(x=5,y=5,width=670,height=520)


        #SCROLL BAR
        scroll_x=ttk.Scrollbar(inner_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(inner_frame1,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(inner_frame1,column=('NAME','ID','ROLL_NO','DEPARTMENT','TIME','DATE','ATTENDANCE_STATUS'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        #creating and setup treeview(table)
        self.AttendanceReportTable.heading('NAME',text='NAME')
        self.AttendanceReportTable.heading('ID',text='ID')
        self.AttendanceReportTable.heading('ROLL_NO',text='ROLL_NO')
        self.AttendanceReportTable.heading('DEPARTMENT',text='DEPARTMENT')
        self.AttendanceReportTable.heading('TIME',text='TIME')
        self.AttendanceReportTable.heading('DATE',text='DATE')
        self.AttendanceReportTable.heading('ATTENDANCE_STATUS',text='ATTENDANCE_STATUS')

        #set column props
        self.AttendanceReportTable['show']='headings'
        self.AttendanceReportTable.column('NAME', width=150, anchor='center')
        self.AttendanceReportTable.column('ID', width=100, anchor='center')
        self.AttendanceReportTable.column('ROLL_NO', width=100, anchor='center')
        self.AttendanceReportTable.column('DEPARTMENT', width=100, anchor='center')
        self.AttendanceReportTable.column('TIME', width=100, anchor='center')
        self.AttendanceReportTable.column('DATE', width=100, anchor='center')
        self.AttendanceReportTable.column('ATTENDANCE_STATUS', width=150, anchor='center')
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.get_cursor)

        #fetchdata for import csv btn
    def fetching_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)
    #import_csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV file','*.csv'),('All File','*.*')),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetching_data(mydata)
    #export data btn function
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('NO DATA','NO data found to export',parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV file','*.csv'),('All File','*.*')),parent=self.root)
            with open(fln,mode='w',newline='') as myfiles:
                export_write=csv.writer(myfiles,delimiter=',')
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo('data exported','Your Data Exported to '+ os.path.basename(fln) + ' Successfully')
        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

    #get_cursor and showing it in entry field

    def get_cursor(self,event=''):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_att_NAME.set(rows[0])
        self.var_att_ID.set(rows[1])
        self.var_att_ROLL.set(rows[2])
        self.var_att_DEPT.set(rows[3])
        self.var_att_TIME.set(rows[4])
        self.var_att_DATE.set(rows[5])
        self.var_att_STATUS.set(rows[6])

        #we need to bind 188 line
    #for reset data

    def update_data(self):
        try:
            # Get the updated data from the entry fields

            name = self.var_att_NAME.get()
            std_id = self.var_att_ID.get()
            roll_no = self.var_att_ROLL.get()
            dept = self.var_att_DEPT.get()
            time = self.var_att_TIME.get()
            date = self.var_att_DATE.get()
            status = self.var_att_STATUS.get()

            #get the selected row
            selected_row = self.AttendanceReportTable.focus()
            if not selected_row:
                messagebox.showerror("Select Row", "Please select a row to update")
                return

            # Update the selected row in the Treeview
            self.AttendanceReportTable.item(selected_row, values=(name, std_id, roll_no, dept, time, date, status))

            # Optionally, reset fields after update
            self.reset_datas()
            messagebox.showinfo("Updated", "Data updated successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while updating: {str(e)}")




    def reset_datas(self):
        self.var_att_NAME.set('')
        self.var_att_ID.set('')
        self.var_att_ROLL.set('')
        self.var_att_DEPT.set('')
        self.var_att_TIME.set('')
        self.var_att_DATE.set('')
        self.var_att_STATUS.set('')    








        

        


























if __name__=='__main__':
    root=Tk()
    obj=Attendace_System(root)
    root.mainloop()
