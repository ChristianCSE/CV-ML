from SimpleCV import Camera, Display, Image
import time
img = Image('logo')
blobs = img.findBlobs(100)
print blobs

#Prints out
#[SimpleCV.Features.Blob.Blob object at (146, 28) with area 20, SimpleCV.Features.Blob.Blob object at (182, 218) with area 63, SimpleCV.Features.Blob.Blob object at (116, 31) with area 70, SimpleCV.Features.Blob.Blob object at (119, 222) with area 82, SimpleCV.Features.Blob.Blob object at (103, 218) with area 152, SimpleCV.Features.Blob.Blob object at (56, 222) with area 153, SimpleCV.Features.Blob.Blob object at (198, 222) with area 160, SimpleCV.Features.Blob.Blob object at (81, 222) with area 173, SimpleCV.Features.Blob.Blob object at (161, 219) with area 193, SimpleCV.Features.Blob.Blob object at (135, 215) with area 264, SimpleCV.Features.Blob.Blob object at (125, 125) with area 60792]