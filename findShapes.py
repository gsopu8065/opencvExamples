import cv2

#Read image
image = cv2.imread("images/shapes.jpg")

#Before contour
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
morphed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (5,5))

cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
print("Total shapes = ",len(cnts[0]))
for c in cnts[0]:
	cv2.drawContours(image, [c], -1, (0, 0, 0), 2)
	peri = cv2.arcLength(c, True)
	sides = cv2.approxPolyDP(c, 0.01 * peri, True)
	shape = "unknown"
	if len(sides) == 3:
		shape = "triangle"
	elif len(sides) == 4:
		shape = "quadrangle"
	elif len(sides) == 5:
		shape = "pentagon"
	elif len(sides) == 10:
		shape = "star"
	else:
		shape = "circle"

	print(shape, len(sides))
	cv2.imshow("Image", image)
	cv2.waitKey(0)