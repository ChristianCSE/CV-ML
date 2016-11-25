from SimpleCV import Image, Display
import time

display = Display()
Image("logo").save(display)
# img = Image("logo")
# img.show(type="browser")
print "I launched a window"

while not display.isDone():
  time.sleep(0.1)

print "Manually closed the window"