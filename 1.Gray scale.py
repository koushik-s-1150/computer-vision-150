import cv2
image=cv2.imread(r"C:\Users\Kiranmaye R\Downloads\practical cv\dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
cv2.imshow("original",image)
cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("converted",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
