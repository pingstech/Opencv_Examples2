import cv2
import numpy as np

def value(temp):
    None

cv2.namedWindow("Original Image")
cv2.createTrackbar("Gradient value","Original Image",10,255,value)
cv2.createTrackbar("Threshold Value","Original Image",10,255,value)
cv2.createTrackbar("Min radius","Original Image",0,50,value)
cv2.createTrackbar("Max radius","Original Image",50,150,value)
cv2.createTrackbar("Min distance","Original Image",2,128,value)


img=cv2.imread("coins.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.medianBlur(imgGray,5)


while True:

    minRad=cv2.getTrackbarPos("Min radius","Original Image")
    maxRad=cv2.getTrackbarPos("Max radius","Original Image")
    minDist=cv2.getTrackbarPos("Min distance","Original Image")
    gradVal=cv2.getTrackbarPos("Gradient value","Original Image")
    thrVal=cv2.getTrackbarPos("Threshold Value","Original Image")

    circles=cv2.HoughCircles(imgBlur,cv2.HOUGH_GRADIENT,1,img.shape[0]/minDist,param1=gradVal,param2=thrVal,minRadius=minRad,maxRadius=maxRad)    
    if circles is not None:
        circles=np.uint16(np.around(circles))        # "circles"ın içine gelen değerleri "np.around" ile yuvarladık ve işlenebilsin diye uint16 formuna getirdik

        for circle in circles[0,:]:                 # yani "circles" değerinin sıfırıncı indisinden son indisine kadar giden değerlerire "circle" a atadık burada sıfırıncı ve birinci indeks çemberin merkezi, ikinci indeks ise yarı çapı
            cv2.circle(img,(circle[0],circle[1]), circle[2],(0,0,255),2)
        
    cv2.imshow("Original Image",img)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()