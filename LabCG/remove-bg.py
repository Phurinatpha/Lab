import cv2

# Load the image
img = cv2.imread('/Lab/LabCG/img/or-cat.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary mask
_, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Apply the mask to the original image
result = cv2.bitwise_and(img, img, mask=mask)

# Save the resulting image
cv2.imwrite('/Lab/LabCG/img/or-cat.png', result)
