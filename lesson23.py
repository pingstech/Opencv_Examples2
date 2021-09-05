import cv2
import numpy as np

img1=cv2.imread("balls.jpg")
img2=cv2.imread("coins.jpg")
print(img2.shape[0])
imgGray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
imgGray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
imgBlur1=cv2.medianBlur(imgGray1,5)
imgBlur2=cv2.medianBlur(imgGray2,5)

circles=cv2.HoughCircles(imgBlur2,cv2.HOUGH_GRADIENT,1,img2.shape[0]/4,param1=200,param2=10,minRadius=30,maxRadius=70)    # Bunun dışında girecek bir değer yok o yüzden "cv2.HOUGH_GRADIENT" yazacağız

#----------------------------------------------------------FONKSİYON KULLANIMI---------------------------------------------------------------
# cv2.HoughCircles (image, method, dp, minDist, circles=..., param1=..., param2=..., minRadius=..., maxRadius=...)
# image=resim kaynağı, method=cv2.HOUGH_GRADIENT, dp=1, minDist=Çemberler arası minimum mesafe(burası için genelde img.shape[0]/x yapılır, hata oranına göre "x" değeri arttırılıp azaltılır)
# param1=gradient değer, param2=threshold değer, minRadius=tahmini en az yarıçap değeri, maxRadius=tahmini en fazla yarıçap değeri   [ minDist,param1,param2 bizim için önemli değerler]
#--------------------------------------------------------------------------------------------------------------------------------------------

if circles is not None:
    circles=np.uint16(np.around(circles))        # "circles"ın içine gelen değerleri "np.around" ile yuvarladık ve işlenebilsin diye uint16 formuna getirdik

    for circle in circles[0,:]:                 # yani "circles" değerinin sıfırıncı indisinden son indisine kadar giden değerlerire "circle" a atadık burada sıfırıncı ve birinci indeks çemberin merkezi, ikinci indeks ise yarı çapı
        cv2.circle(img2,(circle[0],circle[1]), circle[2],(0,0,255),2)

#cv2.imshow("First Image",img1)
cv2.imshow("Second Image",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()