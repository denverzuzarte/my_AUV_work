import cv2 as cv
import numpy as np;
img = cv.imread('python/PythonOOPS/images/img.jpg',cv.IMREAD_COLOR);
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
gray_blurred = cv.blur(gray, (3, 3));
resize = cv.resize(gray_blurred, (500, 500))
cv.imshow('hell',resize);
cv.waitKey(0);

gay_var,threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, gay_var2 = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
i = 0

# list for storing names of shapes 
for contour in contours: 
  
    # here we are ignoring first counter because  
    # findcontour function detects whole image as shape 
    if i == 0: 
        i = 1
        continue
  
    # cv.approxPloyDP() function to approximate the shape 
    approx = cv.approxPolyDP( 
        contour, 0.0001 * cv.arcLength(contour, True), True) 
      
    # using drawContours() function 
    cv.drawContours(img, [contour], 0, (0, 0, 255), 1) 
  
    # finding center point of shape 
    M = cv.moments(contour) 
    if M['m00'] != 0.0: 
        x = int(M['m10']/M['m00']) 
        y = int(M['m01']/M['m00']) 
    
    # printing shape name
    if len(approx) == 3: 
        print('Triangle');
    elif len(approx) == 4: 
        print('Quadrilateral');
    else: 
        print('circle');
# displaying the image after drawing contours 
cv.imshow('shapes', img) 
  
cv.waitKey(0) 
cv.destroyAllWindows() 