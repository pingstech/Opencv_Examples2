import cv2
import numpy as np
import utlis

webcam=False                # Kamerayı başta kullanmayacağımız için kamerayı false yaparak kameranın çalışmasını engelledik
path="measurement2.jpg"
cap=cv2.VideoCapture(0)
cap.set(10,160)             # Parlaklık için
cap.set(3,1920)             # Genişlik için
cap.set(4,1080)              # Yükseklik için
scale=3
widthPaper=230*scale
heightPaper=320*scale

while True:
    if webcam:
        success,img=cap.read()
    else:
        img=cv2.imread(path)
    
    img=cv2.resize(img,(0,0),None,0.5,0.5)      # Resim ekrana sığmadığından resmi yeniden boyutlandırdık
    imgContours,conts=utlis.getContours(img,minArea=3000,filter=4)
    
    if len(conts)!=0:
        biggest=conts[0][2]
        #print(biggest)
        imgWarp=utlis.warpImg(img,biggest,widthPaper,heightPaper)
        imgContours2,conts2=utlis.getContours(imgWarp,minArea=30000,filter=4,CanThresh=[50,50],draw=False)
        
        
        if len(conts)!=0:
            for obj in conts2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,0,255),2) 
                nPoints=utlis.reorder(obj[2]) 
                nWei=round((utlis.findDist(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nHei=round((utlis.findDist(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv2.arrowedLine(imgContours2,(nPoints[0][0][0],nPoints[0][0][1]),(nPoints[1][0][0],nPoints[1][0][1]),(255,0,255),3,8,0,0.05)
                cv2.arrowedLine(imgContours2,(nPoints[0][0][0],nPoints[0][0][1]),(nPoints[2][0][0],nPoints[2][0][1]),(255,0,255),3,8,0,0.05)
                x,y,w,h=obj[3]
                cv2.putText(imgContours2,"{}cm".format(nWei),(x+30,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(0,255,0),2)
                cv2.putText(imgContours2,"{}cm".format(nHei),(x-80,h//2),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(0,255,0),2)

        cv2.imshow("Warped Image",imgContours2)

    cv2.imshow("Original",img)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()