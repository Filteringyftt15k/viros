# azrael
import cv2
import winsound 
import random 

while 1:
     img = cv2.imshow("virus.jpg", 1)

     cv2.waitKey(200) 
     f = random.randint(800,20000)
     g = random.randint(1000,3000)

     winsound.Beep(f, g)
