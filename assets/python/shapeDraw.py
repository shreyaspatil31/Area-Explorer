import pandas
from graphics import *

# Create a window with width and height
win = GraphWin("Point Example", 1920, 1080)

df = pandas.read_excel('../xlsx/dataset.xlsx')
for i in range(len(df)):
    # Create a Point object at the given x-y position
    point = Point(df['x1'][i], df['y1'][i])

    # Set the color of the point (e.g., red)
    point.setFill("red")

    # Draw the point on the window
    point.draw(win)

# Wait for the user to close the window
win.getMouse()
win.close()
