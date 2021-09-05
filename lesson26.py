import cv2

def setFrame(frame):
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurFrame=cv2.GaussianBlur(grayFrame,(5,5),0)
    _,threshFrame=cv2.threshold(blurFrame,20,255,cv2.THRESH_BINARY)
    dilatedFrame=cv2.dilate(threshFrame,None,iterations=3)
    return dilatedFrame

def doContour(frame,orgFrame,areaSize=1500):
    contours,_=cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    font=cv2.FONT_HERSHEY_SIMPLEX
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        
        if cv2.contourArea(contour)<areaSize:
            continue
        
        cv2.rectangle(orgFrame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(orgFrame,"x value :{}".format(x),(20,50),font,1,(0,255,0),1)
        cv2.putText(orgFrame,"y value :{}".format(y),(20,75),font,1,(0,255,0),1)

    return frame

cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    diff=cv2.absdiff(frame1,frame2)
    diff=doContour(setFrame(diff),frame1)
    cv2.imshow('Detection',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()