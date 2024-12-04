from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os #for storing face images in data folder
import numpy as np
from cv2.face import LBPHFaceRecognizer_create



class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1580x830+0+0')
        self.root.title('Train Data ')

        #title
        ttl_lbl=Label(self.root,text='Photo Sample Training',font=('times new roman',30,'bold'),bg='blue',fg='gold')
        ttl_lbl.place(x=0,y=0,width=1530,height=45)

        #top img
        img_top=Image.open('./Images/img6.png')
        img_top=img_top.resize((1500,300),Image.LANCZOS)
        self.photoimgt=ImageTk.PhotoImage(img_top)
        
        fst_lbl=Label(self.root,image=self.photoimgt)
        fst_lbl.place(x=0,y=45,width=1500,height=300)

        #button
        btn=Button(self.root,text='TRAIN DATA',command=self.train_classifier,font=('times new roman',25,'bold'),bg='blue',fg='gold',cursor='hand2')
        btn.place(x=0,y=342,width=1530,height=50)

        #btmimg
        img_btm=Image.open('./Images/img7.jpeg')
        img_btm=img_btm.resize((1450,430),Image.LANCZOS)
        self.photoimgbtm=ImageTk.PhotoImage(img_btm)
        
        fst_lbl=Label(self.root,image=self.photoimgbtm)
        fst_lbl.place(x=0,y=400,width=1450,height=430)
    #traning the imagedata    
    def train_classifier(self):
        data_dir=('data_img')
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for img in path:
            image=Image.open(img).convert('L') # converting Gray Scale img
            imagenp=np.array(image,'uint8')
            #from path we are taking id
            id=int(os.path.split(img)[1].split('.')[1])
            # D:\PYTHON PROJECT\FACE RECOGNITION STUDENT ATTENDANCE SYSTEM\imagedata\user.2.1.jpg(.split('.'[1])==id(so id =2))
            #from here to                             index-0               to here ||  index-1                   
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow('Training',imagenp)
            cv2.waitKey(1)==13 #click enter to close window
        ids=np.array(ids)

        #train the classifier and save
        clf = LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        #after training we need to store into a file
        clf.write('classifier.xml')
        #destroy the window
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Training Dataset Completed',parent=self.root)


















if __name__=='__main__':
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()