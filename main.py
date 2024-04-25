# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:11:46 2024

@author: oneph
"""

# coding:utf-8
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.button import Button
#from kivy.uix.label import Label
#from kivy.uix.togglebutton import ToggleButton
#import time

import cv2
import mediapipe as mp

#landmarks 68
landmark_points_68 = [13,151,136,365,58,288,162,234,93,149,
                      148,152,377,378,323,454,389,71,63,105,
                      66,107,336,296,334,293,301,197,45,275,
                      193,51,417,281,75,2,305,33,160,158,
                      133,153,144,362,385,387,263,373,380,61,
                      39,37,0,267,269,291,405,314,17,84,
                      181,78,82,312,308,88,80,318,310,14,
                      178,402]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

face1_array = []
face2_array = []

#camera and face dection
class KivyCamera(Image):
    
    #global start_countdown
    #start_countdown = 0
    

    
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)
  
    
    def update(self, dt):
        
        ret, image = self.capture.read()
        

        
        #cv2.rectangle(image, (100,100), (400,300), (255,255,255), 1)
        #cv2.putText(image , "0", (300,300), 0 ,10, (0,255,0))
        
        #print(dt)
        #on switch
        #if a == 1:
            #print("in")
            #cv2.rectangle(image, (100,100), (400,300), (255,255,255), 1)
###############################################################################
        #if dt == 1: 
            #global start_countdown 
            #start_countdown = 2
            
            #global start_time
            #start_time = int(time.time())

            
        ###START
       # if start_countdown == 2:
            #countdown
            #if (start_time) == int(time.time()):
                #print("3") 
            #if (start_time + 1) == int(time.time()):
                #print("2") 
            #if (start_time + 2) == int(time.time()):
                #print("1")             
            #if (start_time + 3) <= int(time.time()):
                #print("start program")
                
                
        #print(int(time.time()))
        #print("in") 
                    
        #print(start_countdown)
        
        
###############################################################################            
        
           
           
        rgb_image1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        result1 = face_mesh.process(rgb_image1)



###############################################################################
        if ret:            
            #add square to image
            #cv2.rectangle(image, (100,100), (200,200), (255,255,255), 1)
            #if face found
            if result1.multi_face_landmarks != None:

                find_landmarks(result1, image, face1_array, True, 255)
            
            
            #cv2.imshow("image", frame)
            # convert it to texture
            buf1 = cv2.flip(image, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(image.shape[1], image.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture
            
          
###############################################################################            

def find_landmarks(result, image, face_array, true_false, num):
    for facial_landmarks in result.multi_face_landmarks: 
        #for i in range(a,b):
        for i in landmark_points_68:
            pt1 = facial_landmarks.landmark[i]
            p1_x = int(pt1.x * image.shape[1])
            p1_y = int(pt1.y * image.shape[0])
            #draw circles and numbers
            cv2.circle(image, (p1_x, p1_y), 1, (0, 255, num), -1)
            #cv2.putText(image , str(i), (p1_x,p1_y), 0 ,0.4, (0,255,0))
            
            #face_array.append([p1_x,p1_y])
            
            #if true_false is True:
            #    face1_array_before.append([p1_x,p1_y])
            
        
###############################################################################
###############################################################################  
        
#main
class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)


##############################################################################
        ##WIDGETS

        #Button
        #button_obj = Button(text="Start", state='down')
        #button_obj.size_hint = (.5, .2)
        #button_obj.pos_hint = {"x":.50, "y":.25}
        #button_obj.bind(on_press=self.start_button)
        
        #btn1 = ToggleButton(text="Start")
        #btn1.bind(on_press=self.start_button)
        #print("main")
        #Label
        #greeting_obj = Label(text="0", font_size=72)
        
        
        #Layout
        layout = GridLayout(cols=1)
        layout.add_widget(self.my_camera)
        #layout.add_widget(button_obj)
        #layout.add_widget(btn1)
        #layout.add_widget(greeting_obj)
        return layout

###############################################################################
    
    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()

    def capture_image(self):
        print("take image")
        self.my_camera.export_to_png("IMG.png")
        
    def start_button(self, *args):
        print("start")
        #cv2.putText(self.capture , "3", (100,100), 0 ,0.2, (255,0,0))
        #self.my_camera.test(10)
        self.my_camera.update(1)
        #self.capture_image()
        
        
CamApp().run()