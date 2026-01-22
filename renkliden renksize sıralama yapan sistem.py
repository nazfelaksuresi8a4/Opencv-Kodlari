import matplotlib.pyplot as plt 
import cv2 as cv 
import os 
import numpy as np 

imgdir = str(input('image folder directory>> ')).replace('\\','/')

image_matrix,space_matrix,current_space = [],[],[]
msX = []

images = os.listdir(imgdir)

for img in images:
    if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.img') or img.endswith('.jfif'):
        path = f'{imgdir}/{img}'
        matlike = cv.imread(path)
        
        if matlike is not None:
            rgb_matrix = cv.cvtColor(matlike,cv.COLOR_BGR2RGB)
            image_matrix.append(rgb_matrix)
            for channel in range(4):
                try:
                    if rgb_matrix is not None:
                        if channel == 3:
                            space_matrix.append(current_space.copy())
                            current_space.clear()
                            break

                        spacex = cv.calcHist([rgb_matrix],[channel],None,[256],[0,256])
                        current_space.append(spacex)

                except Exception as e:
                    print(e,channel)

        else:
            print(path,' İs none')


for mlike,vec,index in zip(image_matrix,space_matrix,range(len(space_matrix))):
    H = 0
    for tX in vec:
        normalized_hist = vec / np.sum(vec)
        H += -(np.sum(normalized_hist * np.log(normalized_hist + 1e-5)))
    
    msX.append([mlike,[H,index]])
    H = 0

spacelist = [space[1] for space in msX]

outputMX = sorted(spacelist,reverse=True)

n = len(outputMX)
AIndex,SIndex = 0,0

if n %2 == 0:
    fig,ax = plt.subplots(n//2,2)

    for axis,matrix,sumF in zip(range(n),image_matrix,outputMX):
        if AIndex == 2:
            SIndex += 1
            AIndex = 0

        ax[SIndex,AIndex].imshow(image_matrix[outputMX[axis][1]])
        ax[SIndex,AIndex].set_title(f'Skor: {outputMX[axis][0]}')
        ax[SIndex,AIndex].axis(False)
        AIndex += 1
        
    plt.show()

else:
    print('İşlem devam edemiyor.... Görsel sayısı bir çift sayı olmalı')
