import cv2
vid=cv2.VideoCapture(0)
#0 is for camera 1 (if there are multiple cameras)

while(True):
    #capture the video frame by frame
    ret,frame=vid.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display the resulting frameq
    cv2.imwrite("pic.png",gray)
    cv2.imshow("grayframe",gray)
    #press q to quit
    if cv2.waitKey(1)& 0xff==ord('q'):
        break

vid.release()
#destroyallwindows
cv2.destroyAllWindows()
