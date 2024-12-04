from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from cv2.face import LBPHFaceRecognizer_create
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1580x830+0+0')
        self.root.title('Face Recognition')

        # Title
        ttl_lbl = Label(self.root, text='Face Recognition', font=('times new roman', 30, 'bold'), bg='blue', fg='gold')
        ttl_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open('./Images/f2.webp')
        img_top = img_top.resize((1530, 800), Image.LANCZOS)
        self.photoimgt = ImageTk.PhotoImage(img_top)

        fst_lbl = Label(self.root, image=self.photoimgt)
        fst_lbl.place(x=0, y=45, width=1530, height=800)

        # Button
        btn = Button(fst_lbl, text='FACE DETECTOR', command=self.face_recog, font=('Arial', 12, 'bold'), bg='gold', fg='blue', cursor='hand2')
        btn.place(x=600, y=700, width=200, height=40)
    
    #ATTENDANCE
    def mark_attendance(self,n,i,r,d):
        with open('./attendance.csv','r+',newline='\n') as f:
            myDatlist=f.readlines()
            name_list=[]
            for line in myDatlist:
                entry=line.split(',') #rupali,id,roll
                name_list.append(entry[0])
                #for not repeating the attendance whenever i come for face recognition
            if((n not in name_list) and (i not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime('%d/%m/%y')
                timeString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{n},{i},{r},{d},{timeString},{d1},Preset')













    #FACE RECOGNITION FUNCTION

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                idss, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection and query
                try:
                    conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognition')
                    my_cursor = conn.cursor()

                    my_cursor.execute('SELECT NAME FROM student WHERE ID=' + str(idss))
                    n = my_cursor.fetchone()
                    n = '+'.join(n) if n else 'Unknown'

                    my_cursor.execute('SELECT DEPT FROM student WHERE ID=' + str(idss))
                    d = my_cursor.fetchone()
                    d = '+'.join(d) if d else 'Unknown'

                    my_cursor.execute('SELECT `ROLL NO` FROM student WHERE ID=' + str(idss))
                    r = my_cursor.fetchone()
                    r = '+'.join(r) if r else 'Unknown'

                    my_cursor.execute('SELECT ID FROM student WHERE ID=' + str(idss))
                    i = my_cursor.fetchone()
                    i = '+'.join(i) if d else 'Unknown'

                    # Check confidence and display details
                    if confidence > 77:
                        cv2.putText(img, f'Name: {n}', (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3,)
                        cv2.putText(img, f'Id: {i}', (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                        cv2.putText(img, f'Roll NO: {r}', (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                        cv2.putText(img, f'Department: {d}', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                        self.mark_attendance(n,i,r,d)

                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, 'Unknown Face', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    cv2.putText(img, "DB Error", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), 'Face', clf)
            return img

        # Load face cascade and trained classifier
        faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  # Ensure the path is correct
        clf = LBPHFaceRecognizer_create()
        clf.read('./classifier.xml')

        # Open webcam
        videocap = cv2.VideoCapture(0)

        while True:
            ret, img = videocap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow('Welcome To Face Recognition', img)

            # Press Enter to close the webcam window
            if cv2.waitKey(1) == 13:
                break

        videocap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
