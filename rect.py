import numpy as np
import cv2 

rect=np.ones((600,800,3),dtype=np.uint8)*255
#np.ones reshapes the array-----width:600, height:800

cv2.rectangle(rect,(0,300),(400,599),(0,0,255),10)
#10 is the thickness 
#bgr 0,0,255 is for red colour
#0,300 is the (x,y) of left top corner of the rectangle
#400,599 is the x,y of right bottom corner of the rectangle
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.rectangle(rect,(400,0),(800,300),(0,255,0),4)
#10 is the thickness 
#bgr 0,0,255 is for red colour
#400,0 is the (x,y) of left top corner of the rectangle
#800,300 is the x,y of right bottom corner of the rectangle
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()