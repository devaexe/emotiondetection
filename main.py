from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QFileDialog
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import time 

import home


import MySQLdb
import numpy as np
import cv2 
import getopt

from video import create_capture
from common import clock, draw_str

from cv2 import WINDOW_NORMAL
from face_detect import find_faces
from image_commons import nparray_as_image, draw_with_alpha

import os
import random
import dircache
import subprocess



      

class home(QtGui.QMainWindow, home.Ui_Home):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.strt)
        self.pushButton_5.clicked.connect(self.ex)
        self.pushButton_6.clicked.connect(self.sng)
        self.pushButton_4.clicked.connect(self.stp)
    

    def strt(self):
        
        def _load_emoticons(emotions):
            return [nparray_as_image(cv2.imread('graphics/%s.png' % emotion, -1), mode=None) for emotion in emotions]


        def show_webcam_and_run(model, emoticons, window_size, window_name='webcam', update_time=10):
            happy=0
            sad=0
            disgust=0
            suprise=0
            neutral=0
            angry=0
            fear=0
           
            cv2.namedWindow(window_name, WINDOW_NORMAL)
            if window_size:
                width, height = window_size
                cv2.resizeWindow(window_name, width, height)

            vc = cv2.VideoCapture(0)
            if vc.isOpened():
                read_value, webcam_image = vc.read()
            else:
                print("webcam not found")
                return

            while read_value:
                for normalized_face, (x, y, w, h) in find_faces(webcam_image):
                    prediction = model.predict(normalized_face)  # do prediction
                    if cv2.__version__ != '3.1.0':
                        prediction = prediction[0]

                    image_to_draw = emotions[prediction]
                    if str(image_to_draw)=="happy":
                        happy+=1
                        #print "hcount",happy
                    if str(image_to_draw)=="neutral":
                        neutral+=1
                        #print "ncount",neutral
                    if str(image_to_draw)=="anger":
                        angry+=1
                        #print "acount",angry
                    if str(image_to_draw)=="disgust":
                        disgust+=1
                        #print "dcount",disgust
                    if str(image_to_draw)=="sadness":
                        sad+=1
                        #print "scount",sad
                    if str(image_to_draw)=="surprise":
                        suprise+=1
                        #print "supcount",suprise
                    if str(image_to_draw)=="fear":
                        fear+=1
                        #print "fcount",fear
                    if happy>=3:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/happy.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0

                    if neutral>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/neutral.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                    if angry>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/anger.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                    if disgust>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/disgust.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                    if sad>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/sadness.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                    if suprise>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/surprise.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                    if fear>=10:
                        #draw_with_alpha(webcam_image, image_to_draw, (x, y, w, h))
                        fname = "graphics/sadness.png"
                        #print fname
                        label = QLabel(self.label_5)
                        pixmap = QPixmap(fname)
                        label.setPixmap(pixmap)
                        label.resize(pixmap.width(),pixmap.height())
                        label.show()
                        self.lineEdit.setText(str(image_to_draw))
                        happy=0
                        sad=0
                        disgust=0
                        suprise=0
                        neutral=0
                        angry=0
                        fear=0
                cv2.imshow(window_name, webcam_image)
                read_value, webcam_image = vc.read()
                key = cv2.waitKey(update_time)

                if key == 27:  # exit on ESC
                    break

            cv2.destroyWindow(window_name)

        emotions = ['neutral', 'anger', 'disgust', 'happy', 'sadness', 'surprise']
        emoticons = _load_emoticons(emotions)

        # load model
        fisher_face = cv2.face.FisherFaceRecognizer_create()
        fisher_face.read('models/emotion_detection_model.xml')
         # use learnt model
        window_name = 'WEBCAM (press ESC to exit)'
        show_webcam_and_run(fisher_face, emoticons, window_size=(600, 400), window_name=window_name, update_time=8)
        
  
        
    def sng(self):
        emotion=self.lineEdit.text()
        print "emotion=",emotion
        dir = 'songs/%s/'%emotion
        filename = random.choice(dircache.listdir(dir))
        print "filename",filename
        path = os.path.join(dir, filename)
        print "path",path
        self.lineEdit_2.setText(path)
        subprocess.Popen(['mpg123', '-q', path])
           
    def ex(self):
        sys.exit()


    def stp(self):
        subprocess.call(['killall', 'mpg123'])
        
         
        
def main():
    app = QtGui.QApplication(sys.argv)  
    form = home()                 
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              
    main()                             
