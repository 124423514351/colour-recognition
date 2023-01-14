import cv2 as cv
import numpy as np
import imutils
import keyboard

cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

pressed = 0
while True:
        
        if keyboard.is_pressed('g'):
            pressed = 'g'
        elif keyboard.is_pressed('y'):
            pressed = 'y'
        elif keyboard.is_pressed('o'):
            pressed = 'o'
        elif keyboard.is_pressed('b'):
            pressed = 'b'
        elif keyboard.is_pressed('q'):
            pressed = 'q'
        elif keyboard.is_pressed('r'):
            pressed = 'r'  

        _, frame = cap.read()
        frame = cv.resize(frame,(800,600))
        blur = cv.GaussianBlur(frame,(15,15),0)
        hsv=cv.cvtColor(blur,cv.COLOR_BGR2HSV)

        lower_gray=np.array([0, 0, 40])
        upper_gray=np.array([180, 18, 230])
    
        lower_yellow=np.array([25, 50, 70])
        upper_yellow=np.array([35, 255, 255])
    
        lower_orange=np.array([10, 50, 70])
        upper_orange=np.array([24, 255, 255])
    
        lower_blue=np.array([90, 50, 70])
        upper_blue=np.array([128, 255, 255])
    
        lower_green=np.array([36, 50, 70])
        upper_green=np.array([89, 255, 255])

        lower_red=np.array([159, 50, 70])
        upper_red=np.array([180, 255, 255])
        lower_red2=np.array([0, 50, 70])
        upper_red2=np.array([9, 255, 255])
#---------------------------------------------------------------
        mask_green=cv.inRange(hsv,lower_green,upper_green)
        mask_red=cv.inRange(hsv,lower_red,upper_red)
        mask_orange=cv.inRange(hsv,lower_orange,upper_orange)
        mask_blue=cv.inRange(hsv,lower_blue,upper_blue)
        mask_yellow=cv.inRange(hsv,lower_yellow,upper_yellow)
        mask_gray=cv.inRange(hsv,lower_gray,upper_gray)
        mask_red2=cv.inRange(hsv,lower_red2,upper_red2)
#---------------------------------------------------------------
        cnts_green=cv.findContours(mask_green,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_green=imutils.grab_contours(cnts_green)

        cnts_red=cv.findContours(mask_red,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_red=imutils.grab_contours(cnts_red)
    
        cnts_orange=cv.findContours(mask_orange,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_orange=imutils.grab_contours(cnts_orange)

        cnts_blue=cv.findContours(mask_blue,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_blue=imutils.grab_contours(cnts_blue)
    
        cnts_yellow=cv.findContours(mask_yellow,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_yellow=imutils.grab_contours(cnts_yellow)
    
        cnts_gray=cv.findContours(mask_gray,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_gray=imutils.grab_contours(cnts_gray)
    
        cnts_red2=cv.findContours(mask_red2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        cnts_red2=imutils.grab_contours(cnts_red2)
    
#------------------------------------------------------------

        if pressed == 'g':
            for c in cnts_green:
                
                area_green=cv.contourArea(c)
            
                if area_green>5000:
                    cv.drawContours(frame,[c],-1,(0,255,0),2)
                    M=cv.moments(c)
                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"green",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                
        elif pressed == 'r':
            for c in cnts_red:
                
                area_red=cv.contourArea(c)
                if area_red>5000:

                    cv.drawContours(frame,[c],-1,(0,0,255),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"red",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
        elif pressed == 'r':
            for c in cnts_red2:
                
                area_red2=cv.contourArea(c)

                if area_red2>5000:

                    cv.drawContours(frame,[c],-1,(0,0,255),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"red",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
          
        elif pressed == 'o':
            for c in cnts_orange:
                
                area_orange=cv.contourArea(c)

                if area_orange>5000:

                    cv.drawContours(frame,[c],-1,(0,165,255),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"orange",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
   
        elif pressed == 'b':
            for c in cnts_blue:
                
                area_blue=cv.contourArea(c)

                if area_blue>5000:

                    cv.drawContours(frame,[c],-1,(255,0,0),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"blue",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            
        elif pressed == 'y':
            for c in cnts_yellow:
                
                area_yellow=cv.contourArea(c)

                if area_yellow>5000:

                    cv.drawContours(frame,[c],-1,(0,255,255),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"yellow",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                
        elif pressed == 'q':
            for c in cnts_gray:
                
                area_gray=cv.contourArea(c)

                if area_gray>5000:

                    cv.drawContours(frame,[c],-1,(192,192,192),2)
                    M=cv.moments(c)

                    cx=int(M["m10"]/M["m00"])
                    cy=int(M["m01"]/M["m00"])

                    cv.circle(frame,(cx,cy),7,(255,255,255),-1)
                    cv.putText(frame,"gray",(cx-20,cy-20),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
      
        cv.imshow("result",frame)
        k=cv.waitKey(5)
        if k==27:
            break
cap.release()
cv.destroyAllWindows()
