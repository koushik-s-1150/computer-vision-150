import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Kiranmaye R\Pictures\Camera Roll\WIN_20240130_14_45_59_Pro.jpg")
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

#stretch_near = cv2.resize(image, (780, 540), 
			#interpolation = cv2.INTER_LINEAR)


Titles =["Original", "Half", "Bigger"]
images =[image, half, bigger]
count = 3

for i in range(count):
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()
