import cv2
import numpy
from modelArch import DenseArchs
from embedding import emb
class face:
    def __init__(self):
        self.cascade=cv2.CascadeClassifier('faces.xml')
        self.x=None
        self.y=None
        self.w=None
        self.h=None
        #initializes the coordinates required

    def detectFace(self,img):
        cropped=None
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.cascade.detectMultiScale(grey,1.3,5)
        cropped=[]
        coor=[]
        for (self.x,self.y,self.w,self.h) in faces:
            cropped.append(img[self.y:self.y+self.h,self.x:self.x+self.w])
            coor.append([self.x,self.y,self.w,self.h])
            #generates coordinated img values
        return cropped,coor
