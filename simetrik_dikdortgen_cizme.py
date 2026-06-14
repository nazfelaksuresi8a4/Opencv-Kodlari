'''KONU: GORUNTULER UZERINDE CIZIM ISLEMLERI'''

#Görüntü matrisleri
#Görüntü matrislerinde koordinat sistemi
#OpenCv ve Matplotlib modülleri
#görselde dikdörtgen çizme 
#belirtilen koordinatlar arası çizgi çizme
#bazı geometrik şekillerin görsel üzerine çizilmesi

import cv2
import matplotlib.pyplot as plt

yol = r"C:\Users\alper\Desktop\kodlar\bildircin-zararlari.jpg"

goruntu_matrisi = cv2.imread(yol)

diktortgen_boyut_x,diktortgen_boyut_y = 200,150

merkez_y,merkez_x = goruntu_matrisi.shape[0] // 2,goruntu_matrisi.shape[1] // 2

x1 = merkez_x - diktortgen_boyut_x 
y1 = merkez_y - diktortgen_boyut_y 
x2 = merkez_x + diktortgen_boyut_x 
y2 = merkez_y + diktortgen_boyut_y

diktortgen_cekilmis = cv2.rectangle(goruntu_matrisi,
                                    (x1,y1),
                                    (x2,y2),
                                    (0,255,0),
                                    4)

plt.imshow(diktortgen_cekilmis)
plt.show()
