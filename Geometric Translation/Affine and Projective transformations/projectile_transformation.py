# Import packages
import cv2 as cv
import numpy as np

# Read image in opencv format
img = cv.imread("../../images/tesla.jpg")

# Scale down the image
scaled_img = cv.resize(img,None, fx=0.3, fy=0.3, interpolation=cv.INTER_AREA)
# assign rows and columns
rows , cols = scaled_img.shape[:2]

##########     Projective Transformation     ############################################
# original points of the image
org_points = np.float32([[0,0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
# destinating points for image
trans_points = np.float32([[int(0.2*(cols-1)),0], [int(0.8*(cols-1)), 0], [int(0.2*(cols-1)), rows-1], [int(0.8*(cols-1)),rows-1]])
# initialize projective matrix
projective_matrix = cv.getPerspectiveTransform(org_points, trans_points)
projective_image = cv.warpPerspective(scaled_img, projective_matrix, (cols,rows))



# show  Projective transformation
cv.imshow("Porjective Transformation", projective_image)

cv.waitKey(0)

cv.destroyAllWindows()