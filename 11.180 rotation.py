import cv2

# Read the image
img = cv2.imread(r"C:\Users\Kiranmaye R\Downloads\practical cv\dog-puppy-on-garden-royalty-free-image-1586966191.jpg")  # Replace with your image path

# Define rotation matrix for 180-degree clockwise along y-axis
rows, cols, _ = img.shape
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1.0)

# Rotate the image
rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))

# Display or save the rotated image
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the rotated image
cv2.imwrite("rotated_image.jpg", rotated_img)
