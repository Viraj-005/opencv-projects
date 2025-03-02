#Motion filtering on a video
import cv2 as cv # type: ignore

#video = cv.videoCapture(0) if you use your own camera (if one camera = 0, two is = 1, three is = 2 etc)
video = cv.VideoCapture('people.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(300, 200) # (20)how long back and how far back should i look, (50) = threshold

#visualize data frame by frame
while True:
    ret, frame = video.read() #ret=return value, frame=current frame
    if ret:
        mask = subtractor.apply(frame) #apply subtractor to current frame
        cv.imshow('Mask', mask) #show mask
        
        if cv.waitKey(5) == ord('X'): #if X is pressed break(terminate)
            break
        
    else:
        #if we don't have a return value, reset the video
        video = cv.VideoCapture('people.mp4')
        
cv.destroyAllWindows()
video.release()