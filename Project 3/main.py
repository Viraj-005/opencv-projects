# Making Text Images Readable Again
import cv2 as cv

img = cv.imread('note.jpg')#import our image into script
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert to grayscale image

#thresholding method on cv
_, result = cv.threshold(img, 150, 255, cv.THRESH_BINARY) # 127 means every image that is  lighter grade in 35 is converted to the white completely,
# 255 means every image that is darker than 127 is converted to black completely
# cv.THRESH_BINARY is the most common type of thresholding, it converts all pixel values above

adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 91, 4)
# cv.ADAPTIVE_THRESH_GAUSSIAN_C is the adaptive thresholding method, it is the most common type of adaptive thresholding
# 11 is the block size, and 2 hepls to reduce or increase the noise and it is the C constant

# Resize the image and result for better display on the screen
display_img = cv.resize(img, (600, 1200))  # Adjust width and height as needed
display_result = cv.resize(result, (600, 1200))
display_adaptive = cv.resize(result, (600, 1200))

# Create resizable windows for proper display
# cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
# cv.namedWindow('Thresholded Result', cv.WINDOW_NORMAL)
# cv.namedWindow('Adaptive Result', cv.WINDOW_NORMAL)

cv.imshow('Image', display_img)

cv.imshow('Result', display_result)

cv.imshow('Adaptive Result', display_adaptive)

cv.waitKey(0)# wait here
cv.destroyAllWindows()# close all windows


