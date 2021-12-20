#pip intall opencv-contrib-python
import cv2 as cv
capture=cv.VideoCapture("FroggerHighway_1.mp4")
cars_cascade=cv.CascadeClassifier("cars.xml")
while True:
    ret,frames=capture.read()
    gray=cv.cvtColor(frames,cv.COLOR_BGR2GRAY)
    cars_detect=cars_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)
    for (x,y,w,h) in cars_detect:
        cv.rectangle(frames,(x,y),(x+w,y+h),(51,51,255),thickness=4)
        cv.putText(frames,"Cars",(x,y),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255),4)
    frames=cv.resize(frames,(400,400))
    cv.imshow("Cars",frames)
    if cv.waitKey(60)==ord("q"):
        break
cv.destroyAllWindows()