# Import packages
import cv2 as cv
import numpy as np
from projectile_transformation import projective_image

# Read image in opencv format
img = cv.imread("../../images/tesla.jpg")

# Scale down the image
scaled_img = cv.resize(img,None, fx=0.3, fy=0.3, interpolation=cv.INTER_AREA)
# assign rows and columns
rows , cols = scaled_img.shape[:2]

##########     Parallelogram      ############################################
# original points of the image
org_points = np.float32([[0,0], [cols-1, 0], [0, rows-1]])
# destinating points for image
trans_points = np.float32([[0,0], [int(0.6*(cols-1)), 0], [int(0.4*(cols-1)), rows-1]])
# initialize affine matrix(for affine transformations)
affine_matrix = cv.getAffineTransform(org_points, trans_points)
parallelogram_image = cv.warpAffine(scaled_img, affine_matrix, (cols,rows))


##########      Mirror Image      #############################################
# original points will be same
# change the transfomation points(destinatioin points) 
trans_points = np.float32([[cols-1,0], [0,0], [cols-1, rows-1]])
affine_matrix = cv.getAffineTransform(org_points, trans_points)
mirror_image = cv.warpAffine(scaled_img, affine_matrix, (cols, rows))





# show  parallelogram image
cv.imshow("Affine Transformation", parallelogram_image)

# show mirror image
cv.imshow("Mirror Image", mirror_image)
cv.imshow("Normal image With Affine and Projective transformation", horizontal_1)
cv.waitKey(0)

cv.destroyAllWindows()