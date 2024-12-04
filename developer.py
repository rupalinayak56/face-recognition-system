from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser

class Developer_Page:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1580x830+0+0')  
        self.root.title('About Developer')  

        ttl_lbl = Label(self.root, text='DEVELOPER PAGE', font=('times new roman', 25, 'bold'), bg='#2d3e50', fg='white')
        ttl_lbl.place(x=0, y=0, width=1530, height=45)  

        main_frame=Frame(self.root,bg='white',bd=1)
        main_frame.place(x=0,y=40,width=1530,height=740)

        #img
        my_img=Image.open('./Images/girl.jpg')
        my_img=my_img.resize((200,200),Image.LANCZOS)
        self.photoimgg=ImageTk.PhotoImage(my_img)

        im=Label(main_frame,image=self.photoimgg,bg='white')
        im.place(x=1210,y=0,width=200,height=200)
        # Footer Section
        footer_frame = Frame(self.root, bg='#2d3e50', bd=2)
        footer_frame.place(x=0, y=780, width=1530, height=50)

        footer_lbl = Label(footer_frame, text="© 2024 | All rights reserved.", font=("Helvetica", 14), fg='white', bg='#2d3e50')
        footer_lbl.place(x=600, y=10)

         # Developer Information
        about_text = """
        I am Rupali Nayak and an aspiring software developer with a strong foundation in programming and a genuine
        passion for technology and I have knowladge on Python, Django Framework, Flask Web-Framework,
        Webtechnologies and Sql.

        I have worked on a variety of academic projects including a web-based e-commerce site and a weather
        forecasting app. 

        These projects have given me practical experience with front-end and back-end technologies, as well as
        databases like MySql. 

        I am always excited to learn new tools and frameworks to enhance my skill set.
        My ultimate goal is to develop software that can solve real-world problems while continually improving as a developer."

        Contact Information:
        - Email: rupalinayak7789@gmail.com
        - GitHub: https://github.com/rupalinayak56
        - LinkedIn: https://www.linkedin.com/in/rupali-nayak-6162a230a/

        """
        about_lbl = Label(main_frame, text=about_text, font=("times new roman", 18), fg='black', bg='white', justify=LEFT)
        about_lbl.place(x=10, y=10)

        social_frame = Frame(main_frame, bg='white', bd=2)
        social_frame.place(x=560, y=510, width=1430, height=100)

        #Social media links
        lnk_btn=Button(social_frame,text='LinkedIn',font=('Arial',15,'bold'),bg='white',fg='royalblue',command=self.open_linkedin)
        lnk_btn.grid(row=0,column=0,padx=20,pady=20)

        github_btn = Button(social_frame, text="GitHub", font=("Arial", 14), bg='white', fg='black', command=self.open_github)
        github_btn.grid(row=0, column=1, padx=20, pady=20)

        hack_btn = Button(social_frame, text="HackerRank", font=("Arial", 14), bg='white', fg='green', command=self.open_hack)
        hack_btn.grid(row=0, column=2, padx=20, pady=20)


    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/rupali-nayak-6162a230a/")
    def open_github(self):
        webbrowser.open("https://github.com/rupalinayak56")

    def open_hack(self):
        webbrowser.open("https://www.hackerrank.com/profile/rupalinayak7789")



       



if __name__ == '__main__':
    root = Tk()
    obj = Developer_Page(root)  # Initialize the Developer_Page class
    root.mainloop()
