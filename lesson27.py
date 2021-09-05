import cv2
import numpy as np

def doContour(frame,orgFrame):
    contours,_=cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    font=cv2.FONT_HERSHEY_SIMPLEX
    for contour in contours:
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        cv2.drawContours(frame,[approx],-1,(0,0,255),3)
        x=approx.ravel()[0]
        y=approx.ravel()[1]

        if len(approx)==1:
            pass

        else:
            cv2.putText(orgFrame,"Target",(x,y),font,1,(255,255,255),2)

    return frame

def trackbarVal():
    None

capCam=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow("Trackbar Window")
cv2.createTrackbar("Low HUE ","Trackbar Window",0,255,trackbarVal)
cv2.createTrackbar("High HUE ","Trackbar Window",255,255,trackbarVal)
cv2.createTrackbar("Low Saturation","Trackbar Window",0,255,trackbarVal)
cv2.createTrackbar("High Saturation","Trackbar Window",255,255,trackbarVal)
cv2.createTrackbar("Low Value","Trackbar Window",0,255,trackbarVal)
cv2.createTrackbar("High Value","Trackbar Window",255,255,trackbarVal)

while True:
    _,frame=capCam.read()
    #frame=cv2.imread("hedef.png")
    hsvFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_Hue=cv2.getTrackbarPos("Low HUE ","Trackbar Window")
    h_Hue=cv2.getTrackbarPos("High HUE ","Trackbar Window")
    l_Sat=cv2.getTrackbarPos("Low Saturation","Trackbar Window")
    h_Sat=cv2.getTrackbarPos("High Saturation","Trackbar Window")
    l_Val=cv2.getTrackbarPos("Low Value","Trackbar Window")
    h_Val=cv2.getTrackbarPos("Low Value","Trackbar Window")
    lowLimit=np.array([l_Hue,l_Sat,l_Val])
    uppLimit=np.array([h_Hue,h_Sat,h_Val])
    maskFrame=cv2.inRange(hsvFrame,lowLimit,uppLimit)
    resFrame=cv2.bitwise_and(frame,frame,mask=maskFrame)
    cv2.imshow("Orginal Image",frame)
    cv2.imshow("Mask Image",maskFrame)
    doContour(maskFrame,resFrame)
    cv2.imshow("Final Image",resFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capCam.release()
cv2.destroyAllWindows()