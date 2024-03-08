import cv2 
  
img = cv2.imread(r"C:\Users\Kiranmaye R\Pictures\Camera Roll\WIN_20240130_14_45_59_Pro.jpg")  # Read image 
  
# Setting parameter values 
t_lower = 50
t_upper = 150
  
# Applying the Canny Edge filter 
edge = cv2.Canny(img, t_lower, t_upper) 
  
cv2.imshow('original', img) 
cv2.imshow('edge', edge) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
