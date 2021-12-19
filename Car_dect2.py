import cv2 as cv
img=cv.imread("peak.jpg")
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
count=0
car_dect=cv.CascadeClassifier("cars.xml")
caroo=car_dect.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)
for (x,y,w,h) in caroo:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    count+=1
    cv.putText(img,f"Car{count}",(x,y),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=2)
cv.imshow("car",img)
cv.waitKey(0)