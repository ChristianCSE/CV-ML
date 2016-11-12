import cv2
video = cv2.VideoCapture(0)
if not video.isOpened():
    print "Can't open video"
    exit(-1)
cv2.namedWindow("Test")

while True:
    result, image = video.read()
    if result:
        print "Frame read!"
        cv2.imshow("Test", image)
        if cv2.waitKey(5) == ord('a'):    # Modified code from here
            break

cv2.destroyAllWindows()
video.release()