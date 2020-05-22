from tkinter import Image

from modelArch import DenseArchs
import cv2
import numpy as np
import os
from embedding import emb
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

from faceRec import assurePath

n_classes=5

e=emb()
arc=DenseArchs(n_classes)
face_model=arc.arch()

x_data=[]
y_data=[]

learning_rate=0.01
epochs=27
batch_size=32

people=os.listdir('people')

for x in people:
    for i in os.listdir('people/'+x):
        img=cv2.imread('people'+'/'+x+'/'+i,1)
        img=cv2.resize(img,(160,160))
        img=img.astype('float')/255.0
        img=np.expand_dims(img,axis=0)
        embs=e.calculate(img)
        x_data.append(embs)
        y_data.append(int(x[-1]))


x_data=np.array(x_data,dtype='float')
y_data=np.array(y_data)
y_data=y_data.reshape(len(y_data),1)
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.1,random_state=77)
y_train=to_categorical(y_train,num_classes=n_classes)
y_test=to_categorical(y_test,num_classes=n_classes)

o=Adam(lr=learning_rate,decay=learning_rate/epochs)
face_model.compile(optimizer=o,loss='categorical_crossentropy')
face_model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,shuffle='true',validation_data=(x_test,y_test))
face_model.save('face_reco2.MODEL')
print(x_data.shape,y_data.shape)


def tag_image(loc):
    face_cascade = cv2.CascadeClassifier(
        'C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(
        'C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

    assurePath(loc)

    imagePaths = [os.path.join(loc, f) for f in os.listdir(loc)]
    rawimg = []
    tag_value = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img = np.array(PIL_img, "uint8")
        id = int(os.path.split(imagePath)[-1].split(".")[0])

        faces = face_cascade.detectMultiScale(img)

        for (x, y, w, h) in faces:
            rawimg.append(cv2.resize(img[y:y + h, x:x + w], (200, 200)))
            tag_value.append(id)
    return rawimg, tag_value
