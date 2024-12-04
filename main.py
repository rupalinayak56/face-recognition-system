from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from student import Student_Details
import os
import tkinter
from train import Train_Data
from face_recognition import Face_Recognition
from attendance import Attendace_System
from developer import Developer_Page
from help import Help
from time import strftime
from datetime import datetime
import time

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1580x830+0+0')
        self.root.title('FACE RECOGNITION SYSTEM ')
        #fst
        img1=Image.open('./Images/img1.jpeg')
        img1=img1.resize((359,170),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        fst_lbl=Label(self.root,image=self.photoimg1)
        fst_lbl.place(x=0,y=0,width=359,height=170)
        #sec
        img2=Image.open('./Images/img4.jpeg')
        img2=img2.resize((359,170),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        fst_lbl=Label(self.root,image=self.photoimg2)
        fst_lbl.place(x=359,y=0,width=359,height=170)
        #third
        img3=Image.open('./Images/img3.jpg')
        img3=img3.resize((359,170),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        fst_lbl=Label(self.root,image=self.photoimg3)
        fst_lbl.place(x=713,y=0,width=359,height=170)
        #fourth
        img4=Image.open('./Images/img5.jpg')
        img4=img4.resize((371,170),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        fst_lbl=Label(self.root,image=self.photoimg4)
        fst_lbl.place(x=1069,y=0,width=371,height=170)

        #background
        img5=Image.open('./Images/bg1.jpg')
        img5=img5.resize((1580,660),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=0,y=170,width=1580,height=660)

        #title
        ttl_lbl=Label(bg_img,text='FACE RECOGNITION ATTENDANCE SOFTWARE SYSTEM',font=('Tahoma',30,'bold'),fg='royalblue')
        ttl_lbl.place(x=0,y=0,width=1580,height=45)

        #showing current time
        def timee():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,timee)

        lbl=Label(ttl_lbl,font=('Arial',14,'bold'),fg='black')
        lbl.place(x=0,y=0,width=120,height=50)
        timee()

        #student details button
        img6=Image.open('./Images/f2.webp')
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.student_details,cursor='hand2')
        b1.place(x=140,y=70,width=220,height=220)

        b1_1=Button(bg_img,text='STUDENT DETAILS',command=self.student_details,cursor='hand2',font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b1_1.place(x=140,y=270,width=221,height=30)

        #faceRecognition
        img7=Image.open('./Images/f4.jpg')
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2=Button(bg_img,image=self.photoimg7,cursor='hand2',command=self.faces_recognition)
        b2.place(x=430,y=70,width=220,height=220)

        b2_1=Button(bg_img,text='FACE DETECTOR',cursor='hand2',font=('Arial',15,'bold'),bg='white',fg='royalblue',command=self.faces_recognition)
        b2_1.place(x=430,y=270,width=221,height=30)

        #ATTENDANCE
        img8=Image.open('./Images/f5.webp')
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b3=Button(bg_img,image=self.photoimg8,command=self.att_system,cursor='hand2')
        b3.place(x=710,y=70,width=220,height=220)

        b3_1=Button(bg_img,text='ATTENDANCE',cursor='hand2',command=self.att_system,font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b3_1.place(x=710,y=270,width=221,height=30)

        #help
        img9=Image.open('./Images/f6.png')
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b4=Button(bg_img,image=self.photoimg9,command=self.he_page,cursor='hand2')
        b4.place(x=990,y=70,width=221,height=220)

        b4_1=Button(bg_img,text='HELP DESK',command=self.he_page,cursor='hand2',font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b4_1.place(x=990,y=270,width=221,height=30)

        #traindata
        img10=Image.open('./Images/img2.jpg')
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b5=Button(bg_img,image=self.photoimg10,command=self.train_data,cursor='hand2')
        b5.place(x=140,y=370,width=220,height=220)

        b5_1=Button(bg_img,text='TRAIN DATA',cursor='hand2',command=self.train_data,font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b5_1.place(x=140,y=570,width=221,height=30)

        #photos
        img11=Image.open('./Images/f7.jpg')
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b6=Button(bg_img,image=self.photoimg11,cursor='hand2',command=self.open_img)
        b6.place(x=430,y=370,width=220,height=220)

        b6_1=Button(bg_img,text='PHOTOS',cursor='hand2',command=self.open_img,font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b6_1.place(x=430,y=570,width=221,height=30)

        #developer
        img12=Image.open('./Images/dev.jpg')
        img12=img12.resize((220,220),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b7=Button(bg_img,image=self.photoimg12,command=self.dev_page,cursor='hand2')
        b7.place(x=710,y=370,width=220,height=220)

        b7_1=Button(bg_img,text='DEVELOPER',command=self.dev_page,cursor='hand2',font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b7_1.place(x=710,y=570,width=221,height=30)

        #EXIT
        img13=Image.open('./Images/f9.jpg')
        img13=img13.resize((220,220),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b8=Button(bg_img,image=self.photoimg13,command=self.iexit,cursor='hand2')
        b8.place(x=990,y=370,width=220,height=220)

        b8_1=Button(bg_img,text='EXIT',cursor='hand2',command=self.iexit,font=('Arial',15,'bold'),bg='white',fg='royalblue')
        b8_1.place(x=990,y=570,width=221,height=30)
    #for photos button
    def open_img(self):
        os.startfile('data_img')
    
    #exit btn

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno('Face Recognition','Are You Sure To Exit This Project',parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return

    #function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Details(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)
    
    def faces_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def att_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendace_System(self.new_window)

    def dev_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer_Page(self.new_window)
    
    def he_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        













        

        
        


if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()