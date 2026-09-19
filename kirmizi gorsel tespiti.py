import cv2 as cv 
import numpy as np

alpha = 0.2

lower_mask = np.array([0, 120, 120])         #kırmızı renk için alt ve üst hsv renk sınırları
upper_mask = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 120])    #aynı sınırların farklı tonlamaları 
upper_red2 = np.array([179, 255, 255])

capture = cv.VideoCapture(0)

kernel = np.ones((8,8),dtype=np.uint8)  #filtre boyutu (kernel)
smooth_x,smooth_y,smooth_w,smooth_h = 0,0,0,0

while True:
    ret,frame = capture.read()

    if ret == False:
        print('hata')
        continue

    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)    #hsv ye dönüştür.
    
    mask_1 = cv.inRange(hsv_frame,lower_mask,upper_mask)      #hsv dönüşümü uygulanan matrise alt ve üst sınırları maske olarak ver. ve çıkış olarak bu alt ve üst sınırların 1 e eşitlendiği bu sınır dışında kalanlarn 0 a eşitlendiği binary matris al boyur aynıdır.
    mask_2 = cv.inRange(hsv_frame,lower_red2,upper_red2)      #aynısını diğer alt üst sınırlar için ypar

    mask = mask_1 + mask_2    #iki maskeyi birleştirir (kırmızı ve tonlarını daha iyi algılamak için kullanılan bir toplama yöntemidir.)

    mask = cv.medianBlur(mask,7)    #maskedeki artefaktları & küçük gözle görülemeyen kırmızı pikselleri büyük oranda azaltmak için maskeye 7 kernelinde bulanıklık uygula

    mask = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)  #backgrounddaki gürültüleri 5x5 etki alanında atlayarak 0 a eşitler  binary matris döner mask ile aynı boyuta sahiptir
    mask = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)  #foregrounddaki gürültüleri 5x5 etki alanında atlayarak 1 e eşitler binary matris döner mask ile aynı boyuta sahiptir
    
    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)  #kontütr tespiti yapılır 

    masked = cv.bitwise_and(frame,frame,mask=mask)  #frame && frame = frame verir ve frame üzerine mask uygulanır. maske ve frame botyutu aynıdır bu nedenle maskenin [255,255,255,255,255,255] oldugu ve frame in [1,1,1,0,1,1] oldugu yerde bu çıkış [255,255,255,0,255,255] -> matris içindeki tek bir vektöre uygulanır böyle durur her vektör için yaparsanız matrisi maskelemiş olursunz. 

    if len(contours) > 0:  #kontür bulundumu 
        largest_contour = max(contours,key=cv.contourArea) #max ile kontür alanını anahtar vererek maksimum kontürü bul

        if cv.contourArea(largest_contour) > 500:  #eğer kontürün alanı 500 den büyükse aşşağıya geç
            x,y,w,h = cv.boundingRect(largest_contour)    #kontürün etrafındaki dikdörtgen alanı hesapla 

            if smooth_x == 0 and smooth_y == 0:  #başta 0 ise tanımla
                smooth_x,smooth_y,smooth_w,smooth_h = x,y,w,h

            else:  #zaten tanımlı ise yumuşatma formülünü uygulamaya başla
                smooth_x = int(alpha * x + (1-alpha) * smooth_x)
                smooth_y = int(alpha * y + (1-alpha) * smooth_y)
                smooth_w = int(alpha * w + (1-alpha) * smooth_w)
                smooth_h = int(alpha * h + (1-alpha) * smooth_h)
)
            frame = cv.rectangle(frame,(smooth_x,smooth_y),(smooth_x+smooth_w,smooth_y+smooth_h),(255,255,255),1)  #(x,y),(x+w,y+h) genişlik,yüksekliğinde dikdörtgen çizer. yumuşak hareket vardır(kısaca x başlangıçtan nesne genişliğine kadar y başlkangıçtan nesne yükseklşiğimne kadar bir dikdörtgen çizilir ve nesneyi çevrelr.)
            cv.putText(frame,'kirmizi_gorsel',(smooth_x,smooth_y-20),cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,255,0))  #x ekseni sabit y ekseni 40 daha az olacak şekilde bir yazı yazılır.

    cv.imshow('test',frame)
    cv.waitKey(1)

