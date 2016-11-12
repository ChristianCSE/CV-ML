# import cv
# import sys
from SimpleCV import Camera, Display, Image
import time
# #init the camera
# cam = Camera(0)

# # cv.GrabFrame(cam.capture) checks
# # frame = cv.RetrieveFrame(cam.capture) checks

# #init display
# display = Display()

# #snap pic using camera
# img = cam.getImage()

# #show pic on screen
# img.save(display)



###improved hello world
cam = Camera(0)
display = Display()
img = cam.getImage()
img.save(display)
img.drawText("Hello Hello Hello Hello Hello Hello World!")
img.save(display)
time.sleep(5)
