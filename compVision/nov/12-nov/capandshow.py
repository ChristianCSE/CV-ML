from SimpleCV import Camera
cam = Camera(0, {"width": 640, "height": 480})
img = cam.getImage()
img.drawText("ayy I'm camera 0", 160, 120)
img.show()