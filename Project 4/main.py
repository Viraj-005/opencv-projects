# Extract Text From Images (OCR)

import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

"""
Page segmentation modes:

O Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD. ‘
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of textJ
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.
"""

"""
OCR Engine Mode

0 Legacy engine only.
1 Neural nets LSTM engine only.
2 Legacy + LSTM engines.
3 Default, based on what is available.
"""

# create a config
myconfig = r"--psm 11 --oem 3"

img = cv2.imread("test.png")
height, width, _ = img.shape

# convert above image using boxes to pytesseract
# boxes = pytesseract.image_to_boxes(img, config=myconfig)
# print(boxes) we can get the coordinates

# for box in boxes.splitlines():
#     box = box.split(" ")
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     img = cv2.rectangle(img, (x, height - y), (w, height - h), (255, 255, 0), 1)

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# print(data['text'])
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1) # rectangle = x and y coordinates, and lower right point = x +w and lower left point = y + h
        #w means width and h means height
        cv2.putText(img, data['text'][i], (x, y + h+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA) # 2 means thickness
        
display_img = cv2.resize(img, (1200, 750))
display_simg = cv2.resize(img, (1000, 750))
cv2.imshow("Output", display_simg)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# simple function for image to text
# text = pytesseract.image_to_string(PIL.Image.open("OIP.jpg"), lang="eng", config=myconfig)
# print(text)