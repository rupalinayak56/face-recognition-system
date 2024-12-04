from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1580x830+0+0')
        self.root.title('Help Page ')

        img_top=Image.open('./Images/h.jpg')
        img_top=img_top.resize((1500,830),Image.LANCZOS)
        self.photoimgt=ImageTk.PhotoImage(img_top)
        
        fst_lbl=Label(self.root,image=self.photoimgt)
        fst_lbl.place(x=0,y=0,width=1500,height=830)

        des='''
        CONTACT SUPPORT:
        - Email : support@gmail.com
        - phone : +1-800-123-4567
        - Visit our website : https://www.example.com/support
        '''

        h_lbl=Label(fst_lbl,text=des,font=('times in roman',10,'bold'),fg='violet',justify=LEFT)
        h_lbl.place(x=1050,y=700)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()