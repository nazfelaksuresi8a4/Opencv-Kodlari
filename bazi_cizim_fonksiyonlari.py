#opencv-python ile çizim fonksiyonları

'''Gerekli importlar'''
import cv2 as cv    
import numpy as np 

linedMatlike,rectangledMatlike,contouredImage = None,None,None

'''Hedef görüntüyü okumak'''
target_path = r"testing_png.png"
matlike = cv.imread(target_path)

'''Uzunluk ve genişlik almak'''
space = matlike.shape
height,width,depth = None,None,None

if len(space) == 3:
    height,width,depth = space

else:
    pass

'''fonksiyon için gerekli degisken atamalari'''
baslangic_x,baslangic_y = 20,0
genislik,uzunluk = width,height


'''line fonksiyonu uygulayalım'''
linedMatlike = cv.line(matlike.copy(),(baslangic_x,baslangic_y),((genislik // 2) // 2,(uzunluk // 2) // 2),(0,255,0),6*2)
cv.imshow(winname='Lined Matlike',mat=linedMatlike)
cv.waitKey(0)
cv.destroyAllWindows()

'''rectangle fonksiyonunu uygulayalım'''
rectangledMatlike = cv.rectangle(matlike.copy(),(baslangic_x,baslangic_x),((genislik // 2) // 2,(uzunluk // 2) // 2),(0,255,0),6*2)
cv.imshow(winname='Rectangled Matlike',mat=rectangledMatlike)
cv.waitKey(0)
cv.destroyAllWindows()

'''Kontür çizme fonksiyonunu uygulayalım'''
grayscale = cv.cvtColor(matlike,cv.COLOR_BGR2GRAY)
thresholded,_ = cv.threshold(grayscale,155,255,cv.THRESH_BINARY)
canny = cv.Canny(_,155,255)
contours,weights = cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
contouredImage = cv.drawContours(matlike.copy(),contours,-1,(0,255,0),4*2)

cv.imshow(winname='Contoured Matlike',mat=contouredImage)
cv.waitKey(0)
cv.destroyAllWindows()


