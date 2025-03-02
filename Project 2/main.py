#Edge detection
import cv2 as cv # type: ignore
import numpy as np

camera = cv.VideoCapture(0)#use my laptop camera

while True:
    _, frame = camera.read()
    
    cv.imshow("Camera", frame)
    
    #laplacian filter
    laplacian = cv.Laplacian(frame, cv.CV_64F)# 64F means 64 bit and float datatype
    laplacian = np.uint8(laplacian)# convert the above output into uint8 (0-255) datatype
    cv.imshow("Laplacian", laplacian) # Visualize laplacian filter
    
    #canny filter
    edges = cv.Canny(frame, 30, 50) # 100, 200 =two threshholds
    cv.imshow("Canny", edges) # Visualize canny filter
    
    if cv.waitKey(5) == ord('X'):
        break
    
camera.release()
cv.destroyAllWindows()