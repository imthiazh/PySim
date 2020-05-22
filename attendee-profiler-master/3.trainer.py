# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:21:45 2018

@author: Abhishek
"""

import cv2
import os
from tkinter import messagebox
from PIL import Image
import numpy as np

def assurePath(path):
    dir=os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def getImageAndLabel(path):

    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    eye_cascade=cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

    assurePath(path)
    
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids=[]
    
    for imagePath in imagePaths:
        PIL_img=Image.open(imagePath).convert('L')
        img=np.array(PIL_img,"uint8")
        id=int(os.path.split(imagePath)[-1].split(".")[0])
        
        faces=face_cascade.detectMultiScale(img)
        
        for (x,y,w,h) in faces:
            faceSamples.append(cv2.resize(img[y:y+h,x:x+w],(200,200)))
            ids.append(id)
    return faceSamples, ids

def train(year,course,branch,section):
    try:
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        path="C:\\Users\\Abhishek\\faceDataSet\\"+course+"\\"+branch+"\\"+year+"\\"+section+"\\"
        faces,ids=getImageAndLabel(path)
        recognizer.train(faces,np.array(ids))
        assurePath("C:\\Users\\Abhishek\\trainer\\"+course+"\\"+branch+"\\"+year+"\\"+section+"\\")
        recognizer.save("C:\\Users\\Abhishek\\trainer\\"+course+"\\"+branch+"\\"+year+"\\"+section+"\\trainer.yml")
        messagebox.showinfo("Training model","Training model created Successfully")
        
    except Exception as e:
        messagebox.showerror("Training model",e)
    