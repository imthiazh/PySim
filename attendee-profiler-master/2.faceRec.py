# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:49:13 2018

@author: Abhishek
"""
import os
import cv2
import urllib
import tkinter as tk
from tkinter import messagebox
import numpy as np
import mysql.connector
import datetime
import log2

url='http://192.168.201.2:8080/shot.jpg'

#start
def FindFace(self, img):
    cropped = None
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = self.cascade.detectMultiScale(grey, 1.3, 5)
    cropped = []
    coor = []
    for (self.x, self.y, self.w, self.h) in faces:
        cropped.append(img[self.y:self.y + self.h, self.x:self.x + self.w])
        coor.append([self.x, self.y, self.w, self.h])
    return cropped, coor
#end

def save(newvar,screen=None):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
    mycursor= mydb.cursor()
    
    tod=datetime.date.today()
    query= "insert into attendance (date) values('"+str(tod)+"');"
    mycursor.execute(query)
    mydb.commit()
    
    for x,y in newvar.items():
        if str(y.get())=='1':
            query="update attendance set _"+str(x)+" ='P' where date like '"+str(tod)+"';"
        else:
            query="update attendance set _"+str(x)+" ='A' where date like '"+str(tod)+"';"
        mycursor.execute(query)
        mydb.commit()
    mycursor.close()
    messagebox.showinfo("FRAS Attendace","Attendance is uploaded successfully")
    log2.mainScreen(screen.destroy())
    
def assurePath(path):
    dir=os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(dir)

def attendanceSheet(present,details):
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
    mycursor= mydb.cursor()
    
    
    global screen
    screen = tk.Tk()
    
    screen.configure(background = 'floral white')
    screen.geometry("680x600")
    scroll=tk.Scrollbar(screen)
    scroll.pack(side=tk.RIGHT,fill=tk.Y)
    screen.title("Attendance Uploader")
    tk.Label(text = "FRAS Attendance Sheet", bg = "azure", width = "100", height = "2", font = ("Times", 14), fg = "maroon1").pack()
    tk.Label(text=details,bg='floral white',height="2",font=("Times",12,"bold")).pack()
    tk.Button(screen, text = "Save Attendance",fg = "dark violet", bg = "SeaGreen1", borderwidth=2, height = "2", width = "20", command = lambda: save({**var, **var2} ,screen)).pack()

    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "List Of Students", bg = "floral white", font = ("Times", 14), fg = "maroon1").pack()
    tk.Label(screen, text = "Present Students", fg = 'blue', bg = 'floral white', font = ('Times',11)).place(x = 60, y = 180)
    tk.Label(screen, text = "%", fg = 'blue', bg = 'floral white', font = ('Times',14)).place(x = 230, y = 180)
    tk.Label(screen, text = "Absent Students", fg = 'blue', bg = 'floral white', font = ('Times',12)).place(x = 380, y = 180)
    tk.Label(screen, text = "%", fg = 'blue', bg = 'floral white', font = ('Times',14)).place(x = 550, y = 180)

    var=dict()
    name=dict()
    for x in present:
        var[x]=tk.IntVar(value=1)
        query="select name from student where sid like '"+str(x)+"';"
        mycursor.execute(query)
        result=mycursor.fetchone()
        
        for n in result:
            name[x]=n
            
    inc=30
    
    for x in present:
        query="select count(*) from attendance;"
        query2= "select count(*) from attendance where _"+str(x)+" like 'P';"
        mycursor.execute(query)
        result1=mycursor.fetchone()
        mycursor.execute(query2)
        result2=mycursor.fetchone()
        
        tk.Checkbutton(screen, text=str(x)+"  "+str(name[x]), variable=var[x], bg = 'floral white').place(x = 60, y = 180+inc)
        tk.Label(screen, text = str(round((result2[0]/result1[0])*100,2)), bg = 'floral white', font = ('Times',12)).place(x = 230, y = 180+inc)
        inc+=25
    
    absent=set()
    name=dict()
    var2 = dict()
    query="select name , sid from student;"
    mycursor.execute(query)
    if (mycursor.rowcount==1):
        result=mycursor.fetchone()
    else:
        result=mycursor.fetchall()
    
    for x,y in result:
        if int(y) not in present:
            var2[y]=tk.IntVar(value=0)
            absent.add(y)
            name[y]=x
    
    inc =30
    for x in absent:
        query="select count(*) from attendance;"
        query2= "select count(*) from attendance where _"+str(x)+" like 'P';"
        mycursor.execute(query)
        result1=mycursor.fetchone()
        mycursor.execute(query2)
        result2=mycursor.fetchone()        
        tk.Checkbutton(screen, text=str(x) + "  "+str(name[x]), variable=var2[x], bg = 'floral white').place(x = 380, y = 180+inc)
        tk.Label(screen, text = str(round((result2[0]/result1[0])*100,2)), bg = 'floral white', font = ('Times',12)).place(x = 550, y = 180+inc)
        inc+=25
    
    screen.mainloop()


def face_rec(year,course,branch,section,screen):
    present=set()
    model=cv2.face.LBPHFaceRecognizer_create()
    details="Year : "+year+"    "+"  Course : "+course+"    "+"  Branch : "+branch+"    "+"  Seciton:"+section+"  "
    path="C:\\Users\\Abhishek\\trainer\\"+course+"\\"+branch+"\\"+year+"\\"+section+"\\"
    assurePath(path)
    try:
        model.read(path+"trainer.yml")
    except Exception as e:
        messagebox.showerror("FRAS Error",e)
    font =cv2.FONT_HERSHEY_SIMPLEX
    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    try:
        while(True):
            imgResponse = urllib.request.urlopen(url)
 
        # Numpy to convert into a array
            imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
 
        # Decode the array to OpenCV usable format
            img = cv2.imdecode(imgNp,-1)
        
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray,1.3,5)
        
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x-20,y-20),(x+w+20,y+w+20),(0,255,0),2)
                roi=cv2.resize(gray[y:y+h,x:x+w],(200,200),interpolation=cv2.INTER_LINEAR)
                id,confidence = model.predict(roi)
                present.add(id)
                cv2.rectangle(img,(x-22,y-90),(x+w+22,y-22),(0,255,0),-1)
                cv2.putText(img,str(id)+" : "+str(round(confidence,2)),(x,y-40),font,1,(255,255,255),3)
            cv2.imshow("camera",img)
            if cv2.waitKey(10)& 0xff ==ord("q"):
                break
        cv2.destroyAllWindows()
        attendanceSheet(present,details)
        
    except Exception as e:
        messagebox.showerror("FRAS Error",e)
