import cv2 as cv

img_1 = 'cpp_logo.png'
img_2 = 'python_logo.webp'

mat_1 = cv.imread(img_1)
mat_2 = cv.imread(img_2)

row,col,channels = mat_1.shape

roi = mat_2[0:row, 0:col]

mat_1_gray = cv.cvtColor(mat_1,cv.COLOR_BGR2GRAY)
_ ,mask = cv.threshold(mat_1_gray,220,255,cv.THRESH_BINARY_INV)

mask_inv = cv.bitwise_not(mask)

bg = cv.bitwise_and(roi,roi,mask=mask_inv)
fg = cv.bitwise_and(mat_1,mat_1,mask=mask)

dest = cv.add(bg,fg)

mat_2[0:row,0:col] = dest

cv.imshow('dested images',mat_2)
cv.waitKey(0)
cv.destroyWindow()

'''
burada yapılan şey temelde şudur; opencvde maskeleri direkt olarak uygulamak için bir fonksiyon olmadıugı için and bitwise fonksiyonu kullanılır

roi^roi = roi verir roi^mask_inv ise roi'e roi'i uygular bunu mask içinde tam tersi olacka şekilde yapar 
birinde arka plan kalır (mat_1'de)
birinde ise logo kalır(roi'de)
'''


'''
mask kullanımında maskedeki 0  lar ve 1 ler şunları ifade eder

'''
ters ve düz maske kullanımı:

ters ve düz maske kullanılmasını sebebi şuıdur 
thresh inv normal thresholdun tersini alır yani kenarlar beyaz ortalara doğru siyahtır. bu nedenle ters maske bitwise_not(mask) kısmından ters maske olur yani kenarlar siyah ortalar beyaz olur 
iki tarafta (mat_1 ve roi) farklı maskeler kullanılma sebebi ise şudur; mat_1 foreground görselimizi temsil eder bu nedenle mat_1 ile normal maske karşılşaştırılır normal maskede kenarlar 1 ve ortalar 0 olacağı için çıkış olarak kenarlar 1 ortalar 0 olan bir görsel çıkar 
bg kısmında ise durum tam tersidir mask_inv kullanıdlığı için roi görselinin mask_inv ile kesiştiği noktalarda yapılan karşılaştırmada ters  maskede kenar 0 ortalar 1 olacağı için burada durum şu şekildedir mat_1 eğerki kenarları 0 ortaları 1 bir matris ise görsel oldugu gibi çıakr ancak biz burada ortalar 1 kenarları 0 bir görsel kullandıgımız için karanlık bir görsel çıkar bg + fg de buradan direkt olarak fg yi verir bu sebeple


hedef matriste maskenin herhangi bir elemanının koordinatina gelindiği zaman maskenin i. elemanı 0 ise matrisin i. elemanı zorla 0 yapılır.  
eğerki maskenin i. elemnanı 1 olsaydfı (yani mask[i] > 0 ise == 1 olmak üzere)  and karşılaştırmasını ikisi arasında yapar teknik olarak roi ve roi = roi vereceği için burada yapılacak karşılaştırma 
direkt olarak matrisin i. elemanını verecektir.
