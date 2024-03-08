import cv2 
  
# importing library for plotting 
from matplotlib import pyplot as plt 
  
# reads an input image 
img = cv2.imread(r"C:\Users\Kiranmaye R\Pictures\Camera Roll\WIN_20240130_14_45_59_Pro.jpg") 
  
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
  
# show the plotting graph of an image 
plt.plot(histr) 
plt.show() 
