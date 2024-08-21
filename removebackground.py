
from rembg import remove
from PIL import Image
import cv2 
import numpy as np


img = ("img1.jpeg")
output_path = 'output5.jpeg'


input = Image.open(img)
output = remove(input)
output.save(output_path)

outputImg=cv2.imread('./output5.jpeg')
print(outputImg)
#_,mask = cv2.threshold(outputImg,230,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((3,3),np.uint8)
# dilation=cv2.dilate(mask,kernel)
erosion=cv2.erode(outputImg,kernel,iterations=1)



cv2.imshow("Image",outputImg)
# cv2.imshow("Mask",mask)
# cv2.imshow("Dilation",dilation)
cv2.imshow("erosion",erosion)
cv2.imwrite('./a.jpeg',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
