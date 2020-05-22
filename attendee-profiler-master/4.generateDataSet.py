import cv2 
import numpy as np
import urllib
from tkinter import messagebox
import tkinter as tk

url='http://192.168.201.2:8080/shot.jpg'

def generate(screen=None):
    Id=0
    screen=tk.Tk()
    eye_cascade=cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_eye.xml')
    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')    
    messagebox.showinfo("Generate DataSet","Starting Creating Face Recognition dataset" )
    while(True):
        imgResponse = urllib.request.urlopen(url)
 
        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
 
        # Decode the array to OpenCV usable format
        img = cv2.imdecode(imgNp,-1)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            f=cv2.resize(gray[y:y+h,x:x+w],(200,200))
            Id=Id+1
            cv2.imwrite('C:\\Users\\Abhishek\\Local data\\'+str(Id)+'.jpg',f)
            
            roi_gray=gray[y:y+h,x:x+w]
            
            eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
            
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(img[y:y+h,x:x+w],(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow("Generate Data Set",img)
        if cv2.waitKey(int(1000/12)) & 0xff==ord("q"):
            break
        
    cv2.destroyAllWindows()
    messagebox.showinfo("Generate DataSet","Dataset is created successfully and saved at C:\\Users\\Abhishek\\local data")
    screen.destroy()
    
if __name__=="__main__":
    generate()