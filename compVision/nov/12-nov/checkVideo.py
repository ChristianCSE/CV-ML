import cv2
c = cv2.VideoCapture(0)
val, img = c.read()
print val #this should be True
print img #this should not be all 0s