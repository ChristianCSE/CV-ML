import cv
import sys
from SimpleCV import Camera, Display, Image
cam = Camera(0)
# cv.GrabFrame(cam.capture)
# frame = cv.RetrieveFrame(cam.capture)
display = Display()
img = cam.getImage()
img.save(display)
