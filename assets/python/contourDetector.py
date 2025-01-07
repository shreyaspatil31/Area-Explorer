import cv2
import pandas
 
# Read the color image
#image = cv2.imread('../images/file.png')
image = cv2.imread("C:\\Users\\shrey\\Documents\\CODE\\CODE\\assets\\images\\file.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to binary
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)

# Detect contours using the inverted binary image
contours, _ = cv2.findContours(~binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Extract contour coordinates
coordinates = {'x1': [], 'y1': []}
for contour in contours[0]:
    x, y = contour[0][0], contour[0][1]
    coordinates['x1'].append(x)
    coordinates['y1'].append(y)

# storing into excel
df = pandas.DataFrame(coordinates)
df.to_excel("C:\\Users\\shrey\\Documents\\CODE\\CODE\\assets\\xlsx\\dataset.xlsx", index=False, columns=['x1', 'y1'])
