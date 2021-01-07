# Import opencv and numpy packages
import cv2 as cv
import numpy as np

#make image instance
img = cv.imread('../../images/flowers.jpg')

# first shrink down the image size
img = cv.resize(img,(480,320),interpolation=cv.INTER_AREA)
# convert it to gray 
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# convert it to YUV color format
img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
# convert it to HSV color format
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

##################################################################
#display images in seperate frames

# display default colored image
cv.imshow("Default Image",img)
# display all of the color formats
cv.imshow('Gray Image', img_gray)
cv.imshow('YUV image', img_yuv)
cv.imshow('HSV image', img_hsv)

##################################################################

# display all the color chennels of YUV and HSV color spaces separatelly 

#first lets stack the images horizontally by numpy hstack()
horizontal_1 = np.hstack([img_yuv[:,:,0],img_yuv[:,:,1],img_yuv[:,:,2]])
horizontal_2 = np.hstack([img_hsv[:,:,0],img_hsv[:,:,1],img_hsv[:,:,2]])

vertical = np.vstack([horizontal_1,horizontal_2])
# Show the final image collage
# cv.imshow("Y,U and V chennels", horizontal_1)
# cv.imshow("H,S and V chennels", horizontal_2)
cv.imshow('YUV and HSV mix collage',vertical)
# set wait key to all
cv.waitKey(0)
#destroy all the windows
cv.destroyAllWindows()
