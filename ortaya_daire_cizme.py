import cv2 as cv 
import matplotlib.pyplot as plt 

img_path = r"hedef_gorsel.jpg"

matlike = cv.imread(img_path)

h,w,c = matlike.shape

p1,radx = (w // 2, h // 2),40

c = cv.circle(matlike,p1,radx,(0,255,0),2)

plt.imshow(c)
plt.show()

