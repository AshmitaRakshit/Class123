import cv2
vid=cv2.VideoCapture(0)
#0 is for camera 1 (if there are multiple cameras)

while(True):
    #capture the video frame by frame
    ret,frame=vid.read()

    #display the resulting frame 
    cv2.imshow("colourframe",frame)

    #press q to quit
    if cv2.waitKey(1)& 0xff==ord('q'):
        break

vid.release()
#destroyallwindows
cv2.destroyAllWindows()
