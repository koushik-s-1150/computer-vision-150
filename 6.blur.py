import cv2
import numpy as np
img=cv2.imread(r"C:\Users\Kiranmaye R\Downloads\practical cv\dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)
cv2.imshow("image",img)
cv2.waitKey()
cv2.imshow("eroded",erosion)
cv2.waitKey()
cv2.destroyAllWindows()
