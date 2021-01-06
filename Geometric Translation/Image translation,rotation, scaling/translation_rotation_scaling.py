# import Opencv and numpy
import cv2 as cv
import numpy as np

# create instance of the image
img = cv.imread('../../images/glass-ball.jpg')
# check The image size 
print(img.shape[:2])
#######################################################################
#Image Resize

# Image size is very large so lets scale it down to (640, 480) 
img_scale = cv.resize(img, (640,480), interpolation=cv.INTER_AREA)
#take values for rows, cols
num_rows, num_cols = img_scale.shape[:2]


########################################################################
#Image Translation

# build a matrix for shift images
translation_mat = np.float32([[1,0,50], [0,1,50]])
# lets shift the image bottum-right direction
img_translation = cv.warpAffine(img_scale, translation_mat, (num_cols,num_rows))

# Warpaffne function shifts the image in any direction but frame size does't change automatically,
#We can increase the frame size
translation_matrix = np.float32([[1,0, 0], [0, 1, 0]])
scaled_frame_img = cv.warpAffine(img_translation, translation_matrix, (num_cols + 70, num_rows + 70))

##########################################################################
#Image Rotation

# Create matrix translation_mat for rotation
translation_mat = np.float32([[1,0, int(0.5*num_cols -100)], [0,1,int(0.5*num_rows-185)]])
#Create rotation matrix for give angle and points 
rotation_mat = cv.getRotationMatrix2D((num_cols, num_rows), 30, 1) 
img_trans = cv.warpAffine(img_scale, translation_mat,(2*num_cols,2*num_rows))
# lets make frame bigger
img_rotation = cv.warpAffine(img_trans, rotation_mat, (2*num_cols-426,2*num_rows-226))


# show Scaled image 
cv.imshow('Scaled Image',img_scale)
# show Translate image
cv.imshow('Translation',img_translation)
# show translate image with bigger in frame bigger frame
cv.imshow('Translation_image',scaled_frame_img)
# show rotated image 
cv.imshow('Rotation',img_rotation)
# Wait until any keyboard argument not pass
cv.waitKey(0)
