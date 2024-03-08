import cv2 
import numpy as np 
  
image = cv2.imread(r"C:\Users\Kiranmaye R\Downloads\practical cv\dog-puppy-on-garden-royalty-free-image-1586966191.jpg") 
  
cv2.imshow('Original Image', image) 
cv2.waitKey(0) 
  
# Gaussian Blur 
Gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 
cv2.waitKey(0) 
