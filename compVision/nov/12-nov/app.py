# import cv2
# video = cv2.VideoCapture(0)
# if not video.isOpened():
#     print "Can't open video"
#     exit(-1)
# cv2.namedWindow("Test")

# while True:
#     result, image = video.read()
#     if result:
#         print "Frame read!"
#         cv2.imshow("Test", image)
#         if cv2.waitKey(5) == ord('a'):    # Modified code from here
#             break

# cv2.destroyAllWindows()
# video.release()

from SimpleCV import Camera, Display, Image
cam = Camera()
display = Display()
img = cam.getImage()
img.save(display)

# import cv2
# c = cv2.VideoCapture(0)
# val, img = c.read()
# print val #this should be True
# print img #this should not be all 0s
#
# from SimpleCV import Camera, Display, Image
# import cv
# mycam = Camera()
# cv.GrabFrame(mycam.capture)
# frame = cv.RetrieveFrame(mycam.capture)